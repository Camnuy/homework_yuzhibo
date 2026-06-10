from __future__ import annotations

from pathlib import Path
import traceback

import gradio as gr
import pandas as pd
from PIL import Image, ImageOps

from reference_board_tool.clip_embedder import ClipEmbedder
from reference_board_tool.config import LABEL_DESCRIPTIONS, resolve_project_path
from reference_board_tool.retrieval import cosine_rank, load_bundle


bundle = load_bundle()
catalog_df = pd.DataFrame(bundle["catalog"])
reference_embeddings = bundle["embeddings"]
embedder = ClipEmbedder()


def _prepare_image(image: Image.Image, max_size: int = 1536) -> Image.Image:
    prepared = ImageOps.exif_transpose(image).convert("RGB")
    prepared.thumbnail((max_size, max_size))
    return prepared


def _build_outputs(ranked_indices: list[int], ranked_scores: list[float], query_note: str):
    gallery = []
    rows = []
    matched_labels = []
    for index, score in zip(ranked_indices, ranked_scores):
        row = catalog_df.iloc[index]
        matched_labels.append(row["label"])
        caption = f'{row["label"]} | {row["title"]} | sim={score:.3f}'
        gallery.append((str(resolve_project_path(row["image_path"])), caption))
        rows.append(
            {
                "label": row["label"],
                "title": row["title"],
                "creator": row["creator"],
                "similarity": round(float(score), 4),
                "brief_hint": row["brief_hint"],
            }
        )

    lead_label = matched_labels[0] if matched_labels else "unknown"
    summary = (
        f"Query mode: {query_note}\n\n"
        f"Top reference direction: {lead_label}\n\n"
        f"Creative note: {LABEL_DESCRIPTIONS.get(lead_label, '')}"
    )
    return summary, pd.DataFrame(rows), gallery


def search_by_image(image: Image.Image):
    if image is None:
        return "Please upload an image.", None, None
    try:
        prepared_image = _prepare_image(image)
        query_embedding = embedder.encode_image(prepared_image)
        ranked_indices, ranked_scores = cosine_rank(query_embedding, reference_embeddings, top_k=6)
        return _build_outputs(ranked_indices, ranked_scores, "image query")
    except Exception as exc:
        traceback.print_exc()
        return f"Processing failed: {exc}", pd.DataFrame([{"error": str(exc)}]), []


def search_by_text(text_query: str):
    if not text_query or not text_query.strip():
        return "Please enter a text brief.", None, None
    try:
        query_embedding = embedder.encode_text(text_query.strip())
        ranked_indices, ranked_scores = cosine_rank(query_embedding, reference_embeddings, top_k=6)
        return _build_outputs(ranked_indices, ranked_scores, f'text brief: "{text_query.strip()}"')
    except Exception as exc:
        traceback.print_exc()
        return f"Processing failed: {exc}", pd.DataFrame([{"error": str(exc)}]), []


with gr.Blocks(title="Artist Style Retrieval and Reference Board Tool") as demo:
    gr.Markdown("# Artist Style Retrieval and Reference Board Tool")
    gr.Markdown(
        "Search the reference library with an image or a short creative brief, then browse the most relevant visual references."
    )

    with gr.Tab("Search By Image"):
        with gr.Row():
            image_input = gr.Image(type="pil", label="Upload Query Image")
            with gr.Column():
                image_summary = gr.Textbox(label="Search Summary", lines=5)
                image_table = gr.Dataframe(label="Ranked Results", interactive=False)
        image_gallery = gr.Gallery(label="Reference Matches", columns=3, height="auto")
        image_button = gr.Button("Find Related References")
        image_button.click(search_by_image, inputs=image_input, outputs=[image_summary, image_table, image_gallery])

    with gr.Tab("Search By Text Brief"):
        text_input = gr.Textbox(
            label="Creative Brief",
            placeholder="Try something like: monumental, calm, painterly, architectural",
            lines=3,
        )
        text_summary = gr.Textbox(label="Search Summary", lines=5)
        text_table = gr.Dataframe(label="Ranked Results", interactive=False)
        text_gallery = gr.Gallery(label="Reference Matches", columns=3, height="auto")
        text_button = gr.Button("Search By Brief")
        text_button.click(search_by_text, inputs=text_input, outputs=[text_summary, text_table, text_gallery])


if __name__ == "__main__":
    demo.launch(inbrowser=True, show_error=True)

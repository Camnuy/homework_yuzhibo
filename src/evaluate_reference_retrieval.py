from __future__ import annotations

import json

import pandas as pd

from reference_board_tool.config import REPORTS_ROOT
from reference_board_tool.retrieval import cosine_rank_excluding_self, load_bundle


def main() -> None:
    bundle = load_bundle()
    catalog_df = pd.DataFrame(bundle["catalog"])
    embeddings = bundle["embeddings"]

    top1_hits = 0
    top3_hits = 0
    rows: list[dict] = []

    for query_index, row in catalog_df.iterrows():
        ranked_indices, ranked_scores = cosine_rank_excluding_self(query_index, embeddings, top_k=3)
        ranked_rows = catalog_df.iloc[ranked_indices]

        top1_label = ranked_rows.iloc[0]["label"]
        top3_labels = ranked_rows["label"].tolist()
        query_label = row["label"]

        top1_match = int(top1_label == query_label)
        top3_match = int(query_label in top3_labels)

        top1_hits += top1_match
        top3_hits += top3_match

        rows.append(
            {
                "query_image": row["image_name"],
                "query_label": query_label,
                "top1_label": top1_label,
                "top1_score": round(float(ranked_scores[0]), 4),
                "top3_labels": " | ".join(top3_labels),
                "top1_match": top1_match,
                "top3_match": top3_match,
            }
        )

    total = len(catalog_df)
    metrics = {
        "num_queries": total,
        "top1_label_agreement": round(top1_hits / total, 4),
        "top3_label_agreement": round(top3_hits / total, 4),
        "note": "These metrics use broad folder labels only as a proxy for relatedness.",
    }

    REPORTS_ROOT.mkdir(parents=True, exist_ok=True)
    predictions_path = REPORTS_ROOT / "retrieval_case_studies.csv"
    metrics_path = REPORTS_ROOT / "retrieval_metrics.json"
    summary_path = REPORTS_ROOT / "retrieval_summary.md"

    pd.DataFrame(rows).to_csv(predictions_path, index=False, encoding="utf-8")
    with metrics_path.open("w", encoding="utf-8") as handle:
        json.dump(metrics, handle, indent=2, ensure_ascii=False)
    with summary_path.open("w", encoding="utf-8") as handle:
        handle.write("# Retrieval Summary\n\n")
        handle.write(f"- Number of queries: `{metrics['num_queries']}`\n")
        handle.write(f"- Top-1 label agreement: `{metrics['top1_label_agreement']}`\n")
        handle.write(f"- Top-3 label agreement: `{metrics['top3_label_agreement']}`\n")
        handle.write(f"- Note: {metrics['note']}\n")

    print(f"Saved metrics to: {metrics_path}")
    print(f"Saved case studies to: {predictions_path}")
    print(f"Top-1 label agreement: {metrics['top1_label_agreement']}")
    print(f"Top-3 label agreement: {metrics['top3_label_agreement']}")


if __name__ == "__main__":
    main()

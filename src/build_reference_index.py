from __future__ import annotations

import numpy as np

from reference_board_tool.catalog import load_catalog
from reference_board_tool.clip_embedder import ClipEmbedder
from reference_board_tool.config import resolve_project_path
from reference_board_tool.retrieval import save_bundle


def main() -> None:
    catalog_df = load_catalog()
    paths = [resolve_project_path(path) for path in catalog_df["image_path"].tolist()]
    embedder = ClipEmbedder()
    embeddings = embedder.encode_paths(paths)
    embeddings = np.asarray(embeddings, dtype=np.float32)
    bundle_path = save_bundle(catalog_df, embeddings)
    print(f"Saved retrieval bundle to: {bundle_path}")
    print(f"Indexed references: {len(catalog_df)}")
    print(f"Embedding shape: {embeddings.shape}")


if __name__ == "__main__":
    main()

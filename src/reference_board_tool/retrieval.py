from __future__ import annotations

from pathlib import Path

import joblib
import numpy as np
import pandas as pd

from .config import ARTIFACTS_ROOT, RUNTIME_ARTIFACTS_ROOT


def cosine_rank(query_embedding: np.ndarray, reference_embeddings: np.ndarray, top_k: int = 6) -> tuple[list[int], list[float]]:
    similarities = reference_embeddings @ query_embedding
    ranked_indices = np.argsort(similarities)[::-1][:top_k]
    ranked_scores = similarities[ranked_indices].tolist()
    return ranked_indices.tolist(), ranked_scores


def cosine_rank_excluding_self(
    query_index: int,
    reference_embeddings: np.ndarray,
    top_k: int = 5,
) -> tuple[list[int], list[float]]:
    query_embedding = reference_embeddings[query_index]
    similarities = reference_embeddings @ query_embedding
    similarities[query_index] = -1.0
    ranked_indices = np.argsort(similarities)[::-1][:top_k]
    ranked_scores = similarities[ranked_indices].tolist()
    return ranked_indices.tolist(), ranked_scores


def save_bundle(catalog_df: pd.DataFrame, embeddings: np.ndarray, path: Path | None = None) -> Path:
    output_path = path or (ARTIFACTS_ROOT / "reference_index_bundle.joblib")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(
        {
            "catalog": catalog_df.to_dict(orient="records"),
            "embeddings": embeddings,
        },
        output_path,
    )
    return output_path


def load_bundle(path: Path | None = None) -> dict:
    bundle_path = path or ((RUNTIME_ARTIFACTS_ROOT if RUNTIME_ARTIFACTS_ROOT.exists() else ARTIFACTS_ROOT) / "reference_index_bundle.joblib")
    return joblib.load(bundle_path)

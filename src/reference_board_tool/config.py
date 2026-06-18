from __future__ import annotations

from pathlib import Path
import sys


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RUNTIME_ROOT = Path(getattr(sys, "_MEIPASS", PROJECT_ROOT))
DATA_ROOT = PROJECT_ROOT / "data" / "reference_board"
IMAGE_ROOT = DATA_ROOT / "images"
CATALOG_CSV = DATA_ROOT / "reference_catalog.csv"
MANIFEST_JSONL = DATA_ROOT / "source_manifest.jsonl"
ARTIFACTS_ROOT = PROJECT_ROOT / "artifacts"
REPORTS_ROOT = PROJECT_ROOT / "reports"
MODEL_ROOT = PROJECT_ROOT / "models" / "clip-vit-base-patch32"
RUNTIME_DATA_ROOT = RUNTIME_ROOT / "data" / "reference_board"
RUNTIME_ARTIFACTS_ROOT = RUNTIME_ROOT / "artifacts"
RUNTIME_MODEL_ROOT = RUNTIME_ROOT / "models" / "clip-vit-base-patch32"

EMBEDDING_MODEL_ID = "openai/clip-vit-base-patch32"

ARTIST_QUERIES = {
    "monet": [
        "\"Claude Monet\" painting",
        "\"Claude Monet\" landscape",
        "\"Claude Monet\" water lilies",
        "\"Claude Monet\" haystacks",
        "\"Claude Monet\" Rouen Cathedral",
    ],
    "vangogh": [
        "\"Vincent van Gogh\" painting",
        "\"Vincent van Gogh\" landscape",
        "\"Vincent van Gogh\" wheat field",
        "\"Vincent van Gogh\" cypress",
        "\"Vincent van Gogh\" olive trees",
    ],
    "hokusai": [
        "\"The Great Wave off Kanagawa\" Hokusai",
        "\"Fine Wind, Clear Morning\" Hokusai",
        "\"Ejiri in Suruga Province\" Hokusai",
        "\"Kajikazawa in Kai Province\" Hokusai",
        "\"Hokusai Manga\" bathing",
        "\"Hokusai\" waterfall",
        "\"Hokusai\" dragon",
        "\"Poem by Fujiwara no Yoshitaka\" Hokusai",
    ],
    "klimt": [
        "\"Gustav Klimt\" painting",
        "\"Gustav Klimt\" portrait",
        "\"Gustav Klimt\" landscape",
        "\"Gustav Klimt\" gold",
        "\"Gustav Klimt\" tree",
    ],
}

LABEL_BRIEF_HINTS = {
    "monet": "atmospheric, luminous, plein-air, soft color, impressionist",
    "vangogh": "expressive, swirling, intense color, textured, emotional",
    "hokusai": "graphic, wave-like, flattened space, printmaking, Japanese",
    "klimt": "ornamental, gold, decorative, symbolic, patterned, sensuous",
}

LABEL_DESCRIPTIONS = {
    "monet": "Atmospheric impressionist landscapes, luminous light, and soft plein-air color.",
    "vangogh": "Expressive brushwork, intense color, dynamic contour, and emotionally charged painting.",
    "hokusai": "Graphic ukiyo-e print language, flattened space, bold line, and iconic wave-like forms.",
    "klimt": "Decorative symbolism, patterned surfaces, golden ornament, intimate portraiture, and lush stylization.",
}


def resolve_project_path(path_like: str | Path) -> Path:
    path = Path(path_like)
    return path if path.is_absolute() else RUNTIME_ROOT / path

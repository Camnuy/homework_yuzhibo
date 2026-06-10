from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from .config import CATALOG_CSV, IMAGE_ROOT, LABEL_BRIEF_HINTS, MANIFEST_JSONL, PROJECT_ROOT


def _load_manifest_lookup(manifest_path: Path = MANIFEST_JSONL) -> dict[str, dict]:
    if not manifest_path.exists():
        return {}

    lookup: dict[str, dict] = {}
    with manifest_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            record = json.loads(line)
            local_image = record.get("local_image", "")
            image_name = record.get("image_name", "")
            if local_image:
                lookup[Path(local_image).name] = record
            if image_name:
                lookup[image_name] = record
    return lookup


def scan_reference_images(image_root: Path = IMAGE_ROOT) -> pd.DataFrame:
    records: list[dict[str, str]] = []
    manifest_lookup = _load_manifest_lookup()

    for label_dir in sorted(path for path in image_root.iterdir() if path.is_dir()):
        label = label_dir.name
        for image_path in sorted(label_dir.glob("*")):
            if image_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                continue

            manifest_record = manifest_lookup.get(image_path.name, {})
            title = manifest_record.get("title") or image_path.stem.replace("_", " ")
            creator = manifest_record.get("artist") or manifest_record.get("creator") or "Unknown"
            source = manifest_record.get("source") or "Wikimedia Commons"
            brief_hint = LABEL_BRIEF_HINTS.get(label, label.replace("_", " "))
            tags = ", ".join(filter(None, [label, brief_hint]))

            records.append(
                {
                    "label": label,
                    "image_name": image_path.name,
                    "image_path": image_path.relative_to(PROJECT_ROOT).as_posix(),
                    "title": title,
                    "creator": creator,
                    "source": source,
                    "brief_hint": brief_hint,
                    "tags": tags,
                }
            )

    return pd.DataFrame.from_records(records)


def save_catalog(dataset_df: pd.DataFrame, path: Path = CATALOG_CSV) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    dataset_df.to_csv(path, index=False, encoding="utf-8")
    return path


def load_catalog(path: Path = CATALOG_CSV) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Catalog not found: {path}")
    return pd.read_csv(path)

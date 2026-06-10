from __future__ import annotations

from reference_board_tool.catalog import save_catalog, scan_reference_images


def main() -> None:
    catalog_df = scan_reference_images()
    path = save_catalog(catalog_df)
    counts = catalog_df["label"].value_counts().sort_index()
    print(f"Saved catalog to: {path}")
    print("Label counts:")
    for label, count in counts.items():
        print(f"  {label}: {count}")


if __name__ == "__main__":
    main()

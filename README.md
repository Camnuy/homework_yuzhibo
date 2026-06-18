# Artist Style Retrieval and Reference Board Tool

## Project Idea

This project explores how machine learning can support creative practice through **reference retrieval** rather than classification.

The central question is:

> How can a small machine-learning system help a user search for visually related artworks and build a reference board from an image or a short text brief?

The system uses CLIP embeddings to map both images and text into the same feature space. A query is then compared against a local artist reference library and the most similar examples are returned.

## Current Scope

The current prototype focuses on four artist groups:

1. `monet`
2. `vangogh`
3. `hokusai`
4. `klimt`

This keeps the dataset compact enough for a clear demo while still showing cross-style retrieval behaviour.

## What The System Does

The tool supports two query modes:

1. upload an image and retrieve similar references
2. enter a short creative brief and retrieve similar references

The demo then shows:

1. a summary of the query mode
2. the top reference direction
3. a ranked result table
4. a gallery of matched reference images

## Repository Contents

```text
README.md
weblog.md
requirements.txt
run_demo.ps1
src/
  demo_app.py
  download_artist_reference_dataset.py
  prepare_reference_catalog.py
  build_reference_index.py
  evaluate_reference_retrieval.py
  reference_board_tool/
```

Large local assets such as downloaded images, generated index bundles, and runtime model files are not intended as core submission materials in this repository.

## How To Run

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Download the starter reference images:

```powershell
python src/download_artist_reference_dataset.py --per-query 20 --per-label 8
```

Build the catalog:

```powershell
python src/prepare_reference_catalog.py
```

Build the retrieval index:

```powershell
python src/build_reference_index.py
```

Evaluate the retrieval system:

```powershell
python src/evaluate_reference_retrieval.py
```

Launch the demo:

```powershell
.\run_demo.ps1
```

You can also run:

```powershell
python src/demo_app.py
```

and then open the local URL after the service starts.

## Why This Fits The Course

This project aligns with the course brief because it includes:

1. a machine-learning pipeline rather than only prompt use
2. dataset preparation and catalog design
3. embedding-based retrieval logic
4. a working interactive demo
5. room for critical reflection on similarity, taste, and recommendation systems

## Limitations

This is a local reference-library retrieval tool, not an internet image search engine.

Results are limited by:

1. the size of the curated artist library
2. the quality and diversity of the downloaded images
3. the fact that style similarity is partly subjective rather than absolute

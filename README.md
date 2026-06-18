# Artist Style Retrieval and Reference Board Tool

This project is an EMI 2026 final-project prototype built as a **retrieval and moodboard system** for artists and designers.

This GitHub version is a **code-and-documentation release**. Large local assets such as datasets, generated artifacts, runtime models, and packaged executables are intentionally not uploaded here.

## Important Notice For Clients

This repository is **not** a directly runnable website package.

- The `publication/` folder contains written project materials only.
- It is **not** an image folder and **not** a web page folder.
- The demo UI is a local Gradio application started from Python code.
- If you only open files on GitHub, no demo website will appear.

If you need a customer-facing runnable version, use a packaged local delivery build rather than this GitHub code repository.

Unlike a classification project, this version is centered on a different question:

> How can a machine-learning system help creators find visually related artworks and build reference boards for a creative brief?

The tool uses CLIP embeddings to index a small artist-reference library. A user can search with:

1. an uploaded image
2. a text brief such as "monumental, calm, architectural"

The system then returns the most visually relevant references from the collection.

## Current Starter Artist Library

The initial version uses a fully separate public-domain artist dataset built around four named artists:

1. `monet`
2. `vangogh`
3. `hokusai`
4. `klimt`

This is intentional. The other project folder uses a different topic and a different dataset structure, so the two assignments do not share the same image corpus.

## Project Direction

This is the **retrieval / recommendation** project in the two-project split:

- `homework_nan` = retrieval, ranking, reference board building
- `homework女` = classification, subjective style judgement, critical error analysis

## What Is In The Repo

```text
docs/                                 project notes and assignment-facing documentation
publication/                          client-facing overview and release notes
src/prepare_reference_catalog.py
src/build_reference_index.py
src/evaluate_reference_retrieval.py
src/demo_app.py
src/reference_board_tool/             shared retrieval code
scripts/                              packaging and setup helpers
reports/                              evaluation summary files
weblog.md                             project weblog draft
```

## Current Initial Version

The current initial version already includes:

1. a distinct artist-reference library
2. CLIP-based image and text retrieval
3. index-building and evaluation code
4. a Gradio demo for searching by image or text
5. a starter retrieval evaluation script

## How To Run

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Prepare a clean catalog:

```powershell
python src/prepare_reference_catalog.py
```

Build the CLIP retrieval index:

```powershell
python src/build_reference_index.py
```

Run the starter evaluation:

```powershell
python src/evaluate_reference_retrieval.py
```

Launch the demo:

```powershell
python src/demo_app.py
```

For this GitHub release, you should prepare your own local dataset and build the retrieval index locally before running the demo.

## Why This Fits EMI

This project aligns with the brief because it includes:

1. machine-learning code rather than only off-the-shelf AI tools
2. a direct connection to creative practice
3. a clear process from dataset preparation to interface demo
4. room for critical reflection about taste, similarity, and recommendation systems

## Notes

This repo is intentionally framed as a **reference-finding tool**, not a style classifier. It also uses a fully separate dataset from the second project folder.

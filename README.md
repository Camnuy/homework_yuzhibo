# Artist Style Retrieval and Reference Board Tool

Weblog link: [weblog.md](weblog.md)

Link to video: https://pan.baidu.com/s/1ZUVxxH3AhwEzXIsMDNPn3Q?pwd=este

## Introduction

This project explores a simple question: how can machine learning support creative research without turning the task into a rigid classification problem? Instead of asking a system to decide what an artwork "is," I wanted to build a tool that helps a user search for visually related references and assemble a small moodboard from either an uploaded image or a short descriptive prompt.

My motivation came from the way designers and artists often work with references. In early project planning I found that many image-AI examples focus on generation, but I was more interested in retrieval: a lightweight system that helps someone move from a rough visual intuition to a useful set of comparable images. The final objective was therefore to build a local artist-reference retrieval tool that:

1. accepts both image and text queries
2. embeds queries and reference images in the same feature space
3. returns a ranked set of related references with captions
4. presents the results through a small interactive interface

## Related Technical and/or Creative Work

The most important technical reference for this project is CLIP, a vision-language model trained to align text and images in a shared embedding space (Radford et al., 2021). CLIP made it possible to keep the system small while still supporting both image-to-image retrieval and text-to-image retrieval. This was important because the project is less about formal labelling and more about open-ended creative search.

The project is also related to the broader area of content-based image retrieval, where similarity is computed from image features rather than keyword metadata alone. In a practical design context, the workflow is also influenced by online reference-board and moodboard practices: users collect examples, compare variations in composition and palette, and look for visual direction rather than one single "correct" answer. My project is a deliberately compact version of that workflow, focused on a curated local library rather than a web-scale archive.

For the interface I used Gradio Blocks, which provided a clear way to expose the retrieval model as a lightweight local demo (Gradio, 2026). For the image source material I used Wikimedia Commons because it offers openly accessible cultural-image resources with metadata that can be incorporated into a small research prototype (Wikimedia Commons, 2026).

## Summary of Design and Development Process

The development process moved through five stages. First, I reframed the project away from style classification and toward reference retrieval, because that matched my creative intention more closely. Second, I designed a small dataset strategy: four artist groups (`monet`, `vangogh`, `hokusai`, and `klimt`) with a compact library of reference images and source metadata. Third, I built a pipeline that scans the local image folders, creates a catalog, computes CLIP embeddings, and saves an index bundle for fast retrieval. Fourth, I built a Gradio demo with two search modes: upload an image or enter a short creative brief. Finally, I evaluated the system with simple quantitative checks and qualitative testing, then revised the image library to reduce repeated motifs and improve the clarity of the returned examples.

The weblog documents these iterations in more detail, especially the shift in scope, the dataset curation process, the evaluation logic, and the final packaging work. Key entries include the [dataset strategy entry](weblog.md#2026-06-03---defining-the-dataset), the [evaluation entry](weblog.md#2026-06-11---retrieval-evaluation), and the [final packaging entry](weblog.md#2026-06-17---packaging-for-submission).

## Summary of Final Version

The final version is a local interactive retrieval tool rather than a generator. A user can upload an image or type a short text brief such as "ornamental gold portrait" or "calm blue landscape," and the system returns the closest matches from the local artist-reference library. Each result includes a label, title, creator field, similarity score, and a gallery image.

At the time of submission, the project works in the following sense:

1. it can download a starter dataset from Wikimedia Commons
2. it can build a local reference catalog
3. it can compute and save image embeddings
4. it can retrieve similar references from either image or text input
5. it can display results in a local Gradio interface

The current scope is intentionally modest. The tested local working set contains four artist groups and a small curated reference collection. The project does not perform live internet image search, does not automatically learn from user feedback, and does not claim that similarity is objective. It is better understood as a creative-support prototype than as a production search engine.

## Evaluation

I evaluated the project in two ways: a simple quantitative proxy and qualitative inspection. For the quantitative step, I used the script `src/evaluate_reference_retrieval.py`, which checks whether items from the same broad folder label tend to appear near the top of the ranked results when each reference image is queried against the rest of the library. On the local working set used for testing, this produced:

1. Top-1 label agreement: `0.7188`
2. Top-3 label agreement: `0.875`

These numbers should be treated carefully. The folder labels are only a rough organizational proxy, not a ground-truth measure of visual meaning. However, the results were still useful as a sanity check that the embeddings and ranking pipeline were behaving plausibly.

The more meaningful evaluation was qualitative. In testing, the system was able to separate broad visual directions such as Klimt's ornamental gold patterning, Van Gogh's expressive texture, Monet's atmospheric landscape treatment, and Hokusai's graphic print-like structure. One issue that emerged during development was that some Hokusai examples were too repetitive, especially around wave imagery. I therefore revised the local image set to make that category more varied, adding non-wave scenes so that the retrieval gallery felt more like a style reference set than a single-motif collection.

Overall, I think the project met its main objective: it demonstrates a working machine-learning-assisted reference search workflow and makes the design decisions visible enough to discuss critically.

## Reflection and Conclusion

In the end, I am satisfied with the project because it became more coherent once I stopped treating it as a classification task and treated it instead as a creative retrieval tool. That change in framing improved both the technical design and the user experience. The system now has a clear purpose: help a user move from a visual cue to a small, interpretable set of references.

If I continued the project, I would expand it in three directions. First, I would build a larger and better-balanced reference library, because the current system is strongly shaped by the size and composition of the local dataset. Second, I would add stronger metadata tools, such as filtering by subject matter or time period. Third, I would explore lightweight relevance feedback, so that the user could mark results as useful or not useful and refine the search over time.

The main lesson from the project is that a small machine-learning system can still be valuable when it is designed around a realistic creative task. It does not need to generate images or claim perfect understanding to be useful; it only needs to return references that help the user think and compare.

## Repository Structure and Instructions for Running

### Repository structure

- `README.md`: final project overview and submission-facing documentation
- `weblog.md`: dated development log with iterative progress notes
- `weblog_assets/`: images embedded in the weblog entries
- `requirements.txt`: Python dependencies
- `run_demo.ps1`: Windows launcher for the local Gradio demo
- `src/demo_app.py`: main interactive demo application
- `src/download_artist_reference_dataset.py`: downloads starter reference images from Wikimedia Commons
- `src/prepare_reference_catalog.py`: scans local images and builds `reference_catalog.csv`
- `src/build_reference_index.py`: computes CLIP embeddings and saves the retrieval bundle
- `src/evaluate_reference_retrieval.py`: runs a simple retrieval evaluation
- `src/reference_board_tool/catalog.py`: catalog loading and saving utilities
- `src/reference_board_tool/clip_embedder.py`: CLIP model wrapper for image and text embeddings
- `src/reference_board_tool/config.py`: project paths, labels, and query configuration
- `src/reference_board_tool/retrieval.py`: cosine-similarity ranking and bundle persistence

Large runtime files such as downloaded images, generated index bundles, and model caches are intentionally not committed to the repository.

### Running the project

The project was developed and tested in Python 3.11 with Anaconda on Windows. A typical setup is:

```powershell
conda create -n emi_retrieval python=3.11
conda activate emi_retrieval
cd <your-local-repo-path>
python -m pip install -r requirements.txt
```

Download a starter image set:

```powershell
python src/download_artist_reference_dataset.py --per-query 20 --per-label 8
```

Build the local catalog:

```powershell
python src/prepare_reference_catalog.py
```

Build the retrieval index:

```powershell
python src/build_reference_index.py
```

Optional evaluation:

```powershell
python src/evaluate_reference_retrieval.py
```

Launch the demo:

```powershell
.\run_demo.ps1
```

or:

```powershell
python src/demo_app.py
```

Then open:

```text
http://127.0.0.1:7860
```

On first run, if the CLIP model is not already cached locally, the Hugging Face libraries may need to download model files before the interface becomes available.

## Use of External Resources

### Statement on Use of AI Tools

AI tools were used during the development of this project. In particular, I used OpenAI language-model tools for brainstorming, debugging, code revision support, packaging help, and drafting technical explanations while building the repository. I used these tools as assistive support rather than as an autonomous author of the whole project. The project topic, scope, testing decisions, data curation choices, and final selection of what stayed in the repository were directed by me. I reviewed, edited, and tested the resulting code and documentation locally.

### Use of Other Third-Party Resources

I used several third-party libraries and resources:

1. the pretrained CLIP model and Hugging Face `transformers` library for multimodal embeddings
2. PyTorch as the model runtime
3. Gradio for the local interactive interface
4. Wikimedia Commons as the source for the starter reference images
5. standard Python data-processing libraries including `numpy`, `pandas`, `Pillow`, `requests`, and `joblib`

I did not copy large blocks of external tutorial code verbatim into the project. The repository mainly uses these libraries through their documented APIs.

## References

Gradio (2026) *Gradio documentation*. Available at: https://www.gradio.app/docs (Accessed: 18 June 2026).

Radford, A., Kim, J.W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., Sastry, G., Askell, A., Mishkin, P., Clark, J., Krueger, G. and Sutskever, I. (2021) *Learning transferable visual models from natural language supervision*. Available at: https://arxiv.org/abs/2103.00020 (Accessed: 18 June 2026).

Wikimedia Commons (2026) *Wikimedia Commons*. Available at: https://commons.wikimedia.org/ (Accessed: 18 June 2026).

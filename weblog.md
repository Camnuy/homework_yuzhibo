# Research and Implementation Weblog

> Draft note: this is a starter weblog structure. Before submission, rewrite it in the student's own voice.

## 2026-06-01 - Topic framing

- Chose to build an artist style retrieval and reference board tool.
- Defined the project as a creative search system rather than a classification task.
- Wanted the tool to feel useful to people collecting moodboard references.

## 2026-06-02 - Core project question

- Clarified that the main question is about visual similarity and inspiration search.
- Decided the system should accept both image queries and text briefs.
- Noted that similarity is also subjective, not purely objective.

## 2026-06-03 - Dataset strategy

- Chose to start with a small curated library instead of a massive archive.
- Reused a compact image collection so the first prototype could be built quickly.
- Planned to keep provenance notes for the reference images.

## 2026-06-04 - Model choice

- Selected CLIP because it supports both image and text embeddings.
- This was important because the project needs image-to-image retrieval and text-to-image retrieval.
- Decided not to train a classifier in this version.

## 2026-06-05 - Catalog design

- Planned a reference catalog with image paths, labels, tags, titles, and source notes.
- Treated labels as organizational hints rather than final truth.
- Wanted gallery captions to help users browse references more meaningfully.

## 2026-06-06 - Index building

- Built a pipeline to embed every reference image and save the retrieval index.
- This separates indexing from demo runtime and makes the system easier to explain.
- Planned to store embeddings so the demo can launch quickly.

## 2026-06-07 - Demo design

- Designed the demo with two search modes: image query and text brief query.
- The intended experience is closer to searching a reference archive than using a classifier.
- Decided the output should show a ranked gallery and similarity scores.

## 2026-06-08 - Evaluation plan

- Considered how to evaluate retrieval even though the task is not standard classification.
- Chose a simple starter metric: whether related items appear near the top of the results.
- Planned to use category overlap only as a rough proxy, not as perfect truth.

## 2026-06-09 - Critical reflection

- Reflected on how recommendation systems shape what creators see first.
- The system may reinforce narrow definitions of style if the dataset is too small or too biased.
- This makes the project useful for both practical design and critical discussion.

## 2026-06-10 - Final framing

- Finalized the project as a reference-board assistant with a machine-learning search layer.
- Positioned it as a creative tool plus a critique of algorithmic visual similarity.
- This framing feels distinct from a style-classification project.

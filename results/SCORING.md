# Scoring rules

How the per-item records were scored to produce the numbers in the paper.
The records are `runs/**/stage34_examples.csv` for Stages 3 and 4,
`runs/stage1/citeworth/stage1_predictions.jsonl` for Stage 1,
`runs/stage2_availability/stage2_references.csv` for Stage 2, and
`ground_truth/annotation/gold_rows.csv` for the end-to-end evaluation.
The survey is described in `runs/survey/SCHEMA.md`.

**Stage 1 detection (CiteWorth).** A predicted citance counts as correct if it
covers at least half of a ground-truth sentence's tokens. At sentence level,
several predicted sub-spans of the same sentence count once. At span level,
each predicted span is matched to at most one ground-truth sentence, requiring
a token Jaccard similarity of at least 0.5. `regex_metrics.json` scores the
regex detector alone; `stage1_metrics.json` scores the shipped hybrid.

**Stage 1 PDF vs LaTeX.** The `\cite` commands in the LaTeX source are the
ground truth. A detection on the PDF side counts under the same half-coverage
rule. The reported recall is averaged over the 8 papers that have citations,
weighted by each paper's citation count.

**Stage 2 availability.** A reference is resolved only if the retrieval chain
returned a full-text PDF that opened. Abstract-only hits do not count. The
cross-check classes are: an open-access copy exists but the chain missed it,
no free copy is known anywhere, and no identifier was available to search.

**Stage 3 localization.** A hit means a ground-truth evidence sentence appears
among the top k located passages, with k=3 unless stated otherwise. MRR uses
the rank of the first hit. Recall@k is the fraction of ground-truth sentences
found.

**Stage 4 verdicts.** The tool's four labels are mapped to the datasets' three.
The lenient mapping treats Partially Supported as Supported, the strict mapping
treats it as Not Enough Information. Table 4 reports both.

**End-to-end annotation (Table 6).** A located evidence sentence matches an
annotated one if, after Unicode normalization and removal of non-alphanumeric
characters, one contains the other or their fuzzy ratio is at least 0.85.
Attribution accuracy comes from the `attribution_correct` column of
`ground_truth/annotation/gold_rows.csv`.

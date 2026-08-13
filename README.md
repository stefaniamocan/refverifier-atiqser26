# RefVerifier, ATIQSER '26 reproduction package

Evaluations reported in *RefVerifier: Semi-Automated Reference Claim
Verification for Scientific Manuscripts*. All LLM results use `gpt-5.6-terra`.

## Layout

`data/` are the inputs. The 10 arXiv papers used in the Stage 1 detection
evaluation, and the 24 bibliographies (992 references) whose resolution Stage 2
measures.

`ground_truth/` are the correct answers the tool's outputs are compared
against. Two sets: 300 CiteWorth paragraphs with their true citances, for
Stage 1, and 153 hand annotated citance-reference rows over 8 manuscripts, for
the end-to-end evaluation.

`runs/` are the tool's outputs. Each experiment, meaning one execution of the
tool on one dataset with one configuration, has its own directory. For example,
`runs/stage4/sweep/` holds seven directories, one per row of Table 5. Each
directory contains the numbers printed in the paper and a file with one row per
evaluated item, from which those numbers can be recomputed.

`results/SCORING.md` is how those per-item rows turn into the reported numbers,
stage by stage: what counts as a match, and how the tool's labels map onto each
dataset's.

`paper_manifest/runs.csv` is the index tying it together. One row per reported
run, giving its dataset, model, reasoning effort, sample size, seed, and the
directory under `runs/` that holds it.

`DATASETS.md` records where each external dataset came from, which version, and
under what licence. `DATASET_COMPARISON.md` is the comparison of established
datasets referred to in the related-work section.

`scripts/fetch_pdfs.py` downloads the 10 arXiv PDFs, which are not redistributed
here, and records their hashes.

## Human-subjects data

Participants reviewed their own unpublished manuscripts. To protect their
privacy, the survey ships closed items only, without timestamps, free text or
background items, and the per-manuscript runtime measurement is withheld.

## Licence

Code and manifests: MIT (`LICENCE`). External data keeps its source licence
(`DATASETS.md`). CiteWorth-derived files are CC BY-NC 4.0.

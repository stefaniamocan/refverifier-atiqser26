# External datasets

Every dataset row used by a reported evaluation, with the version pins needed
to resolve the same samples. No dataset is redistributed in full; `ground_truth/` and
`runs/` contain only the evaluated samples and outputs.

| Dataset | Source | Split / sample | Pin | Licence |
|---|---|---|---|---|
| CiteWorth | HF `copenlu/citeworth` | test, first 300 paragraphs (streamed, deterministic) | revision `ea2a5bde` | CC BY-NC 4.0 |
| SciFact | AllenAI release (`claims_dev.jsonl` + `corpus.jsonl`) | first 100 claims | fixed official release files | CC BY-NC 2.0 |
| SCitance | SciFact-derived (SDP 2024) | test split, first 100 | release files | per SciFact |
| SciCiteVal | HF `birdie0111/SciCiteVal` | train, first 100 | pin the revision current at run time (2026-08-13); the dataset card carries no tags | not stated on card |
| Citation-Integrity | github.com/ScienceNLP-Lab/Citation-Integrity | test; n=100 seeded (seed 20260622) for Tables 4-5; 65-span subset for Table 3 | repository default branch at clone time | per repository |
| arXiv papers (Stage 1 PDF eval) | arxiv.org | 10 fixed IDs in `data/stage1_pdf/papers_manifest.csv` | immutable arXiv versions | per-paper arXiv licences |

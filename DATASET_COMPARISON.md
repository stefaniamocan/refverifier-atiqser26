# Comparison of established claim-verification datasets

This is the full comparison referred to in the related-work section of the
paper. It covers the benchmarks surveyed for this work, not only the five used
in the evaluation. Version pins and licences for the five that were actually
run are in `DATASETS.md`.

Datasets are compared on the three dimensions that decide whether a benchmark
measures the task studied here:

- **Citation-bounded**: is the claim checked against the specific source its
  author cited, rather than against a corpus searched at retrieval time?
- **Full paper**: is the evidence the complete cited paper, rather than an
  abstract or a pre-selected passage?
- **Ground-truth evidence**: does the dataset mark which passage supports the
  label, so evidence localization can be scored separately from the verdict?

Legend: ✓ yes, ~ partial, ✗ no. Labels abbreviate Supported (S), Refuted (R),
Not Enough Information (NEI). "N/A (QA)" marks question-answering datasets,
which have no claims and no verdict labels.

## General-domain benchmarks

| Dataset | Cit.-bound. | Full paper | GT evidence | Claim source | Labels | Notes |
|---|:--:|:--:|:--:|---|---|---|
| FEVER | ✗ | ✗ | ✓ | Curated (human) | S / R / NEI | open retrieval, n ≈ 185K |
| AVeriTeC | ✗ | ✗ | ✓ | Real-world | S / R / NEI / Conflicting | question-answer evidence, n ≈ 4.6K |
| WiCE | ✗ | ✗ | ✓ | Real-world | Entailment | sub-claim level, n ≈ 2K |
| InFi-Check | ✗ | ✗ | ~ | LLM-generated | Error types | LLM-output factuality, n ≈ 16K |
| CheckThat! Lab | ✗ | ✗ | ✗ | Real-world | Multi-class | political / societal, per task |

## Scientific datasets, abstract or passage level

| Dataset | Cit.-bound. | Full paper | GT evidence | Claim source | Labels | Notes |
|---|:--:|:--:|:--:|---|---|---|
| SciFact | ✗ | ✗ | ✓ | Curated (human) | S / R / NEI | only ground-truth span set, n ≈ 1.4K |
| SCitance | ✓ | ✗ | ✓ | Citance + LLM negation | S / R / NEI | derived from SciFact, n = 656 |

## Scientific datasets, full-paper level

| Dataset | Cit.-bound. | Full paper | GT evidence | Claim source | Labels | Notes |
|---|:--:|:--:|:--:|---|---|---|
| Citation-Integrity | ✓ | ✓ | ✓ | Real citances (annotated) | Integrity to S / R / NEI | biomedical, sentence-level ground truth, n = 3,063 |
| SciCiteVal | ✓ | ~ | ✓ | Manual (from QASA) | Correct / Incorrect / Unrelated | 5 error sub-types, n = 1,034 |
| QASPER | ✓ | ✓ | ✓ | N/A (QA) | ✗ | QA, not claims, n = 5,049 |
| QASA | ✓ | ✓ | ✓ | N/A (QA) | ✗ | QA, not claims, n = 1,798 |
| SciClaimHunt | ✓ | ✓ | ✗ | LLM-generated | S / R | LLM claims, n ≈ 109K |
| SciClaimHunt-Num | ✓ | ✓ | ✗ | LLM-generated | S / R | numerical subset, n = 25,324 |

## Claim and citance detection

| Dataset | Cit.-bound. | Full paper | GT evidence | Claim source | Labels | Notes |
|---|:--:|:--:|:--:|---|---|---|
| CiteWorth | ~ | ✗ | ✗ | Real (author sentences) | Cite-worthy / not | citance detection, n ≈ 1.18M |

## Which of these the evaluation uses

Five: CiteWorth (Stage 1), SciFact, SCitance, SciCiteVal and Citation-Integrity
(Stages 3 and 4). `DATASETS.md` gives the split, sample and version pin for each.
The others were used for this analysis only and were not run.

## References

- **FEVER**. Thorne, Vlachos, Christodoulopoulos, Mittal. *FEVER: a Large-scale Dataset for Fact Extraction and VERification.* NAACL 2018.
- **AVeriTeC**. Schlichtkrull, Guo, Vlachos. *AVeriTeC: A Dataset for Real-World Claim Verification with Evidence from the Web.* NeurIPS 2023.
- **WiCE**. Kamoi, Goyal, Rodriguez, Durrett. *WiCE: Real-World Entailment for Claims in Wikipedia.* EMNLP 2023.
- **InFi-Check**. Bai, Si, Luo, Wang, Li et al. *InFi-Check: Interpretable and Fine-Grained Fact-Checking.* arXiv, 2026.
- **CheckThat! Lab**. Alam, Struß, Chakraborty et al. *The CLEF-2025 CheckThat! Lab: Subjectivity, Fact-Checking, and More.* ECIR 2025.
- **SciFact**. Wadden, Lin, Lo, Wang, van Zuylen et al. *Fact or Fiction: Verifying Scientific Claims.* EMNLP 2020.
- **SCitance**. Alvarez, Bennett, Wang. *Zero-shot Scientific Claim Verification Using LLMs and Citation Text.* SDP Workshop 2024.
- **Citation-Integrity**. Sarol, Ming, Radhakrishna, Schneider et al. *Assessing Citation Integrity in Biomedical Publications.* Bioinformatics, 2024.
- **SciCiteVal**. Liu, Zhou, Labbé. *SciCiteVal: A Multi-Domain Dataset for Scientific Citation Validation.* LREC 2026.
- **QASPER**. Dasigi, Lo, Beltagy, Cohan, Smith et al. *A Dataset of Information-Seeking Questions and Answers Anchored in Research Papers.* NAACL 2021.
- **QASA**. Lee, Lee, Park, Hwang et al. *QASA: Advanced Question Answering on Scientific Articles.* ICML 2023.
- **SciClaimHunt**. Kumar, Sharma, Khincha, Shroff et al. *SciClaimHunt: A Large Dataset for Evidence-based Scientific Claim Verification.* arXiv:2502.10003, 2025.
- **CiteWorth**. Wright, Augenstein. *CiteWorth: Cite-Worthiness Detection for Improved Scientific Document Understanding.* Findings of ACL 2021.

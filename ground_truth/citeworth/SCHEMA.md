# ground_truth/citeworth - Stage 1 detection set (Table 1)

Derived from HF `copenlu/citeworth` (test split, CC BY-NC 4.0): the first 300
paragraphs of the streamed split, deterministic, no seed - the exact sample of
the reported run.

- `sample_ids.json` - paragraph order with source paper ids.
- `gold_citances.jsonl` - one row per sentence:
  `paragraph_index, sent_idx, text, is_citance, field_of_study`.
  `is_citance` = the sentence carries a citation (CiteWorth's check-worthy
  label on the unmasked text). 1,703 sentences, 578 positive.

Scoring rules: results/SCORING.md #1.

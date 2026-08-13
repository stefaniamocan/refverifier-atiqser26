# gold_rows.csv - end-to-end annotation gold (Table 6)

Two files, same 153 rows. `gold_rows_human.csv` has the annotator's columns
only: the gold set on its own. `gold_rows.csv` adds the tool's `ai_*` columns
and the match columns: the comparison behind Table 6.

One row per citance-reference pair the tool detected on 8 public arXiv
manuscripts (153 rows, 145 with `kept=True`). Produced in the tool's annotation
mode by a single annotator (the author), stage by stage; the verdict was
assigned blind to the tool's prediction. No inter-annotator overlap exists, so
no agreement statistic can be computed.

Manuscripts (fetch from arXiv to re-check any row): 1905.02698, 1803.07640,
1911.08340, 2607.23813, 1503.02531, 2607.24268, 1804.02767, 2607.16494.

Columns prefixed `ai_` are the tool's output; their unprefixed counterparts are
the annotator's gold. Scoring rules: `results/SCORING.md`.

# Acceptance survey (closed items)

`responses.csv` holds the closed-item responses of the \surveyN{} = 11
researchers who evaluated the tool on a manuscript of their own choosing.
`metrics.json` holds the per-item aggregates reported in the paper.

## What is released, and what is not

Released: the ten closed items, as integers on the response scale.

Not released, for participant privacy:

- **Submission timestamps.** With eleven respondents a timestamp is a linkage key
  against anyone who knows when a given participant ran their session.
  Rows are additionally sorted by their response vector, so the file carries no
  submission order either.
- **The free-text suggestion field.** Respondents quoted passages and citation
  keys from the unpublished manuscripts they were reviewing. Those quotations
  identify the manuscript, and through it the respondent, and they reproduce
  third-party unpublished text. The field backs no number reported in the paper.
- **Two background items** (topic familiarity, how often the respondent
  manually inspects cited sources). Neither is reported, and one has a
  single-respondent category that would single that person out.

No participant identifier, name, affiliation, manuscript title, or session log
is present in this package in any form.

## Columns

`respondent` is a row index over the sorted file. It is not a participant ID
and carries no meaning across files.

| Code | Construct | Item |
|---|---|---|
| B1 | Perceived usefulness | Using the tool would enhance my performance in checking whether cited sources support claims. |
| B2 | Perceived usefulness | Using the tool would enhance my effectiveness in identifying unsupported claims. |
| B3 | Perceived usefulness | Using the tool would make citation-support verification easier. |
| B4 | Perceived usefulness | I would find the tool useful for checking citation support in scientific manuscripts. |
| C1 | Perceived ease of use | Learning to operate the tool was easy for me. |
| E1 | Stage 1 quality | The tool found all relevant claims in the manuscript. |
| E2 | Stage 3 quality | The tool presented the correct evidence passages for the claims. |
| E3 | Stage 4 quality | The tool's verdicts were correct, or at least plausible. |
| E4 | Reliance | For claims the tool marked as Supported, I would accept the verdict without checking the source myself. |
| E5 | Reliance | For claims the tool marked as Not Supported, I would check the source myself before accepting the verdict. |

## Scale

Seven points, recorded as integers:

| 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|
| Strongly disagree | Disagree | Somewhat disagree | Neutral | Somewhat agree | Agree | Strongly agree |

Respondents chose from the labels; the integers are the encoding applied here.
No respondent left a closed item blank, so every item has n = 11.

# Human-written samples (criteria 1 and 2)

`scenarios.py` loads every `.txt` file in this folder as one human sample.

## Provenance

| Files | Author | Provenance |
|---|---|---|
| `human_01.txt`, `human_02.txt` | the student | Original writing, preserved verbatim |
| `human_03.txt` – `human_20.txt` | six published authors (Stevenson, Post, Eddy, Trollope, Paine, Murphy) | Public-domain excerpts from Project Gutenberg, **not the student's writing**. Per-file author, work and URL are in `SOURCES.csv` |

All 20 are known human-written, which is what `criteria.md` criterion 1 asks for
("20 known human-written samples"). The starter's `scenarios.py` asked for the
student's *own* writing; only two of these are. The other eighteen are older,
literary prose from about 1850–1925. RUNNING.md notes that dense, rare-word prose tends to
read as human to signal one, so this set is likely *easier* to pass than plain
modern writing. Results are reported separately for the two groups in the README.

# Dev-Demo

This is a simple offline toolset to practice behavior overlap detection.

## 📂 Files

- `main.py` — Runs the full local pipeline: loads sample behaviors, checks for duplicates, overlaps, and toy conflicts.
- `utils.py` — Contains helper functions: `find_exact_duplicates()`, `find_similar_behaviors()`, `find_conflicts()`.
- `sample_behaviors.json` — Small local test dataset.
- `test_main.py` — Unit tests for the utility functions.

## ⚙️ How to run

Run the pipeline:
```bash
python3 main.py
```

Run the tests:
```bash
python3 -m unittest test_main.py
```

## ✅ Features

- Finds exact duplicate behaviors
- Detects similar behaviors with fuzzy match
- Flags toy conflicting behaviors
- Fully unit-tested with reproducible results

## 🗂️ Next Steps

- Add more realistic test data
- Expand the conflict checker logic
- Try connecting to a company's live API instead of JSON
# NFL Big Data Bowl 2026: Prediction

Predict NFL player movement (x, y) in the frames after the ball is thrown, using pre-throw tracking data.

Competition: https://www.kaggle.com/competitions/nfl-big-data-bowl-2026-prediction

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

```bash
kaggle competitions download -c nfl-big-data-bowl-2026-prediction -p data/raw
unzip data/raw/nfl-big-data-bowl-2026-prediction.zip -d data/raw
```

## Layout

```
data/raw/          original Kaggle files (not committed)
data/processed/    derived tables (not committed)
notebooks/         exploration
src/               reusable code
scripts/           training / submission scripts
models/            saved models (not committed)
submissions/       submission files (not committed)
reports/           notes, figures
```

## Notes

(Add experiment log, validation scheme, and results here.)

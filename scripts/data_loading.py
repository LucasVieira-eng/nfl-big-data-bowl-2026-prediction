'''

folder: pode ser uma string ou um Path, de qualquer lugar do seu computador.

pattern: por padrão pega todos os CSVs, então você só precisa especificá-lo quando quiser um subconjunto.

recursive=True: também procura nas subpastas.

add_source: controla se a coluna source_file é adicionada.

**read_kwargs: repassa qualquer argumento extra direto para o pl.read_csv,
por exemplo read_all(TRAIN, "input_*.csv", columns=["game_id", "play_id", "x", "y"])
para carregar só algumas colunas e economizar memória.
'''

import polars as pl
from pathlib import Path

def read_all(folder, pattern="*.csv", add_source=True, recursive=False, **read_kwargs) -> pl.DataFrame:
    """Read and stack every CSV in `folder` that matches `pattern`."""
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    files = sorted(folder.rglob(pattern) if recursive else folder.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matching '{pattern}' in {folder}")
    print(f"{folder.name}/{pattern}: found {len(files)} files")

    read_kwargs.setdefault("infer_schema_length", 10000)
    frames = []
    for f in files:
        df = pl.read_csv(f, **read_kwargs)
        if add_source:
            df = df.with_columns(pl.lit(f.stem).alias("source_file"))
        frames.append(df)
    return pl.concat(frames, how="vertical_relaxed")
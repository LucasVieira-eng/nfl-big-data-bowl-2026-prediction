from pathlib import Path

import pandas as pd


def read_all(folder, pattern="*.csv", add_source=True, recursive=False, **read_kwargs) -> pd.DataFrame:
    """
    Read and stack every CSV in `folder` that matches 'pattern'.

    folder: pode ser uma string ou um Path, de qualquer lugar do seu computador.

    pattern: por padrão pega todos os CSVs, então você só precisa especificá-lo quando quiser um subconjunto.

    recursive=True: também procura nas subpastas.

    add_source: controla se a coluna source_file é adicionada.

    **read_kwargs: repassa qualquer argumento extra direto para o pl.read_csv,
    por exemplo read_all(TRAIN, "input_*.csv", columns=["game_id", "play_id", "x", "y"])
    para carregar só algumas colunas e economizar memória.
    """
    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"Folder not found: {folder}")

    files = sorted(folder.rglob(pattern) if recursive else folder.glob(pattern))
    if not files:
        raise FileNotFoundError(f"No files matching '{pattern}' in {folder}")
    print(f"{folder.name}/{pattern}: found {len(files)} files")

    frames = []
    for f in files:
        df = pd.read_csv(f, **read_kwargs)
        if add_source:
            df["source_file"] = f.stem
        frames.append(df)
    return pd.concat(frames, ignore_index=True)
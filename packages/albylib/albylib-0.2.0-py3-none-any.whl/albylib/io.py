from pathlib import Path
from typing import Union

import pandas as pd


def read_glob(path: Union[str, Path], glob_pattern: str):
    ds = []
    for i in Path(path).glob(glob_pattern):
        d = pd.read_table(i)
        ds.append(d)
    return pd.concat(ds).reset_index(drop=True)

import os

import torch
from torch import tensor

PANDAS_TO_TORCH_TYPES = {"int64": torch.int64, "float64": torch.float32}


def numpy_to_pytorch(data, column_types, target_column, seq_length, device):

    sequence = {
        col: (
            tensor(
                data.query(f"inputCol=='{col}'")[
                    [str(c) for c in range(seq_length, 0, -1)]
                ].values
            )
            .to(column_types[col])
            .to(device)
        )
        for col in column_types.keys()
    }

    if "target" in data:
        target = (
            tensor(data.query(f"inputCol=='{target_column}'")["target"].values)
            .to(column_types[target_column])
            .to(device)
        )
    else:
        target = None

    return (sequence, target)

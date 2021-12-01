import copy
from typing import Sequence, Any

def seq_search(seq: Sequence, key: Any) -> int:

    a = copy.deepcopy(seq)
    a.append(key)

    i = 0

    while True:
        if a[i] == key:
            break
        i += 1
    if i == len(seq):
        return -1
    else:
        return i
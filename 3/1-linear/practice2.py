import copy
from typing import Sequence, Any

def seq_search(list: Sequence, key: Any) -> int:

    a = copy.deepcopy(list)
    a.append(key)

    for i in range(len(a)):
        if a[i] == key and i == len(a):
            return 

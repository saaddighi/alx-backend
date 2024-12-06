#!/usr/bin/env python3


from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple:
    indexs = 0
    indexf = 0
    if page == 1:
        indexs = 0
        indexf = page_size
    else:
        indexs = (page - 1) * page_size
        indexf = page * page_size
    return (indexs, indexf)

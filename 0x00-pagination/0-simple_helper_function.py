#!/usr/bin/env python3


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """a function that eturn a tuple of size two containing a
    start index and an end index corresponding
    to the range of indexes to return in a list
    for those particular pagination parameters"""

    indexa = 0
    indexf = 0
    if page == 1:
        indexa = 0
        indexf = page_size
    else:
        indexa = (page - 1) * page_size
        indexf = page * page_size
    return (indexa, indexf)

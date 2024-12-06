#!/usr/bin/env python3


import csv
import math
from typing import Tuple, List


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        a, b = index_range(page, page_size)
        data = self.dataset()
        try:
            return data[a:b]
        except IndexError:
            return []

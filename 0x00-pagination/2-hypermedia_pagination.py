#!/usr/bin/env python3


import csv
import math
from typing import Tuple, List, Dict
from math import ceil


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
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        data = self.get_page(page, page_size)
        p1 = {'page_size' : len(data)}
        p2 = {'page' : page}
        p3 = {'data' : data}
        try:
            p4 = {"next_page" : page+1}
        except:
            p4 = None
        try:
            p5 = {'prev_page' : page - 1}
        except:
            p5 = None
        p6 = {'total_pages' : len(self.dataset()) / len(data)}
        alldict = {}
        #!/usr/bin/env python3


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
    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        data = self.get_page(page, page_size)
        p1 = {'page_size': len(data)}
        p2 = {'page': page}
        p3 = {'data': data}
        total_data = len(self.dataset())
        total_pages = ceil(total_data / page_size)
        p6 = {'total_pages': total_pages}
        p4 = {"next_page": page + 1 if page < total_pages else None}
        p5 = {'prev_page': page - 1 if page > 1 else None}
        
        alldict = {**p1, **p2, **p3, **p4, **p5, **p6}
        return alldict

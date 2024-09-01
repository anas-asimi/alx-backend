#!/usr/bin/env python3
"""
1-simple_pagination.py
"""
from typing import List
import math
import csv
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """index_range
    Args:
        page (int): _description_
        page_size (int): _description_
    Returns:
        Tuple[int, int]: _description_
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


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
        """get_page
        Args:
            page (int, optional): _description_. Defaults to 1.
            page_size (int, optional): _description_. Defaults to 10.
        Returns:
            List[List]: _description_
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        indexs = index_range(page, page_size)
        return self.dataset()[indexs[0]: indexs[1]]

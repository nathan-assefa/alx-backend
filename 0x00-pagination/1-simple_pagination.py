#!/usr/bin/env python3
''' Finding the starting and ending indexes of pages '''


import csv
import math
from typing import List


def index_range(page, page_size):
    ''' Finding indexes '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_pages = math.ceil(len(dataset) / page_size)

        if page > total_pages:
            return []

        #start_index, end_index = index_range(page, page_size)
        indexes: Tuple = index_range(page, page_size)
        return dataset[indexes[0]:indexes[1]]
        #return dataset[start_index:end_index]

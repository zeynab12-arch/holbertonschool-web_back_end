#!/usr/bin/env python3
'''This module contains a simple pagination implementation.'''
import csv
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''Returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.'''

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing the following key-value pairs:
            page_size: the length of the returned dataset page
            page: the current page number
            data: the dataset page represented as a list of lists
            next_page: the next page number, None if no next page
            prev_page: the previous page number, None if no previous page
            total_pages: the total number of pages in the dataset as an integer
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        total_pgs = len(dataset) // page_size + (len(dataset) % page_size > 0)

        return {
            'page_size': len(dataset[start_index:end_index]),
            'page': page,
            'data': dataset[start_index:end_index],
            'next_page': page + 1 if end_index < len(dataset) else None,
            'prev_page': page - 1 if start_index > 0 else None,
            'total_pages': total_pgs
        }

#!/usr/bin/env python3
'''Simple helper function for pagination'''


def index_range(page: int, page_size: int) -> tuple:
    '''simple helper function'''
    end = page * page_size
    start = (page - 1) * page_size
    return (start, end)

#!/usr/bin/env python3
def index_range(page: int, page_size: int):
    """Pagination helper function"""
    start_index = (page - 1) * page_size
    """Returns start vs end indexes"""
    end_index = page * page_size
    return (start_index, end_index)

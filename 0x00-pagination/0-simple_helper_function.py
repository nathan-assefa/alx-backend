#!/usr/bin/env python3
''' Finding the starting and ending indexes of pages '''


def index_range(page, page_size):
    ''' Finding indexes '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    return start_index, end_index

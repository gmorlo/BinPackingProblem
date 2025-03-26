from typing import Dict, List, Tuple
from bin import Bin

def first_fit(
        bin_capacity: int,
        item_list: List,
):
    bin_list = []
    for item in item_list:
        inserted = False

        for bin in bin_list:
            if bin.add_item(item):
                inserted = True
                break
        
        if not inserted:
            new_bin = Bin(bin_capacity = int(bin_capacity))
            new_bin.add_item(item)
            bin_list.append(new_bin)

    return bin_list

def first_fit_decreasing(
        bin_capacity: int,
        item_list: List,
):
    item_list.sort(reverse=True)

    return first_fit(bin_capacity, item_list)

def full_bin_packing(bin_capacity: int, item_list: List[int]):
    bin_list = []
    item_list.sort(reverse=True)

    while item_list:
        new_bin = Bin(bin_capacity=bin_capacity)
        remaining_items = []

        for item in item_list:
            if not new_bin.add_item(item):
                remaining_items.append(item)

        bin_list.append(new_bin)
        item_list = remaining_items

    return bin_list

def solve_bin_packing(method: str, 
                      bin_capacity: int, 
                      item_list: List) -> list[Bin]:
    if method == 'first_fit':
        return first_fit(bin_capacity, item_list)
    elif method == 'first_fit_decreasing':
        return first_fit_decreasing(bin_capacity, item_list)
    elif method == 'full_bin_packing':
        return full_bin_packing(bin_capacity, item_list)
    else:
        raise ValueError(f'Unknown method: {method}')
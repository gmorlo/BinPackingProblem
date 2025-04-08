from typing import Dict, List, Tuple
from bin import Bin
import random 
import copy

def first_fit(bin_capacity: int, item_list: List[int]):
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

def first_fit_decreasing(bin_capacity: int, item_list: List[int]):
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

def generate_random_solution(bin_capacity: int, item_list: List[int]):
    shuffled_items = item_list[:]
    random.shuffle(shuffled_items)

    return first_fit(bin_capacity, shuffled_items)

def close_neighbor(bin_capacity: int, current_bin_list: List[Bin]):
    bin_list = copy.deepcopy(current_bin_list)
    bin_list = [b for b in bin_list if b.item_list]

    if len(bin_list) < 2:
        return bin_list

    random_bin = random.choice(bin_list)
    random_item = random.choice(random_bin.item_list)
    random_bin.item_list.remove(random_item)
    random_bin.free_bin_capacity += random_item

    if not random_bin.item_list:
        bin_list.remove(random_bin)

    inserted = False
    for bin in bin_list:
        if bin.add_item(random_item):
            inserted = True
            break
    if not inserted:
        new_bin = Bin(bin_capacity=bin_capacity)
        new_bin.add_item(random_item)
        bin_list.append(new_bin)

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
    elif method == 'generate_random_solution':
        return generate_random_solution(bin_capacity, item_list)
    else:
        raise ValueError(f'Unknown method: {method}')
    
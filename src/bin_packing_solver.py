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

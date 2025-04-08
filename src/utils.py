import time
from typing import List, Tuple, Dict
from numpy import array
import random
import numpy as np
import json
from bin import Bin

def load_data_from_file(filepath: str) -> List[int]:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["items"]

def save_results_to_file(filepath, results):

    pass

def generate_items(sequence: array = np.arange(1, 10), number_of_items:int = 100):
    random.seed(42)
    item_list = random.choices(sequence, k=number_of_items)
    
    return item_list


def count_bins(bins: list[Bin]):
    full_bins = 0
    not_full_bins = 0

    for bin in bins:
        if bin.free_bin_capacity == 0:
            full_bins += 1
        else: 
            not_full_bins += 1

    return full_bins, not_full_bins

def display_bins(bins: list[Bin]):
    for i, bin in enumerate(bins):
        print(f"Bin {i + 1}: {bin.item_list}, Free Space: {bin.free_bin_capacity}")

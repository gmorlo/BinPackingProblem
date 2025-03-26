import time
from bin_packing_solver import *
from typing import List, Tuple


class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        if self.start_time is None:
            print("Timer was not started.")
        else:
            elapsed = time.time() - self.start_time
            print(f"Elapsed time: {elapsed:.4f} seconds")
            self.start_time = None

timer = Timer()

def save_results_to_file(filepath, results):

    pass

def count_bins(bins: list[Bin]) -> Tuple[int, int]:
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

def test_solver(method: str, 
                bin_capacity: int, 
                item_list: List,
                display_bins_mode: bool = False,
                count_bins_mode: bool = True) -> list[Bin]:
    timer.start()
    bins = solve_bin_packing(method, bin_capacity, item_list)
    if display_bins_mode:
        display_bins(bins)
    if count_bins_mode:
        full_bins, not_full_bins = count_bins(bins)
        print(f"Full bins: {full_bins}, Not full bins: {not_full_bins}")
    timer.stop()

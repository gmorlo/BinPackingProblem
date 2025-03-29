from bin_packing_solver import *
from typing import List, Tuple
import timer
from plots import plot_bins

timer = timer.Timer()
def objective_function(bins: list[Bin]) -> Tuple[int, int]:
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
                count_bins_mode: bool = True,
                visualize: bool = False) -> list[Bin]:
    timer.start()
    bins = solve_bin_packing(method, bin_capacity, item_list)
    if display_bins_mode:
        display_bins(bins)
    if count_bins_mode:
        full_bins, not_full_bins = objective_function(bins)
        print(f"Full bins: {full_bins}, Not full bins: {not_full_bins}")
    if visualize:
        plot_bins(bins, title=f"Method: {method}, Capacity: {bin_capacity}")

    timer.stop()

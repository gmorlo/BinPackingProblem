from bin_packing_solver import *
from typing import List, Tuple
import timer
from plots import plot_bins
from bin import Bin

timer = timer.Timer()

def evaluate_solution(bins: List[Bin]) -> float:
    total_bins = len(bins)
    total_free_space = sum(bin.free_bin_capacity for bin in bins)

    penalty_factor = 0.05
    score = total_bins + penalty_factor * total_free_space

    return score

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
        full_bins, not_full_bins = count_bins(bins)
        print(f"Full bins: {full_bins}, Not full bins: {not_full_bins}")
    if visualize:
        plot_bins(bins, title=f"Method: {method}, Capacity: {bin_capacity}")

    score = evaluate_solution(bins)
    print(f"Score: {score}")
    timer.stop()

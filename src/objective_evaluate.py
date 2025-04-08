from typing import List, Tuple
from bin import Bin

def evaluate_solution(bins: List[Bin]) -> float:
    total_bins = len(bins)
    total_free_space = sum(bin.free_bin_capacity for bin in bins)

    penalty_factor = 0.1
    score = total_bins + penalty_factor * total_free_space

    return score

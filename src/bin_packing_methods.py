from typing import Dict, List, Tuple
from bin import Bin
import random 
import copy
from objective_evaluate import evaluate_solution


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

def close_random_neighbor(bin_capacity: int, item_list: List[int]):
    all_neighbors = close_neighbors(bin_capacity, item_list)
    return random.choice(all_neighbors)

def close_neighbors(bin_capacity: int, item_list: List[int]):
    initial_solution = first_fit(bin_capacity, item_list)
    all_neighbors = []

    for i, source_bin in enumerate(initial_solution):
        for j, item in enumerate(source_bin.item_list):

                neighbor = copy.deepcopy(initial_solution)
                item_to_move = neighbor[i].item_list.pop(j)
                neighbor[i].free_bin_capacity += item_to_move

                if not neighbor[i].item_list:
                    neighbor.pop(i)
                    if i < len(neighbor):
                        temp_bin_list = neighbor
                    else:
                        temp_bin_list = neighbor[:-1]
                else: 
                    temp_bin_list = neighbor

                inserted = False

                for k, temp_bin in enumerate(temp_bin_list):
                    if k == i:
                        continue
                    if temp_bin.free_bin_capacity >= item_to_move:
                        new_neighbor = copy.deepcopy(temp_bin_list)
                        new_neighbor[k].add_item(item_to_move)
                        all_neighbors.append(new_neighbor)
                        inserted = True


                if not inserted:
                    new_bin = Bin(bin_capacity=bin_capacity)
                    new_bin.add_item(item_to_move)
                    temp_bins = copy.deepcopy(temp_bin_list)

                    temp_bins.append(new_bin)
                    all_neighbors.append(temp_bins)

    return all_neighbors 

def serialize_bins(bins):
    serialized = []

    for bin in bins:
        sorted_items = sorted(bin.item_list)
        bin_tuple = tuple(sorted_items)
        serialized.append(bin_tuple)

    sorted_bins = sorted(serialized)
    return tuple(sorted_bins)

def tabu_search(item_list, bin_capacity, max_iterations=100, tabu_size=None):
    current = generate_random_solution(bin_capacity, item_list)
    global_best = current
    tabu_list = [serialize_bins(current)]

    for i in range(max_iterations):
        neighbors = []
        all_neighbors = close_neighbors(bin_capacity, item_list)

        for n in all_neighbors:
            if serialize_bins(n) not in tabu_list:
                neighbors.append(n)

        if not neighbors:
            break

        best_neighbor = min(neighbors, key=evaluate_solution)
        current = best_neighbor

        tabu_list.append(serialize_bins(current))

        if tabu_size is not None and len(tabu_list) > tabu_size:
            tabu_list = tabu_list[-tabu_size:]#jak rozmiar tabu_list > tabu_size to usuwamy najstarszy element

        if evaluate_solution(current) < evaluate_solution(global_best):
            global_best = current

    print(f"tabu_list: {tabu_list}")
    return global_best

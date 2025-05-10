from bin_packing_methods import simulated_annealing, default_temperature, first_fit, first_fit_decreasing, full_bin_packing, generate_random_solution, close_neighbors, close_random_neighbor, tabu_search
from typing import Dict, List, Tuple
from objective_evaluate import evaluate_solution
from plots import plot_bins
from timer import Timer
from utils import count_bins, display_bins
from bin import Bin

timer = Timer()

def solve_bin_packing(method: str, 
                      bin_capacity: int, 
                      item_list: List,
                      max_iterations=100) -> List[Bin]:
                      
    if method == 'first_fit':
        return first_fit(bin_capacity, item_list)
    
    elif method == 'first_fit_decreasing':
        return first_fit_decreasing(bin_capacity, item_list)
    
    elif method == 'full_bin_packing':
        return full_bin_packing(bin_capacity, item_list)
    
    elif method == 'generate_random_solution':
        return generate_random_solution(bin_capacity, item_list)
    
    elif method == 'close_neighbors':
        return close_neighbors(bin_capacity, item_list)
    
    elif method == 'close_random_neighbor':
        return close_random_neighbor(bin_capacity, item_list)
    
    elif method == 'tabu_search':
        max_iterations = int(input("Enter the number of iterations: "))
        tabu_size = int(input("Enter the size of the tabu list: "))
        result = tabu_search(item_list, bin_capacity, max_iterations=max_iterations, tabu_size=tabu_size)
        return result

    elif method == 'simulated_annealing':
        max_iterations = int(input("Podaj liczbę iteracji: "))
        result, history = simulated_annealing(
            item_list, bin_capacity, max_iterations, T_func=default_temperature
        )
        print("Najlepszy wynik (score):", evaluate_solution(result))
        try:
            import matplotlib.pyplot as plt
            if method == 'simulated_annealing':
                plt.plot(history)
                plt.xlabel("Iteracja")
                plt.ylabel("Score (evaluate_solution)")
                plt.title("Zmiana wartości funkcji celu")
                plt.grid(True)
                plt.show()
        except:
            pass

        return result

    else:
        raise ValueError(f'Unknown method: {method}')
    
def test_solver(method: str, 
                bin_capacity: int, 
                item_list: List,
                display_bins_mode: bool = False,
                count_bins_mode: bool = True,
                max_iterations=100,
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

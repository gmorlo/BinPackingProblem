"""
Generate result images for README: SA and GA convergence curves.
Run from project root: python src/generate_results.py
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bin_packing_methods import simulated_annealing, default_temperature
from genetic_algorithm_bin_packing import genetic_algorithm_bin_packing
import matplotlib
matplotlib.use('Agg')  # non-interactive backend for saving
import matplotlib.pyplot as plt


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    results_dir = os.path.join(base, 'results')
    os.makedirs(results_dir, exist_ok=True)

    # Load items (use larger set for meaningful convergence)
    data_path = os.path.join(base, 'data', 'items.json')
    if os.path.exists(data_path):
        with open(data_path) as f:
            item_list = json.load(f)['items']
    else:
        item_list = [4, 8, 1, 4, 2, 3, 6, 5, 7, 2, 5, 9, 3, 4, 6, 1, 8, 5]
    bin_capacity = 10
    max_iter = 80

    # Simulated Annealing
    _, sa_history = simulated_annealing(
        item_list, bin_capacity, max_iter, T_func=default_temperature
    )
    plt.figure(figsize=(10, 5))
    plt.plot(sa_history, linestyle='-', color='#2ecc71', linewidth=1.5)
    plt.xlabel('Iteration')
    plt.ylabel('Score')
    plt.title('Simulated Annealing — Convergence')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'sa_convergence.png'), dpi=150, bbox_inches='tight')
    plt.close()

    # Genetic Algorithm (one-point crossover)
    _, _, ga_history = genetic_algorithm_bin_packing(
        item_list, bin_capacity,
        population_size=12, max_generations=max_iter,
        mutation_rate=0.2, crossover_method='one_point'
    )
    plt.figure(figsize=(10, 5))
    plt.plot(ga_history, linestyle='-', color='#3498db', linewidth=1.5)
    plt.xlabel('Generation')
    plt.ylabel('Best fitness (score)')
    plt.title('Genetic Algorithm — Convergence')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(os.path.join(results_dir, 'ga_convergence.png'), dpi=150, bbox_inches='tight')
    plt.close()

    print('Saved:', os.path.join(results_dir, 'sa_convergence.png'))
    print('Saved:', os.path.join(results_dir, 'ga_convergence.png'))


if __name__ == '__main__':
    main()

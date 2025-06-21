import random
from typing import List, Callable, Tuple
from bin_packing_genetic_methods import one_point_crossover, uniform_crossover, swap_mutation, mutation_reassign_bin
from bin_packing_methods import generate_random_solution
from objective_evaluate import evaluate_solution

def genetic_algorithm_bin_packing(
    item_list: List[int],
    bin_capacity: int,
    population_size: int = 10,
    max_generations: int = 100,
    mutation_rate: float = 0.2,
    patience: int = 10,
    crossover_method: str = 'one_point',
    mutation_methods: List[Callable[[List[int]], List[int]]] = [swap_mutation, mutation_reassign_bin],
) -> Tuple[List[int], float, List[float]]:
    
    # tworzy początkową populacje
    population = []
    for _ in range(population_size):
        individual = random.sample(item_list, len(item_list))
        population.append(individual)

    best_scores = []
    best_solution = None
    best_fitness = float('inf')
    stagnation_counter = 0
    generation = 0
    max_bin_index = len(item_list)

    # Główna pętla algorytmu genetycznego
    while generation < max_generations:
        fitness_values = []

        # Ocena populacji
        for ind in population:
            solution = generate_random_solution(bin_capacity, ind)
            fitness = evaluate_solution(solution)
            fitness_values.append(fitness)
        sorted_population = []

        # Sortowanie populacji według wartości fitness
        for _, ind in sorted(zip(fitness_values, population), key=lambda x: x[0]):
            sorted_population.append(ind)

        # Selekcja
        # Losowo przetasowuje posortowaną populację, gwarantując, że każdy osobnik pojawi się dokładnie raz w nowej liście
        selected = random.sample(sorted_population, len(population))

        # Krzyżowanie wybraną metodą
        offspring = []
        for i in range(0, len(selected), 2):
            p1 = selected[i]
            p2 = selected[(i + 1) % len(selected)]
            child = one_point_crossover(p1, p2) if crossover_method == 'one_point' else uniform_crossover(p1, p2)
            offspring.append(child)

        # Wybiera losowo metodę mutacji i stosuje ją do każdego potomka
        mutated = []
        for child in offspring:
            if random.random() < mutation_rate:
                mutation_fn = random.choice(mutation_methods)
                if mutation_fn == mutation_reassign_bin:
                    mutant = mutation_fn(child, max_bin=max_bin_index)
                else:
                    mutant = mutation_fn(child)
                mutated.append(mutant)
            else:
                mutated.append(child)

        population = mutated

        # Ocena nowej populacji
        fitness_values = []
        for ind in population:
            solution = generate_random_solution(bin_capacity, ind)
            fitness = evaluate_solution(solution)
            fitness_values.append(fitness)
            
        current_best_score = min(fitness_values)
        best_scores.append(current_best_score)

        if current_best_score < best_fitness: # sprawdza, czy wynik sie poprawił
            best_fitness = current_best_score
            best_solution = population[fitness_values.index(current_best_score)]
            stagnation_counter = 0
        else: # jeśli nie, zwiększa licznik stagnacji   
            stagnation_counter += 1

        if stagnation_counter >= patience:
            break

        generation += 1

    return best_solution, best_fitness, best_scores

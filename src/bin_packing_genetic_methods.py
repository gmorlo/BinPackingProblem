from typing import Dict, List, Tuple
from bin import Bin
import random 
import math
import copy
from objective_evaluate import evaluate_solution

def apply_crossover(population, method='one_point'):
    offspring = []
    for i in range(0, len(population), 2):
        p1 = population[i]
        p2 = population[(i+1) % len(population)]
        if method == 'one_point':
            child = one_point_crossover(p1, p2)
        elif method == 'uniform':
            child = uniform_crossover(p1, p2)
        offspring.append(child)
    return offspring

def uniform_crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    child = []
    used = set()

    for i in range(len(parent1)):
        if random.random() < 0.5 and parent1[i] not in used:
            child.append(parent1[i])
            used.add(parent1[i])
        elif parent2[i] not in used:
            child.append(parent2[i])
            used.add(parent2[i])

    for item in parent1:
        if item not in used:
            child.append(item)

    return child

def one_point_crossover(parent1: List[int], parent2: List[int]) -> List[int]:
    point = random.randint(1, len(parent1) - 2)
    head = parent1[:point]
    tail = [item for item in parent2 if item not in head]
    return head + tail

def swap_mutation(individual: List[int]) -> List[int]:
    mutant = individual[:]
    i, j = random.sample(range(len(mutant)), 2)
    mutant[i], mutant[j] = mutant[j], mutant[i]
    return mutant

# Mutacja nie zakceptowana, ponieważ niepotrzebne jest usuwanie bitów z rozwiązania
def mutation_remove_bit(solution, mutation_rate=0.05) -> List[int]: 
    mutated_solution = [
        bit for bit in solution if random.random() > mutation_rate
    ]
    return mutated_solution

def mutation_reassign_bin(individual: List[int], max_bin: int) -> List[int]:
    mutant = individual[:]
    index = random.randint(0, len(mutant) - 1)         # losowy przedmiot
    new_bin = random.randint(0, max_bin - 1)           # losujemy nowy bin
    while new_bin == mutant[index]:                    
        new_bin = random.randint(0, max_bin - 1)
    mutant[index] = new_bin
    return mutant
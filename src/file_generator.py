import os
import json
import random

def generate_large_json_file(filename: str, num_items: int, min_val: int = 1, max_val: int = 100):
    os.makedirs(os.path.dirname(filename), exist_ok=True)  # tworzy folder jeśli nie istnieje

    data = {
        "items": [random.randint(min_val, max_val) for _ in range(num_items)]
    }

    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

# Przykład użycia:
# generate_large_json_file(
#     "C:/Users/gabry/Desktop/School_projects/MHE/bin_packing_project/data/big_items.json", 
#     num_items=10000)

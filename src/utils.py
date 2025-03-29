import time
from bin_packing_solver import *
from typing import List, Tuple
import json

def load_data_from_file(filepath: str) -> List[int]:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["items"]

def save_results_to_file(filepath, results):

    pass
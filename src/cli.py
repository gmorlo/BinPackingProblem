import argparse
from typing import Dict, List
from utils import test_solver
import json

def parse_command_line_arguments() -> Dict:
    parser = argparse.ArgumentParser(description="Simple CLI for bin packing problem")

    parser.add_argument(
        "method", 
        type=str, 
        help="The bin packing algorithm to use. Options: 'first_fit', 'first_fit_decreasing', 'full_bin_packing', 'best_fit', 'simulated_annealing'."
        )
    parser.add_argument(
        "bin_capacity", 
        type=int, 
        help="The maximum capacity of each bin (integer)."
        )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--items",
        type=int,
        nargs='+',
        help="List of item sizes (e.g., 2 5 4 7 1 3 8)"
    )
    group.add_argument(
        "--file",
        type=str,
        help="Path to JSON file containing item list"
    )
    parser.add_argument(
        "--display", 
        action="store_true",
        help="Display bin contents"
    )
    parser.add_argument(
        "--count", 
        action="store_true",
        help="Count full vs. not full bins"
    )
    args = parser.parse_args()
    return vars(args)

def load_data_from_file(filepath: str) -> List[int]:
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["items"]

def main():

    args = parse_command_line_arguments()

    if args["items"]:
        item_list = args["items"]
    elif args["file"]:
        item_list = load_data_from_file(args["file"])
    else:
        raise ValueError("No input data provided.")

    test_solver(
        method=args["method"],
        bin_capacity=args["bin_capacity"],
        item_list=item_list,
        display_bins_mode=args["display"],
        count_bins_mode=args["count"]
    )

if __name__ == "__main__":
    main()
import argparse
from typing import Dict, List, Tuple
from bin_packing_solver import solve_bin_packing


def parse_command_line_arguments() -> Dict:
    parser = argparse.ArgumentParser(description="Simple CLI for bin packing problem")

    parser.add_argument(
        "method", 
        type=str, 
        help="The bin packing algorithm to use. Options: 'first_fit', 'best_fit', 'simulated_annealing'."
        )
    parser.add_argument(
        "bin_capacity", 
        type=int, 
        help="The maximum capacity of each bin (integer)."
        )
    parser.add_argument(
        "item_list", 
        type=int, 
        nargs='+', 
        help="""A space-separated list of item sizes to be packed (e.g., "2 5 4 7 1 3 8")."""
        )

    args = parser.parse_args()
    return vars(args)

def load_data_from_file(filepath) -> Tuple[int, List[int]]:
    #TODO Implement file loading logic
    pass

def main():
    args = parse_command_line_arguments()

    result = solve_bin_packing(args['method'], args['bin_capacity'], args['item_list'])

    for i, bin in enumerate(result):
        print(f"Bin {i + 1}: {bin.item_list}, Free Space: {bin.free_bin_capacity}")


if __name__ == "__main__":
    main()
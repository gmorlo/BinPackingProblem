class Bin:
    def __init__(self, bin_capacity: int):
        self.bin_capacity = bin_capacity
        self.free_bin_capacity = bin_capacity
        self.item_list = []

    def can_fit(self, item: int) -> bool:
        return self.free_bin_capacity >= item
    
    def add_item(self, item: int):
        if self.can_fit(item):
            self.item_list.append(item)
            self.free_bin_capacity -= item
            return True
        return False


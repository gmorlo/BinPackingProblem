import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()
    
    def stop(self):
        if self.start_time is None:
            print("Timer was not started.")
        else:
            elapsed = time.time() - self.start_time
            print(f"Elapsed time: {elapsed:.4f} seconds")
            self.start_time = None
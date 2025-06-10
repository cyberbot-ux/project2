import time

class Timer:  
    def __init__(self):
        self.start_time = time.time()

    def elapsed(self):
        return time.time() - self.start_time

    def reset(self):
        self.start_time = time.time()

    def sleep(self, seconds):
        time.sleep(seconds)

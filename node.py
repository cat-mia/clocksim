
import random

class Node:
    def __init__(self,index,init_t):
        self.index = index
        self.time = init_t
        
    def time_clock(self):
        max_err_rate = 1e-5
        err_rate = random.uniform(-max_err_rate,max_err_rate)
        self.time += 1 + err_rate # clock tick once
        
    def check_time(self,update_interval):
        return self.time / update_interval >=1 and self.time % update_interval <= 1e-5

    def get_time(self):
        return self.time

    def set_time(self,time):
        self.time = time

    
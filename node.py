from utils import *
import random
import math

class Node:
    def __init__(self,index,init_t):
        self.index = index
        self.time = init_t
        self.last_sync_time = init_t
        self.max_err_rate = 0.3
        
    def time_clock(self):
        err_rate = random.uniform(-self.max_err_rate,self.max_err_rate)
        self.time += 1 + err_rate # clock ticks once
        
    def check_time(self,update_interval):
        return approximate_equals(self.time , self.last_sync_time + update_interval, self.max_err_rate, update_interval)

    def get_time(self):
        return self.time

    def set_time(self,time):
        self.time = time
        self.last_sync_time = time

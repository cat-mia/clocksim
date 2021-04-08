from node import *
from sync import *
from utils import *
import numpy as np


node_num = 10
init_t =0
update_interval = 2 # time = t0 + i*R


nodes = []

for index in range(node_num):
    nodes.append(Node(index, init_t))


# clock ticks 1000 times
for i in range(10):
    times = [-1] * node_num
    is_sync = [False] * node_num
    for node in nodes:
        node.time_clock() # increase time by 1 with error
        if node.check_time(update_interval):
            times[node.index] = broadcast(node)
            is_sync[node.index] = True
    for node in nodes:
        if is_sync[node.index] and -1 not in times:
            other_times = times[:node.index]+times[(node.index+1):]
            sync_clock(node,other_times)
    
    node_t = []
    if (i+1) % update_interval == 0:
        print("\nafter sync***************************")
    else:
        print("\nbefore sync**************************")
    print("clock ticks ",i+1," times, nodes info:")
    for node in nodes:
        print(node.index,"th node's time: ",node.time,"  ")
        node_t.append(node.time)
    print("Variance: ",np.var(node_t))
    print("Range: ",np.ptp(node_t))



            



    
    

from node import *
from sync import *
from utils import *


node_num = 100
init_t =0
update_interval = 10


nodes = []

for index in range(node_num):
    nodes.append(Node(index, init_t))


# clock ticks 1000 times

times = [-1] * node_num
is_sync = [False] * node_num
update_count = [0] * node_num

# clock ticks 1000 times
for i in range(1000):
    for node in nodes:
        node.time_clock()
        if node.check_time(update_interval):
            update_count[node.index] += 1
            times[node.index] = broadcast(node)
            is_sync[node.index] = True   
    for node in nodes:
        if is_sync[node.index] and all_equals(update_count,target = update_count[node.index]):
            other_times = times[0:node.index]+ times[node.index:]
            sync_clock(node,other_times)
    
    if i % 100 == 0:
        print("clock ticks ",i," times, nodes info:\n")
        for node in nodes:
            print(node.index,"th node's time: ",node.time,"  ")


            



    
    

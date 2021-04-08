from node import *

# each node broadcasts its time
# time = t0 + i*R
def broadcast(Node):
    node_time = Node.get_time()
    return node_time

def sync_clock(Node, *other_times):
    new_time = sum(other_times) / len(other_times)
    Node.set_time(new_time)

# remove m largest and m smallest values
def sync_clock_improve(Node, *other_times, m):
    other_times.sort()
    other_times = other_times[:-m]
    other_times = other_times[m:]
    new_time = sum(other_times) / len(other_times)
    Node.set_time(new_time)
    #print(Node.index+"th node's time: "+ new_time +"\n")
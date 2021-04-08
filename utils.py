
def list_equals(list , target):
    for item in list:
        if item != target:
            return False
    return True

def approximate_equals(v1, v2 , err_rate, update_interval):
    return abs(v1 - v2) <= err_rate * update_interval # 2 is update interval
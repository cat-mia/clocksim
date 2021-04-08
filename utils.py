
def all_equals(*list , target):
    for item in list:
        if item != target:
            return False
    return True
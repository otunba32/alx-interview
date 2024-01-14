#!/usr/bin/python3
"""
script that determines if all the boxes can be opened
"""

def canUnlockAll(boxes):
    """
    A function that returns True if all boxes can be opened, else return False
    """
    if type(boxes) is not list:
        return False
    if len(boxes) == 0:
        return False
    if len(boxes) == 1:
        return True

    free_keys = [0] #first key is free
    used_keys = [] #no keys used yet

    for key in free_keys:
        for box in boxes[key]:
            if box not in free_keys:
                if box not in used_keys:
                    if box < len(boxes):
                        free_keys.append(box)
        used_keys.append(key)

    if len(free_keys) == len(boxes):
        return True
    else:
        return False

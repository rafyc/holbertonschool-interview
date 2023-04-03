#!/usr/bin/python3

'''
 method that determines if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    count = len(boxes)
    v = []
    r = range(1, count)
    for i in range(count):
        for j in boxes[i]:
            if j not in v:
                if j != i and j is not None:
                    v.append(j)
                    if 0 in v:
                        v.remove(0)
                        v.sort()
                else:
                    continue
    k = 1
    while k < count - 1:
        if k not in v:
            return False
        else:
            k += 1
    return True

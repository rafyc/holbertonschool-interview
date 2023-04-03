#!/usr/bin/python3

def canUnlockAll(boxes):
    count = len(boxes)
    v = []
    r = range(1, count)
    for i in range(count):
        for j in boxes[i]:
            if j != i:
                if j not in v:
                    v.append(j)
                    if 0 in v:
                        v.remove(0)
                        v.sort()
            else:
                return False
    k = 1
    while k < count - 1:
        k+= 1
    if k not in v:
        return False
    else:
        return True

canUnlockAll(boxes)

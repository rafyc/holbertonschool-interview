#!/usr/bin/python3
'''
 method that determines if all the boxes can be opened.
'''


boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]

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
                print('false')
                return False
    k = 1
    while k < count - 1:
        k += 1
    if k not in v:
        print('false')
        return False
    else:
        print('true')
        return True

canUnlockAll(boxes)

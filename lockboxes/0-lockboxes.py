#!/usr/bin/python3

'''
 method that determines if all the boxes can be opened.
'''

boxes = [[0]]
def canUnlockAll(boxes):
    count = len(boxes)
    v = []
    r = range(1, count)
    for i in range(count):
        for j in boxes[i]:
            if j not in v:
                if j != i:
                    v.append(j)
                else:
                    continue
    print(v)
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

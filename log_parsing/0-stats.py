#!/usr/bin/python3


"""Defines a script that reads stdin line by line and computes metrics"""
from sys import stdin


countStatus = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

totalSize = 0
countLine = 0


def printStats():
    print('File size: {}'.format(totalSize))
    for key in countStatus.key():
        if countStatus[key] != 0 :
            print('{}:{}'.format(ele, countStatus[ele]))


if __name__ == "__main__":

    try:
        for line in stdin:
            countLine += 1

            try:
                parse = line.split()
                totalSize = int(parse[-1])
                status = int(parse[-2])
                countStatus[status] += 1

            except ValueError:
                pass

        if countLine == 10:
            printStats()

    except KeyboardInterrupt:
        printStats()
        exit(1)

    printStats()

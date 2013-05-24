#!/usr/bin/env python
import fileinput

# A slower version of main()
# Original implementation resulted in a O(n^2) algorithm
def slow():
    lineA = []
    lineB = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            lineA = map(int, line.split())
        else:
            lineB = map(int, line.split())

    for numA in lineA:
        i = 0;
        lineB[i] = numA
        while i+1 < len(lineB):
            if lineB[i] > lineB[i+1]:
                lineB[i], lineB[i+1] = lineB[i+1], lineB[i]
                i += 1
            else:
                break

    print lineB

# Use binary search to determine the insertion point for the new number
def insertPoint(sortedList, begin, end, num):
    while end > begin:
        middle = (begin+end)/2
        if num < sortedList[middle]:
            end = middle
        else:
            begin = middle
        
        if end - begin == 1:
            return begin

    return end

# A more time efficent algorithm to solve the problem
# used regul's second post as inspiration to create a O(nlogn) implementation
def main():
    lineA = []
    lineB = []
    for line in fileinput.input():
        if fileinput.isfirstline():
            lineA = map(int, line.split())
        else:
            lineB = map(int, line.split())
    
    for numA in lineA:
        # determine where in lineB to insert numA
        index = insertPoint(lineB, 0, len(lineB)-1, numA)
        # use zero-value buffers at front of lineB to hold numA 
        lineB[0] = numA
        while index >= 0:
            lineB[0], lineB[index] = lineB[index], lineB[0]
            index -= 1

    print lineB


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import fileinput
# itemgetter allows sorting of a list of tuples by specified indices
from operator import itemgetter

def main():
    edges = []
    for line in fileinput.input():
        if not fileinput.isfirstline():
            name, u, v = line.split()
            edges.append((name,u,v))

    edges = sorted(edges, key=itemgetter(1,2))

    for edge in edges:
        print edge[0]

if __name__ == "__main__":
    main()

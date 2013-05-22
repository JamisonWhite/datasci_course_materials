#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce
from collections import defaultdict

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    mr.emit_intermediate("dna", record[1][:-10])


# Part 3
def reducer(key, list_of_values):
    for x in set(list_of_values):
        mr.emit(x)


# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data/dna.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




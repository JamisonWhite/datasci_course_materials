#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce
from collections import defaultdict

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, personB)
    mr.emit_intermediate(personB, personA)


# Part 3
def reducer(key, list_of_values):
    seen = set()
    seen_twice = set()
    for x in list_of_values:
        if x in seen:
            seen_twice.add(x)
        else:
            seen.add(x)

    for x in (seen - seen_twice):
        mr.emit((key, x))


# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data/friends.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




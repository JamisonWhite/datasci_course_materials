#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    # 0: personA
    # 1: personB; object of friendship
    mr.emit_intermediate(record[0], 1)


# Part 3
def reducer(key, values):
    #key: PersonA
    #values: 1 for each friendship
    mr.emit((key, sum(values)))


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




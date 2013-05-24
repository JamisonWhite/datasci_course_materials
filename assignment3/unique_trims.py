#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce


# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    # 1: key
    # 2: DNA sequence
    mr.emit_intermediate("dna", record[1][:-10])


# Part 3
def reducer(key, values):
    # key: "dna"
    # values: trimmed sequence
    [mr.emit(x) for x in set(values)]


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




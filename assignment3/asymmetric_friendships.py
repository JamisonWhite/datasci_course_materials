#problem 3.1
__author__ = 'jamie'



import sys
import MapReduce
from collections import defaultdict

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, (value, 1))
    mr.emit_intermediate(value, (key, 0))
    #mr.emit_intermediate(key, value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of columns
    #mr.emit((key, list_of_values))
    d = defaultdict(list)
    for l in list_of_values:
        d[l[0]] = l[1]
    mr.emit(d)
# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data\\friends.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




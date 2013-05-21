#problem 3.1
__author__ = 'jamie'



import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, key)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in list_of_values:
      total.append(v)
    mr.emit((key, total))

# Part 4

# Part 4
if len(sys.argv) >= 2:
    data = open(sys.argv[1])
else:
    data = "data/books.json"

with open(data, 'r') as f:
    mr.execute(f, mapper, reducer)

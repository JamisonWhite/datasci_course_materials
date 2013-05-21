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
    mr.emit_intermediate(value, record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of columns
    total = {key:[]}
    for v in list_of_values:
      total[key].append(v)
    mr.emit((key, total))


# Part 4
if len(sys.argv) >= 2:
    data = open(sys.argv[1])
else:
    data = "data/records.json"

with open(data, 'r') as f:
    mr.execute(f, mapper, reducer)



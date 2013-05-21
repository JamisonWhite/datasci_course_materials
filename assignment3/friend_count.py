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
    mr.emit_intermediate(key, 1)
    # mr.emit_intermediate(value, 1)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of columns
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))


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




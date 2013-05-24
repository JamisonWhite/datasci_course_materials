#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):
    # 0, key: document identifier
    # 1, value: document contents
    key = record[0]
    value = record[1]
    for w in value.split():
        mr.emit_intermediate(w, key)


# Part 3
def reducer(key, list_of_values):
    # key: word
    # list_of_values: books
    books = list(set(v for v in list_of_values))
    mr.emit((key, books))


# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data/books.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()
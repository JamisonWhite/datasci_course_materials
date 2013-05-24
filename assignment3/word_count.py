#problem 3.1
__author__ = 'jamie'



import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # 0: document identifier
    # 1: document contents
    words = record[1].split()
    for w in words:
      mr.emit_intermediate(w, 1)

# Part 3
def reducer(key, values):
    # key: word
    # values: 1 for each occurrence of word
    mr.emit((key, sum(values)))

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


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
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of columns
    orders = []
    items = []
    for l in list_of_values:
        if l[0] == 'order':
            orders.append(l)
        else:
            items.append(l)

    for o in orders:
        for i in items:
            x = o + i
            mr.emit(x)


# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data\\records.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




#problem 3.1
__author__ = 'jamie'



import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # 1: join key
    # 0..n: attributes
    mr.emit_intermediate(record[1], record)

# Part 3
def reducer(key, values):
    # key: join key
    # values: 0..n attributes
    orders = []
    items = []
    for l in values:
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
        data = "data/records.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




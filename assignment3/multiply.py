#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce
from collections import defaultdict

# Part 1
mr = MapReduce.MapReduce()


# Part 2
def mapper(record):

    matrix = record[0]
    x = record[1]
    y = record[2]
    value = record[3]

    if matrix == 'a':
        mr.emit_intermediate('arow{0}'.format(x), ('a', x, y, value))
        mr.emit_intermediate('acol{0}'.format(y), ('a', x, y, value))

        mr.emit_intermediate('brow{0}'.format(y), ('a', x, y, value))
        mr.emit_intermediate('bcol{0}'.format(x), ('a', x, y, value))

    if matrix == 'b':
        mr.emit_intermediate('arow{0}'.format(y), ('b', x, y, value))
        mr.emit_intermediate('acol{0}'.format(x), ('b', x, y, value))

        mr.emit_intermediate('brow{0}'.format(x), ('b', x, y, value))
        mr.emit_intermediate('bcol{0}'.format(y), ('b', x, y, value))


    # for i in range(x):
    #     for j in range(y):
    #         k = '{0},{1}'.format(i, j)
    #         p = (j if matrix=='a' else i)
    #         v = [matrix, (i,j), value]
    #         mr.emit_intermediate(k, v)

# select sum(a.value * b.value)
# from a
# join b on a.row_num = b.col_num or a.col_num = b.row_num
# where a.row_num = 2 and b.col_num = 3
# group by a.row_num, b.col_num;

# Part 3
def reducer(key, list_of_values):
    mr.emit((key, list_of_values))


# Part 4
def main():
    if len(sys.argv) >= 2:
        data = open(sys.argv[1])
    else:
        data = "data/matrix.json"

    with open(data, 'r') as f:
        mr.execute(f, mapper, reducer)


if __name__ == '__main__':
    main()




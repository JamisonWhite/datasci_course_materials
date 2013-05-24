#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # 0: matrix name
    # 1: rov
    # 2: column
    # 3: value

    #Relation M(I, J, V) with tuples (m, i, j, v=m_ij)
    if record[0] == 'a':
        M = record[0]
        i = record[1]
        j = record[2]
        v = record[3]
        for k in range(5):
            mr.emit_intermediate((i, k), [M, j, v])

    #Relation N(J, K, W) with tuples (n, j, k, w=n_jk)
    if record[0] == 'b':
        N = record[0]
        j = record[1]
        k = record[2]
        w = record[3]
        for i in range(5):
            mr.emit_intermediate((i, k), [N, j, w])


# Part 3
def reducer(key, values):
    # key: (i, k)
    # values: [matrix name, j, value]
    # goal find common j values for both matrices and sum the products of the values
    #mr.emit((key, values))
    M = {v[1]:v[2] for v in values if v[0] == 'a'}
    N = {v[1]:v[2] for v in values if v[0] == 'b'}
    J = set.intersection(set(M.keys()), set(N.keys()))
    total = sum([M[j] * N[j] for j in J])
    mr.emit((key[0], key[1], total))


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




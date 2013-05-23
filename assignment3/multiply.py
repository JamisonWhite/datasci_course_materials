#problem 3.1
__author__ = 'jamie'

import sys
import MapReduce
import json

# Part 1
mr = MapReduce.MapReduce()
mr2 = MapReduce.MapReduce()


# Part 2
def mapper(record):

    #Relation M(I, J, V) with tuples (m, i, j, m_ij)
    #Relation N(J, K, W) with tuples (n, j, k, n_jk)

    k = 4

    if record[0] == 'a':
        M = record[0]
        i = record[1]
        j = record[2]
        v = record[3]
        for k in range(5):
            mr.emit_intermediate((i, k), [M, j, v])


    if record[0] == 'b':
        N = record[0]
        j = record[1]
        k = record[2]
        w = record[3]
        for i in range(5):
            mr.emit_intermediate((i, k), [N, j, w])


# Part 3
def reducer(key, list_of_values):
    M = {}
    N = {}
    for v in list_of_values:
        if v[0] == 'a':
            M[v[1]] = v[2]
        else:
            N[v[1]] = v[2]

    total = 0
    J = set.intersection(set(M.keys()), set(N.keys()))
    for j in J:
        total += M[j] * N[j]
    result = list(key)
    result.append(total)
    mr.emit(result)



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




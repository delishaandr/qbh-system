import os
import libfmp.c3
import libfmp.c7
import numpy as np

def songRanking(hum, midi):
    iter = []

    for i in range (12):
        costs = []
        for j in range (len(midi)):
            costs.append(subsequenceDTW(hum, midi[j]))
        iter.append(costs)
        hum = transposeHum(hum)
    
    tr_iter = np.array(iter).T.tolist()
    min_iter = getMinIter(tr_iter)
    min_iter.sort(key=lambda x: x[1])
    rank_iter = np.array(min_iter).T.tolist()

    return rank_iter[0]

def subsequenceDTW(arr1, arr2):
    cost_matrix = libfmp.c3.compute_cost_matrix(arr1, arr2, metric='euclidean')
    acc_cost_matrix = libfmp.c7.compute_accumulated_cost_matrix_subsequence_dtw_21(cost_matrix)
    opt_path = libfmp.c7.compute_optimal_warping_path_subsequence_dtw_21(acc_cost_matrix)

    a_ast = opt_path[0,1]
    b_ast = opt_path[-1,1]

    # print('Accumulated cost matrix D =', acc_cost_matrix, sep='\n')
    # print('Optimal warping path:', opt_path.tolist())
    # print('a* =', a_ast)
    # print('b* =', b_ast)
    # print('Sequence X =', arr1)
    # print('Optimal subsequence Y(a*:b*) =', arr2[a_ast:b_ast+1])
    # print('Accumulated cost D[N, b*] =', acc_cost_matrix[-1, b_ast])

    return acc_cost_matrix[-1, b_ast]

def getMinIter(iter):
    min = []
    for i in range(len(iter)):
        s = iter[i]
        s.sort()
        min.append([i, s[0]])

    return min

def transposeHum(hum):
    tr = []
    for h in hum:
        if (h == 11):
            tr.append(0)
        else:
            tr.append(h+1)
    return tr

def meanReciprocalRank(ranks, labels):
    Q = len(labels)
    sigma = 0

    for i in range (Q):
        rank = ranks[i].index(labels[i]) + 1
        sigma += 1 / rank
    
    return 1 / Q * sigma
import os
import libfmp.c3
import libfmp.c7
import numpy as np

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

def meanReciprocalRank(ranks, labels):
    Q = len(labels)
    sigma = 0

    for i in range (Q):
        rank = ranks[i].index(labels[i]) + 1
        sigma += 1 / rank
    
    return 1 / Q * sigma
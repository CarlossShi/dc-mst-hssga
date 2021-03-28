from hssga import *
import matplotlib.pyplot as plt


if __name__ == "__main__":
    adj_mat = [[0, 224, 224, 361, 671, 300, 539, 800, 943],
               [224, 0, 200, 200, 447, 283, 400, 728, 762],
               [224, 200, 0, 400, 566, 447, 600, 922, 949],
               [361, 200, 400, 0, 400, 200, 200, 539, 583],
               [671, 447, 566, 400, 0, 600, 447, 781, 510],
               [300, 283, 447, 200, 600, 0, 283, 500, 707],
               [539, 400, 600, 200, 447, 283, 0, 361, 424],
               [800, 728, 922, 539, 781, 500, 361, 0, 500],
               [943, 762, 949, 583, 510, 707, 424, 500, 0]]  # BB solution; 2256

    max_degree = 3
    n_pop = 300
    n_iter = 1000
    P_b = 0.9
    P_c = 0.5
    alpha = 0.1
    PR_pop = 500
    rs = 0.05

    T_gb, data = hssga(adj_mat, max_degree, n_pop, n_iter, P_c, P_b, alpha, PR_pop, rs)
    T_gb.print()

    # visualization
    plt.plot(range(n_iter), data['pop_avg_cost'], color='blue', alpha=0.6, label='mean of population')
    plt.plot(range(n_iter), data['best_cost'], color='red', alpha=0.6, label='best so far')
    plt.title('')
    plt.xlabel('no. of generation')
    plt.ylabel('cost of spanning tree')
    plt.legend(loc='upper right')
    plt.show()

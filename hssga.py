import random
import math
import numpy as np


def is_tree(_n, _edges):
    # https://www.geeksforgeeks.org/check-given-graph-tree/
    def is_cyclic_util(v, _visited, parent):
        _visited[v] = True  # Mark current node as visited
        for e in [_ for _ in _edges if v in _]:  # Recur for all the vertices adjacent for this vertex
            _i = e[0] if e[1] == v else e[1]
            if not _visited[_i]:  # If an adjacent is not visited, then recur for that adjacent
                if is_cyclic_util(_i, _visited, v):
                    return True
            elif _i != parent:  # If an adjacent is visited and not parent of current vertex, then there is a cycle.
                return True
        return False

    visited = [False] * _n
    if is_cyclic_util(0, visited, -1):  # vertex idx begin by 0
        return False
    for _ in range(_n):
        if not visited[_]:
            return False
    return True


class SpanningTree:
    def __init__(self, _edges, _degree, _cost):
        self.edges = _edges
        self.degree = _degree
        self.cost = _cost

    def print(self):
        print('edges:', self.edges)
        print('degree:', self.degree)
        print('cost:', self.cost)
        print('is tree:', is_tree(len(self.degree), self.edges))


def prim_rst(_n, _adj_mat, _V, _E, _max_degree):
    T = set()
    s = random.choice(tuple(_V))
    C = {s}  # set of connected nodes
    A = {_ for _ in _E if s in _}  # eligible edges, e.g. [(1,2), (2,3), ...]
    _degree = [0] * _n
    cost = 0
    while C != _V:
        uv = random.choice([_ for _ in A if (_[0] in C or _[1] in C)])  # choose an edge (u, v) \in A, u \in C at random
        A.remove(uv)
        u, v = (uv[0], uv[1]) if uv[0] in C else (uv[1], uv[0])  # make sure u \in C
        if v not in C and _degree[u] < _max_degree and _degree[v] < _max_degree:  # connect v to the partial tree
            T.add(uv)
            _degree[u] += 1
            _degree[v] += 1
            cost += _adj_mat[u][v]
            C.add(v)
            A = A.union({_ for _ in _E
                         if _[0] == v and _[1] not in C
                         or _[1] == v and _[0] not in C})
    return SpanningTree(T, _degree, cost)


def x_over(_n, _adj_mat, _V, _E, p_1, p_2, _max_degree):
    T = set()
    degree = [0] * _n
    cost = 0
    mark = [0] * _n
    v_1 = random.choice(tuple(_V))
    S = {v_1}  # set of connected nodes
    mark[v_1] = 1
    Pb_p1p2 = 1 / p_1.cost / (1 / p_1.cost + 1 / p_2.cost)
    u_01 = random.random()
    if u_01 < Pb_p1p2:
        e_v1v2 = random.choice([_ for _ in p_1.edges if v_1 in _])
    else:
        e_v1v2 = random.choice([_ for _ in p_2.edges if v_1 in _])
    v_2 = e_v1v2[0] if e_v1v2[1] == v_1 else e_v1v2[1]
    mark[v_2] = 1
    S.add(v_2)
    T.add(e_v1v2)
    degree[v_1] += 1
    degree[v_2] += 1
    cost += _adj_mat[v_1][v_2]
    while _V - S != set():
        u_01 = random.random()
        if u_01 < Pb_p1p2:
            try:  # search in p_1
                e_ij = random.choice([_ for _ in p_1.edges
                                      if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                      or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree])
            except IndexError:  # if the search in p_1 is not successful
                try:  # search in p_2
                    e_ij = random.choice([_ for _ in p_2.edges
                                          if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                          or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree])
                except IndexError:  # if the searches in p_1 and p_2 are not successful
                    e_ij = next(_ for _ in [e for e in _E if e not in T]  # E is a list while T is a set
                                if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree)
                    i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                    mark[j] = 1
                    S.add(j)
                    T.add(e_ij)
                    degree[i] += 1
                    degree[j] += 1
                    cost += _adj_mat[i][j]
                else:  # if the search in p_2 is successful
                    i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                    mark[j] = 1
                    S.add(j)
                    T.add(e_ij)
                    degree[i] += 1
                    degree[j] += 1
                    cost += _adj_mat[i][j]
            else:  # if the search in p_1 is successful
                i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                mark[j] = 1
                S.add(j)
                T.add(e_ij)
                degree[i] += 1
                degree[j] += 1
                cost += _adj_mat[i][j]
        else:
            try:  # search in p_2
                e_ij = random.choice([_ for _ in p_2.edges
                                      if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                      or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree])
            except IndexError:  # if the search in p_2 is not successful
                try:  # search in p_1
                    e_ij = random.choice([_ for _ in p_1.edges
                                          if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                          or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree])
                except IndexError:  # if the searches in p_2 and p_1 are not successful
                    e_ij = next(_ for _ in [e for e in _E if e not in T]
                                if _[0] in S and _[1] in _V - S and degree[_[0]] < _max_degree
                                or _[1] in S and _[0] in _V - S and degree[_[1]] < _max_degree)
                    i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                    mark[j] = 1
                    S.add(j)
                    T.add(e_ij)
                    degree[i] += 1
                    degree[j] += 1
                    cost += _adj_mat[i][j]
                else:  # if the search in p_2 is successful
                    i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                    mark[j] = 1
                    S.add(j)
                    T.add(e_ij)
                    degree[i] += 1
                    degree[j] += 1
                    cost += _adj_mat[i][j]
            else:  # if the search in p_2 is successful
                i, j = (e_ij[0], e_ij[1]) if e_ij[0] in S else (e_ij[1], e_ij[0])
                mark[j] = 1
                S.add(j)
                T.add(e_ij)
                degree[i] += 1
                degree[j] += 1
                cost += _adj_mat[i][j]
    return SpanningTree(T, degree, cost)


def connected_component(_n, _v, _edges):
    """
    # https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
    :param _n: number of vertices
    :param _v: vertex contained by target component
    :type _edges: set of edges, e.g. {(0, 1), (1, 2)}
    """

    def dfs_util(temp, _v, _visited):
        _visited[_v] = True  # Mark the current vertex as visited
        temp.add(_v)  # Store the vertex to list
        adj_edges = [_ for _ in _edges if _v in _]
        for i in [_[0] if _[1] == _v else _[1] for _ in adj_edges]:  # Repeat for all vertices adjacent to this vertex v
            if not _visited[i]:
                temp = dfs_util(temp, i, _visited)  # Update the list
        return temp

    return dfs_util(set(), _v, [False] * _n)


def del_ins(_n, _adj_mat, _V, _E, p, _max_degree):
    edges = p.edges.copy()
    degree = p.degree.copy()
    cost = p.cost
    e_del = random.choice(tuple(edges))
    u, v = e_del
    edges.remove(e_del)
    degree[u] -= 1
    degree[v] -= 1
    cost -= _adj_mat[u][v]
    T_u = connected_component(_n, u, edges)
    T_v = _V - T_u
    e_ins = random.choice([_ for _ in set(_E) - p.edges if
                           _[0] in T_u and degree[_[0]] < _max_degree and
                           _[1] in T_v and degree[_[1]] < _max_degree or
                           _[1] in T_u and degree[_[1]] < _max_degree and
                           _[0] in T_v and degree[_[0]] < _max_degree])
    edges.add(e_ins)
    degree[e_ins[0]] += 1
    degree[e_ins[1]] += 1
    cost += _adj_mat[e_ins[0]][e_ins[1]]
    return SpanningTree(edges, degree, cost)


def dijkstra_in_tree(_n, _V, _E, source):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    Q = _V.copy()
    dist = [math.inf] * _n
    dist[source] = 0
    while Q != set():
        u = min([_ for _ in enumerate(dist) if _[0] in Q], key=lambda x: x[1])[0]
        Q.remove(u)
        for e in [_ for _ in _E if u in _]:
            v = e[0] if e[1] == u else e[1]
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
    return dist


def two_er(_n, _adj_mat, p, max_iter):
    edges = p.edges.copy()
    cost = p.cost
    best_wx = ()  # either best_wx or best_w, best_x cannot launch the other
    best_w, best_x = -1, -1  # because order matters!
    for t in range(max_iter):
        cost_diff = math.inf  # reset every iteration!
        e_uv = random.choice([_ for _ in edges])
        u, v = e_uv
        for e in [_ for _ in edges if u not in _ and v not in _]:  # non_adjacent edge of e_uv
            w, x = e
            if not is_tree(_n, edges - {e_uv, e} | {(u, w), (v, x)}):
                w, x = e[1], e[0]
            temp = _adj_mat[u][w] + _adj_mat[v][x] - _adj_mat[u][v] - _adj_mat[w][x]  # the less, the better
            if temp < cost_diff:
                cost_diff = temp
                best_wx = e
                best_w, best_x = w, x
        edges = edges - {e_uv, best_wx} | {(u, best_w), (v, best_x)}
        cost = cost + cost_diff
    return SpanningTree(edges, p.degree.copy(), cost,)


def one_er(_n, _adj_mat, _E, p, _max_degree, max_iter):
    edges = p.edges.copy()
    degree = p.degree.copy()
    cost = p.cost
    for t in range(max_iter):
        # First stage of 1ER
        for e_uv in [_ for _ in edges if degree[_[0]] == _max_degree or degree[_[1]] == _max_degree]:
            u, v = e_uv
            try:
                e_xy = random.choice([_ for _ in set(_E) - edges if
                                      _adj_mat[_[0]][_[1]] <= _adj_mat[u][v] and
                                      degree[_[0]] + 1 <= _max_degree and
                                      degree[_[1]] + 1 <= _max_degree and
                                      is_tree(_n, edges - {e_uv} | {_})])
            except IndexError:
                continue
            else:  # if the search is successful
                x, y = e_xy
                edges = edges - {e_uv} | {e_xy}
                degree[u] -= 1
                degree[v] -= 1
                degree[x] += 1
                degree[y] += 1
                cost = cost - _adj_mat[u][v] + _adj_mat[x][y]
        # Second stage of 1ER
        for e_uv in edges:
            u, v = e_uv
            try:
                e_xy = random.choice([_ for _ in set(_E) - edges if
                                      _adj_mat[_[0]][_[1]] < _adj_mat[u][v] and
                                      degree[_[0]] + 1 <= _max_degree and
                                      degree[_[1]] + 1 <= _max_degree and
                                      is_tree(_n, edges - {e_uv} | {_})])
            except IndexError:
                continue
            else:  # if the search is successful
                x, y = e_xy
                edges = edges - {e_uv} | {e_xy}
                degree[u] -= 1
                degree[v] -= 1
                degree[x] += 1
                degree[y] += 1
                cost = cost - _adj_mat[u][v] + _adj_mat[x][y]
    return SpanningTree(edges, degree, cost)


def hssga(_adj_mat, _max_degree, n_pop, n_iter, P_c, P_b, alpha, PR_pop, rs):
    _n = len(_adj_mat)
    _V = set(range(_n))  # vertices set
    _E = {(i, j) for i in range(_n) for j in range(i + 1, _n)}
    _E = sorted(_E, key=lambda x: _adj_mat[x[0]][x[1]])  # edge list sorted by weight in descending order

    pop = [prim_rst(_n, _adj_mat, _V, _E, _max_degree) for _ in range(n_pop)]
    pop_avg_cost = sum([_.cost for _ in pop]) / n_pop
    # pop_min_cost = min([_.cost for _ in pop])

    T_gb = min(pop, key=lambda x: x.cost)  # best-so-far generated
    unchanged_iter = 0

    data = {'pop_avg_cost': [0] * n_iter, 'best_cost': [0] * n_iter}

    for _iter in range(n_iter):
        u_01 = random.random()
        if u_01 < P_c:
            p_1 = np.random.choice(sorted(random.sample(pop, 2), key=lambda x: x.cost), p=[P_b, 1-P_b])
            p_2 = np.random.choice(sorted(random.sample(pop, 2), key=lambda x: x.cost), p=[P_b, 1-P_b])
            T_C = x_over(_n, _adj_mat, _V, _E, p_1, p_2, _max_degree)
        else:
            p_1 = np.random.choice(sorted(random.sample(pop, 2), key=lambda x: x.cost), p=[P_b, 1-P_b])
            T_C = del_ins(_n, _adj_mat, _V, _E, p_1, _max_degree)
        edge_diff = 1 - len(T_gb.edges.intersection(T_C.edges)) / (_n - 1)
        if T_gb.cost/T_C.cost+alpha*edge_diff > 1:
            T_C = two_er(_n, _adj_mat, T_C, max_iter=3)
            T_C = one_er(_n, _adj_mat, _E, T_C, _max_degree, max_iter=3)
        for T in pop:
            if T.edges == T_C.edges:  # T_C not unique
                break
        else:  # T_C unique, apply replacement strategy
            if T_C.cost < T_gb.cost:
                T_gb = T_C
                unchanged_iter = 0
            else:
                unchanged_iter += 1
            inferior_T = random.choice([_ for _ in pop if _.cost > pop_avg_cost])
            pop = [T_C if _.edges == inferior_T.edges else _ for _ in pop]  # replace T_C with inferior_T
            if unchanged_iter > PR_pop:  # apply population update strategy
                count = 0
                while count < rs:
                    i, T_i = random.choice(list(enumerate(pop)))
                    T_p = del_ins(_n, _adj_mat, _V, _E, T_i, _max_degree)  # perturbed solution
                    for T in pop:
                        if T.edges == T_p.edges:  # T_p not unique, do not replace
                            break
                    else:  # T_p unique, do replacement
                        pop[i] = T_p  # replace T_i with T_p
                        count += 1
        pop_avg_cost = sum([_.cost for _ in pop]) / n_pop
        data['pop_avg_cost'][_iter] = pop_avg_cost
        data['best_cost'][_iter] = T_gb.cost
    return T_gb, data


if __name__ == "__main__":
    n = 9  # num of vertices
    max_degree = 3
    adj_mat = [[0, 224, 224, 361, 671, 300, 539, 800, 943],
               [224, 0, 200, 200, 447, 283, 400, 728, 762],
               [224, 200, 0, 400, 566, 447, 600, 922, 949],
               [361, 200, 400, 0, 400, 200, 200, 539, 583],
               [671, 447, 566, 400, 0, 600, 447, 781, 510],
               [300, 283, 447, 200, 600, 0, 283, 500, 707],
               [539, 400, 600, 200, 447, 283, 0, 361, 424],
               [800, 728, 922, 539, 781, 500, 361, 0, 500],
               [943, 762, 949, 583, 510, 707, 424, 500, 0]]  # BB solution; 2256
    V = set(range(n))
    E = {(i, j) for i in range(n) for j in range(i + 1, n)}
    E = sorted(E, key=lambda x: adj_mat[x[0]][x[1]])  # sorted by weight in descending order

    T_1 = prim_rst(n, adj_mat, V, E, max_degree)
    T_1.print()

    T_2 = prim_rst(n, adj_mat, V, E, max_degree)
    T_2.print()

    T_12 = x_over(n, adj_mat, V, E, T_1, T_2, max_degree)
    T_12.print()

    T_3 = del_ins(n, adj_mat, V, E, T_1, max_degree)
    T_3.print()

    T_4 = two_er(n, adj_mat, T_3, max_iter=3)
    T_4.print()

    T_5 = one_er(n, adj_mat, E, T_4, max_degree, max_iter=3)
    T_5.print()

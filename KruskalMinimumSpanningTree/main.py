"""
https://www.hackerrank.com/challenges/kruskalmstrsub/problem
"""

def kruskals(node_count, edge_from, edge_to, edge_weights):
    """
    4 (node_count)
    [5, 3, 6, 7, 4, 5] (edge_weights)
    [1, 1, 4, 2, 3, 3] (edge_from)
    [2, 3, 1, 4, 2, 4] (edge_to)
    """
    
    edges = []
    subtree = {}
    min_weight = 0
    
    for x in range(0, len(edge_weights)):
        edges.append((edge_weights[x], edge_from[x], edge_to[x]))
        
    edges.sort()
    
    """
    [(3, 1, 3), (4, 3, 2), (5, 1, 2), (5, 3, 4), (6, 4, 1), (7, 2, 4)] (edges)
    """

    for x in edges:
        if x[1] not in subtree and x[2] not in subtree:
            # (weight, end node)
            subtree[x[1]] = {(x[0], x[2])}
            subtree[x[2]] = {(x[0], x[1])}
        elif x[1] in subtree and x[2] not in subtree:
            # (weight, end node)
            subtree[x[1]].add((x[0], x[2]))
            subtree[x[2]] = {(x[0], x[1])}
        elif x[1] not in subtree and x[2] in subtree:
            # (weight, end node)
            subtree[x[1]] = {(x[0], x[2])}
            subtree[x[2]].add((x[0], x[1]))
        else:
            # (100, 1, 4) (x)
            cycle_found = False
            nodes_visited = {x[1]}
            nodes_to_visit = set()
            
            for y in subtree[x[1]]:
                if y[1] != x[2]:
                    nodes_to_visit.add(y[1])
                else:
                    cycle_found = True
                    nodes_to_visit.clear()
                    break

            while nodes_to_visit:
                z = nodes_to_visit.pop()

                for y in subtree[z]:
                    if y[1] == x[2]:
                        cycle_found = True
                        break
                    elif y[1] not in nodes_visited:
                        nodes_to_visit.add(y[1])

                nodes_visited.add(z)
                    
            if cycle_found is False:
                subtree[x[1]].add((x[0], x[2]))
                subtree[x[2]].add((x[0], x[1]))

    """
    {1: [(3, 3)], 3: [(3, 1), (4, 2), (5, 4)], 2: [(4, 3)], 4: [(5, 3)]} (subtree)
    """
    
    for x in subtree:
        for edge in subtree[x]:
            weight = edge[0]
            target_node = edge[1]
            
            min_weight += weight
            subtree[target_node].remove((weight, x))
    
    """
    12 (min_weight)
    """

    return min_weight

if __name__ == '__main__':
    input = """4 6
1 2 5
1 3 3
4 1 6
2 4 7
3 2 4
3 4 5"""

    input_lines = input.split("\n")

    g_nodes = input_lines[0].split(" ")[0]
    g_from = []
    g_to = []
    g_weight = []

    for x in input_lines[1:]:
        line_vals = x.split(" ")

        g_from.append(int(line_vals[0]))
        g_to.append(int(line_vals[1]))
        g_weight.append(int(line_vals[2]))

    print(kruskals(g_nodes, g_from, g_to, g_weight))
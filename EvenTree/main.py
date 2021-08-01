"""
https://www.hackerrank.com/challenges/even-tree/problem
"""

def getConnectedNodeCount(forest, start_node):
    nodes_to_visit = {start_node}
    nodes_visited = set()
    
    while nodes_to_visit:
        current_node = nodes_to_visit.pop()
        nodes_visited.add(current_node)

        nodes_to_visit.update(forest[current_node].difference(nodes_visited))
    
    return len(nodes_visited)

def getMaxEvenForests(t_nodes, t_edges, t_from, t_to):
    max_even_forest_count = 0
    forest = {}
    
    for x in range(1, t_nodes + 1):
        forest[x] = set()
        
    # {1: [], 2: [], 3: [], 4: [], 5: [], 6: [],
    #  7: [], 8: [], 9: [], 10: []} (forest)
    
    for y in range(0, t_edges):
        forest[t_from[y]].add(t_to[y])
        forest[t_to[y]].add(t_from[y])
        
    # {1: [2, 3, 6], 2: [1, 5, 7], 3: [1, 4], 4: [3], 5: [2], 6: [1, 8],
    #  7: [2], 8: [6, 9, 10], 9: [8], 10: [8]} (forest)
    
    for y in range(0, t_edges):
        # try removing the edge and test if it results in an even split
        edge_begin = t_from[y]
        edge_end = t_to[y]
        
        forest[edge_begin].remove(edge_end)
        forest[edge_end].remove(edge_begin)
        
        begin_connected_node_count = getConnectedNodeCount(forest, edge_begin)
        end_connected_node_count = getConnectedNodeCount(forest, edge_end)
        
        if begin_connected_node_count % 2 != 0 \
        or end_connected_node_count % 2 != 0:
            # add the edge back if this wasn't a split that resulted in an even
            # node count in both of the resulting trees
            forest[edge_begin].add(edge_end)
            forest[edge_end].add(edge_begin)
        else:
            max_even_forest_count += 1
        
    return max_even_forest_count

if __name__ == '__main__':
    print(getMaxEvenForests(10,
                            9,
                            [2, 3, 4, 5, 6, 7, 8, 9, 10],
                            [1, 1, 3, 2, 1, 2, 6, 8, 8]))

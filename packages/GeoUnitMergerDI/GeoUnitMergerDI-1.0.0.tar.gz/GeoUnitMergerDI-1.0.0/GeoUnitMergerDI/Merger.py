import numpy as np
from typing import List, Hashable

class Graph:
    def __init__(self, node_edges: dict, node_weights: dict):
        """
        constructor of graph object
        :param dict node_edges: dictionary of the form {<node_id_1>: set(<node_ids> that are neighbors of <node_id_1>), <node_id_2>: ...}
        :param dict node_weights: dictionary of the form {<node_id_1>: weight_1 (float), <node_id_2>: weight_2 (float), ...}
        """
        self.node_edges = node_edges
        self.node_weights = np.array([v for v in node_weights.values()])
        self._ids2pos = {k: i for i, k in enumerate(node_weights.keys())}
        self._pos2ids = {i: k for i, k in enumerate(node_weights.keys())}
        
    def join_node(self, destination: Hashable, origin: Hashable):
        neighbors_origin: set = self.node_edges[origin]
        neighbors_origin.discard(destination)
        # update neighbors destination
        self.node_edges[destination] = self.node_edges[destination].union(neighbors_origin)
        self.node_edges[destination].discard(origin)
        # update each neighbor of origin
        for neighbor in neighbors_origin:
            self.node_edges[neighbor].discard(origin)
            self.node_edges[neighbor].add(destination)
        # remove origin from edges
        self.node_edges.pop(origin)
        # update weights
        destination_pos = self._keys2positions([destination])[0]
        origin_pos = self._keys2positions([origin])[0]
        self.node_weights[destination_pos] += self.node_weights[origin_pos]
        self.node_weights[origin_pos] = np.inf
    
    def get_key_weights(self):
        keys = [k for k in self._ids2pos.keys()]
        return keys, self.node_weights
    
    def _keys2positions(self, keys: List[Hashable]):
        return [self._ids2pos[k] for k in keys]
    
    def _positions2keys(self, positions: List[int]):
        return [self._pos2ids[p] for p in positions]
    
    def get_weights_by_keys(self, keys: List[Hashable]):
        """
        :param keys: list of python dictionary keys for which to retrieve their weights.
        """
        return self.node_weights[self._keys2positions(keys)]


def min_find(neighbors_keys: List[Hashable], graph: Graph):
    neighbors_weights = graph.get_weights_by_keys(neighbors_keys)
    sorted_indexes = np.argsort(neighbors_weights)
    # return neighbor (position) with lowest weight
    return neighbors_keys[sorted_indexes[0]] if len(sorted_indexes) > 0 else None

def max_find(neighbors_keys: List[Hashable], graph: Graph):
    neighbors_weights = graph.get_weights_by_keys(neighbors_keys)
    sorted_indexes = np.argsort(neighbors_weights)[::-1]
    # return neighbor (position) with greatest weight
    return neighbors_keys[sorted_indexes[0]] if len(sorted_indexes) > 0 else None

def random_find(neighbors: List[Hashable]):
    # return neighbor (position) at random
    return np.random.choice(neighbors, 1) if len(neighbors) > 0 else None
    
def reduce(destination: Hashable, origin: Hashable, graph: Graph):
    graph.join_node(destination, origin)
    return graph

def get_true_parents(parents: dict):
    keys = parents.keys()
    for key in keys:
        parent_key = parents[key]
        while parent_key in keys:
            parent_key = parents[parent_key]
        
        parents[key] = parent_key
    
    return parents

def merge_all(threshold, graph: Graph, find_algorithm='min_find'):
    """
    probably just sort at the beginning, then traverse all nodes and process the ones that have weights < threshold.
    traverse all because if they are sorted, at the beginning there will be a position N in which weights_i > thershold 
    for i > N, but when processing a node can increase the weight of a neighbor which previously was weight_k < threshold
    but after joining them it does not longer fullfill, so check them all (just onces is necesarry thanks to the graph structure)
    """
    parents = {}
    # sort nodes depending on their initial weights
    keys, weights = graph.get_key_weights()
    weights = np.array(weights)
    indexes = np.argsort(weights)
    # start processing lower weight nodes
    for index in indexes:
        # get node id
        key = keys[index]
        
        # verify if node satisfies condition    
        if graph.get_weights_by_keys([key])[0] > threshold:
            continue
        
        # find-reduce
        neighbors = list(graph.node_edges[key])
        if find_algorithm == 'min_find':
            neighbor_key = min_find(neighbors, graph)
        elif find_algorithm == 'max_find':
            neighbor_key = max_find(neighbors, graph)
        elif find_algorithm == 'rand_find':
            neighbor_key = random_find(neighbors)
        else:
            print('[ERR]: find_algorithm parameter only supports "min_find", "max_find", "rand_find"')
            neighbor_key = None

        if neighbor_key is not None:
            parents[key] = neighbor_key
            graph = reduce(neighbor_key, key, graph)
        
    return graph, parents


#!/!usr/bin/env python
__program__ = "get_dfs_traversal_order.py"
__description__ = "Get the dfs traversal order of a given graph using preorder traversal"
__date__ = "15/03/2024"
__author__ = "Christophe Lagaillarde"
__version__ = "2.0"
__license__ = "MIT License"
__copyright__ = "Copyright 2024 (c) Christophe Lagaillarde"

from typing import Optional

def get_dfs_traversal_order(graph: dict[str, list[str]],
			    traversal_order: Optional[list[str]] = None,
			    node_key_index: int = 0,
			    node_predecessor: Optional[dict[Optional[str]]] = None) -> list: 

	if traversal_order is None:
		traversal_order = []
	node_predecessor = node_predecessor if node_predecessor else {key: None for key in graph}
	key_node_selected: Optional[str] = list(node_predecessor.keys())[node_key_index]
	nodes_list :list = graph[key_node_selected]

	if len(traversal_order) == len(graph):
		return traversal_order

	if  key_node_selected not in traversal_order:
		traversal_order.append(key_node_selected)

	next_node_key: Optional[str] = next((node for node in nodes_list if node not in traversal_order)\
					    , node_predecessor[key_node_selected])

	if node_predecessor[next_node_key] is None:
		node_predecessor[next_node_key] = key_node_selected

	node_key_index = list(node_predecessor.keys()).index(next_node_key)

	return get_dfs_traversal_order(graph, traversal_order, node_key_index, node_predecessor)

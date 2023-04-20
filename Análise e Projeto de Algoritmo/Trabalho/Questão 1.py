# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 15:29:18 2023

@author: Matheus
"""

"""
    1 – Gerar randomicamente um grafo não orientado com 100 vértices , com um número baixo
    de ligações ( de uma a dez vezes o número de vértices ). 
"""

import random
import networkx as nx

edge_probability = 0.3
n_nodes = 10

G = nx.DiGraph()

G.add_nodes_from(range(n_nodes))

for u in G.nodes:
    for v in G.nodes:
        if random.random() < edge_probability:
            G.add_edge(u, v)

import numpy as np
import math
from scipy import spatial
import networkx as nx
import matplotlib.pyplot as plt
nnodes = 100
avg_deg = 5
r = math.sqrt((avg_deg+1)/(nnodes*math.pi))
#r = 0.15
positions =  np.random.rand(nnodes,2)
kdtree = spatial.KDTree(positions)
pairs = kdtree.query_pairs(r)
G = nx.Graph()
G.add_nodes_from(range(nnodes))
G.add_edges_from(list(pairs))
pos = dict(zip(range(nnodes),positions))
#nx.draw(G,pos)
#plt.show()
#print(pos)

adj_list = {}
#for key, value in pos.items():
#    adj_list.setdefault(key, []) #create list for values
#    adj_list[key].append(value)#
#print(pairs)
for i in pairs:
    adj_list.setdefault(i[0], []) #create list for values
    adj_list[i[0]].append(i[1])#
for key, val in adj_list.iteritems():
    print key, val

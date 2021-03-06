import numpy as np
import math
from scipy import spatial
import networkx as nx
import matplotlib.pyplot as plt
import sys
import random


def writetofile(pairs):
    adj_list = {}
    for i in pairs:
        adj_list.setdefault(i[0], []) #create list for values
        adj_list.setdefault(i[1], []) #create list for values
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    count = 0
    for key, val in adj_list.items():
        count += 1
        #print key, val
        for p in pos[key]:
            f.write(str(p) + " ")
        for p in val:
            for q in pos[p]:
                f.write(str(q) + " ")
        f.write('S' + '\n')
    f.close()
    print(count)


file = sys.argv[1]
f = open(file, 'w')

nnodes = 16000
avg_deg = 64
r = math.sqrt((avg_deg)/(nnodes*math.pi))
print(r)

#r = 0.15
#positions =  np.random.rand(nnodes,2)
positions = []
count = 0
while (count < nnodes):
    coordinates = []
    rad = random.uniform(0,1)
    deg = random.uniform(0,(2*math.pi))   #generate random degree
    #print(deg)
    coordinates.append(math.sqrt(rad)*math.cos(deg))
    coordinates.append(math.sqrt(rad)*math.sin(deg))
    # coordinates.append(math.sqrt(r)*math.cos(math.radians(deg)))
    # coordinates.append(math.sqrt(r)*math.sin(math.radians(deg)))
    #print(coordinates)
    positions.append(coordinates)
    count += 1
kdtree = spatial.KDTree(positions)
pairs = kdtree.query_pairs(r)
G = nx.Graph()
G.add_nodes_from(range(nnodes))
G.add_edges_from(list(pairs))
pos = dict(zip(range(nnodes),positions))
# nx.draw(G,pos)
# plt.show()
writetofile(pairs)

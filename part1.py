import numpy as np
import copy
import math
from scipy import spatial
import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
from collections import OrderedDict


def smallestLast(nnodes, adj_list, degrees):
    print("nothing")
    orderedDict = OrderedDict(sorted(adj_list.items(), key=lambda t: len(t[1])))
    sum = 0
    for key,value in orderedDict.iteritems():
        degrees[key] = len(value)
        sum += len(value)
    #print(degrees)
    calculatedDeg = sum/nnodes
    print(calculatedDeg)
    maxDeg = len(next(reversed(orderedDict.items()))[1])
    minDeg = len(orderedDict.items()[0][1])
    print(minDeg)
    print(maxDeg)

def degreeCalc(nnodes, adj_list, degrees):
    colorCount = {}
    colorsUsed = {}
    maxColorClassSize = 0
    colorNum = 1
    orderedDict = OrderedDict(sorted(adj_list.items(), key=lambda t: len(t[1])))
    for key,value in orderedDict.iteritems():
        degrees[key] = len(value)
    #print(degrees)
    maxDeg = len(next(reversed(orderedDict.items()))[1])
    minDeg = len(orderedDict.items()[0][1])
    #print(minDeg)
    #print(maxDeg)
    while(nnodes):
        if(next(reversed(orderedDict.items()))):
            item = next(reversed(orderedDict.items()))
        newColor = False
        color = 0
        for i in range(1,colorNum):
            #check which color numbers are not its adjacents' colors

            if(item[0] in colorsUsed):
                print("A")
                colorsUsed[item[0]] = {}
                color = i
                newColor = True
                break
            else:
                if(i in colorsUsed[item[0]]):
                    print("AAA")
                else:
                     #found a color that it is not adjacent to
                    print("*")
                    newColor = True
                    color = i
                    break
        #if all colors are taken by adj vertices
        if(newColor == False):
            colorNum += 1
            color = colorNum
        newColor = False
        #keep track of number of vertices with that color
        if(color in colorCount):
            colorCount[color] = colorCount[color] + 1
            if(colorCount[color] > maxColorClassSize):
                maxColorClassSize = colorCount[color]
        else:
            colorCount[color] = 1
        #iterate through adjacent vertices and add color used
        for i in item[1]:
            degrees[i] = degrees[i] - 1
            if(i in colorsUsed):
                colorsUsed[i][color] = True
            else:
                colorsUsed[i] = {}
                colorsUsed[i][color] = True
        nnodes -= 1
        orderedDict.popitem(last=False)
    # minDeg = len(orderedDict.popitem(last = False)[1])
    # maxDeg = len(orderedDict.popitem(last = True)[1])

    # for i in nnodes:

    # print(orderedDict.popitem(last = True))
    # print(orderedDict.popitem(last = True))
    print(colorNum)
    print("hi")
    #for key in adj_list:

def writetofile(adj_list,pairs):

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
            f.write(str(p) + " ") #write x and y of center vertice
        for p in val:               #write x and y of adjacent vertices
            for q in pos[p]:
                f.write(str(q) + " ")
        f.write('S' + '\n')
    f.close()
    #print(count)


file = "blah.txt"
f = open(file, 'w')

nnodes = 4000
avg_deg = 64
r = math.sqrt(avg_deg/float(nnodes))  #for disk
#r = math.sqrt((avg_deg)/(nnodes*math.pi))  #for square

#r = 0.15
print(r)

#r = 1
positions = []
#positions =  np.random.rand(nnodes,2)

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
nx.draw(G,pos)
#plt.show()
adj_list = {}
writetofile(adj_list, pairs)
degrees = {}
adj_list_copy = copy.deepcopy(adj_list)
smallestLast(nnodes, adj_list_copy,degrees)
#degreeCalc(nnodes,adj_list, degrees)

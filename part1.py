import numpy as np
import copy
import math
from scipy import spatial
import networkx as nx
import matplotlib.pyplot as plt
import sys
import random
from collections import OrderedDict
from pprint import pprint
import random
from multiprocessing import Queue
from collections import deque
import time
import string

cache = {'#348ABD': (0.20392156862745098, 0.5411764705882353, 0.7411764705882353), '#6d904f': (0.42745098039215684, 0.5647058823529412, 0.30980392156862746), '#ccebc4': (0.8, 0.9215686274509803, 0.7686274509803922), 'purple': (0.5019607843137255, 0.0, 0.5019607843137255), '#eeeeee': (0.9333333333333333, 0.9333333333333333, 0.9333333333333333), '#30a2da': (0.18823529411764706, 0.6352941176470588, 0.8549019607843137), 'yellow': (1.0, 1.0, 0.0), 'b': (0.0, 0.0, 1.0), '#E5E5E5': (0.8980392156862745, 0.8980392156862745, 0.8980392156862745), 'white': (1.0, 1.0, 1.0), 'cyan': (0.0, 1.0, 1.0), '#92C6FF': (0.5725490196078431, 0.7764705882352941, 1.0), '#bc82bd': (0.7372549019607844, 0.5098039215686274, 0.7411764705882353), '#009E73': (0.0, 0.6196078431372549, 0.45098039215686275), '#EAEAF2': (0.9176470588235294, 0.9176470588235294, 0.9490196078431372), '#ffed6f': (1.0, 0.9294117647058824, 0.43529411764705883), '#03ED3A': (0.011764705882352941, 0.9294117647058824, 0.22745098039215686), '#FF9F9A': (1.0, 0.6235294117647059, 0.6039215686274509), '0.60': (0.6, 0.6, 0.6), '#003FFF': (0.0, 0.24705882352941178, 1.0), '#EEEEEE': (0.9333333333333333, 0.9333333333333333, 0.9333333333333333), '#8C0900': (0.5490196078431373, 0.03529411764705882, 0.0), '#555555': (0.3333333333333333, 0.3333333333333333, 0.3333333333333333), '#006374': (0.0, 0.38823529411764707, 0.4549019607843137), '#00D7FF': (0.0, 0.8431372549019608, 1.0), 'red': (1.0, 0.0, 0.0), '#7600A1': (0.4627450980392157, 0.0, 0.6313725490196078), '#feffb3': (0.996078431372549, 1.0, 0.7019607843137254), 'gray': (0.5019607843137255, 0.5019607843137255, 0.5019607843137255), '#8EBA42': (0.5568627450980392, 0.7294117647058823, 0.25882352941176473), '#77BEDB': (0.4666666666666667, 0.7450980392156863, 0.8588235294117647), '#00FFCC': (0.0, 1.0, 0.8), 'y': (0.75, 0.75, 0), 'w': (1.0, 1.0, 1.0), '#C4AD66': (0.7686274509803922, 0.6784313725490196, 0.4), '#B0E0E6': (0.6901960784313725, 0.8784313725490196, 0.9019607843137255), '#81b1d2': (0.5058823529411764, 0.6941176470588235, 0.8235294117647058), '#f0f0f0': (0.9411764705882353, 0.9411764705882353, 0.9411764705882353), 'r': (1.0, 0.0, 0.0), '#b3de69': (0.7019607843137254, 0.8705882352941177, 0.4117647058823529), '.8': (0.8, 0.8, 0.8), '#e5ae38': (0.8980392156862745, 0.6823529411764706, 0.2196078431372549), '0.40': (0.4, 0.4, 0.4), '0.00': (0.0, 0.0, 0.0), '#bcbcbc': (0.7372549019607844, 0.7372549019607844, 0.7372549019607844), '#FFC400': (1.0, 0.7686274509803922, 0.0), 'green': (0.0, 0.5019607843137255, 0.0), '#D65F5F': (0.8392156862745098, 0.37254901960784315, 0.37254901960784315), '#988ED5': (0.596078431372549, 0.5568627450980392, 0.8352941176470589), '#467821': (0.27450980392156865, 0.47058823529411764, 0.12941176470588237), '#afeeee': (0.6862745098039216, 0.9333333333333333, 0.9333333333333333), 'darkgoldenrod': (0.7215686274509804, 0.5254901960784314, 0.043137254901960784), 'black': (0.0, 0.0, 0.0), '#4878CF': (0.2823529411764706, 0.47058823529411764, 0.8117647058823529), '#8dd3c7': (0.5529411764705883, 0.8274509803921568, 0.7803921568627451), '#6ACC65': (0.41568627450980394, 0.8, 0.396078431372549), '#fc4f30': (0.9882352941176471, 0.30980392156862746, 0.18823529411764706), '#CCB974': (0.8, 0.7254901960784313, 0.4549019607843137), '#8A2BE2': (0.5411764705882353, 0.16862745098039217, 0.8862745098039215), '#55A868': (0.3333333333333333, 0.6588235294117647, 0.40784313725490196), 'k': (0.0, 0.0, 0.0), '#0072B2': (0.0, 0.4470588235294118, 0.6980392156862745), '0.50': (0.5, 0.5, 0.5), '#E8000B': (0.9098039215686274, 0.0, 0.043137254901960784), '#7A68A6': (0.47843137254901963, 0.40784313725490196, 0.6509803921568628), 'magenta': (1.0, 0.0, 1.0), '#B8860B': (0.7215686274509804, 0.5254901960784314, 0.043137254901960784), '#CC79A7': (0.8, 0.4745098039215686, 0.6549019607843137), '#8b8b8b': (0.5450980392156862, 0.5450980392156862, 0.5450980392156862), '#FFFEA3': (1.0, 0.996078431372549, 0.6392156862745098), 'firebrick': (0.6980392156862745, 0.13333333333333333, 0.13333333333333333), '#64B5CD': (0.39215686274509803, 0.7098039215686275, 0.803921568627451), '#E24A33': (0.8862745098039215, 0.2901960784313726, 0.2), '#FFB5B8': (1.0, 0.7098039215686275, 0.7215686274509804), '#F0E442': (0.9411764705882353, 0.8941176470588236, 0.25882352941176473), '0.75': (0.75, 0.75, 0.75), 'blue': (0.0, 0.0, 1.0), '#FBC15E': (0.984313725490196, 0.7568627450980392, 0.3686274509803922), 'c': (0.0, 0.75, 0.75), '#777777': (0.4666666666666667, 0.4666666666666667, 0.4666666666666667), '#8172B2': (0.5058823529411764, 0.4470588235294118, 0.6980392156862745), '#bfbbd9': (0.7490196078431373, 0.7333333333333333, 0.8509803921568627), '#cbcbcb': (0.796078431372549, 0.796078431372549, 0.796078431372549), '.15': (0.15, 0.15, 0.15), '#C44E52': (0.7686274509803922, 0.3058823529411765, 0.3215686274509804), '#56B4E9': (0.33725490196078434, 0.7058823529411765, 0.9137254901960784), '#97F0AA': (0.592156862745098, 0.9411764705882353, 0.6666666666666666), 'g': (0.0, 0.5, 0.0), '#A60628': (0.6509803921568628, 0.023529411764705882, 0.1568627450980392), '#fdb462': (0.9921568627450981, 0.7058823529411765, 0.3843137254901961), '0.70': (0.7, 0.7, 0.7), '#4C72B0': (0.2980392156862745, 0.4470588235294118, 0.6901960784313725), '0.5': (0.5, 0.5, 0.5), '#D0BBFF': (0.8156862745098039, 0.7333333333333333, 1.0), '#017517': (0.00392156862745098, 0.4588235294117647, 0.09019607843137255), '#001C7F': (0.0, 0.10980392156862745, 0.4980392156862745), '#fa8174': (0.9803921568627451, 0.5058823529411764, 0.4549019607843137), 'm': (0.75, 0, 0.75), '#B47CC7': (0.7058823529411765, 0.48627450980392156, 0.7803921568627451), '#D55E00': (0.8352941176470589, 0.3686274509803922, 0.0)}

def smallestLastt(nnodes, adj_list, degrees):
    print("nothing")
    sum = 0
    for key,value in orderedDict.iteritems():
        degrees[key] = len(value)
        sum += len(value)
    orderedDict = OrderedDict(sorted(degrees.items(), key=lambda t: t[1]))
    #invert dictionary
    degreesToVertices = {}
    for vert,neighbors in degrees.iteritems():
        #if that vertice is not already in that degree's dict
        if(degreesToVertices.get(len(neighbors), None) == None):
            degreesToVertices[len(neighbors)] = {}
            degreesToVertices[len(neighbors)][vert] = True
        else:
            degreesToVertices[len(neighbors)][vert] = True
    #print(degrees)
    print(degreesToVertices)
    calculatedDeg = sum/nnodes
    print(calculatedDeg)
    maxDeg = len(next(reversed(orderedDict.items()))[1])
    minDeg = len(orderedDict.items()[0][1])
    print(minDeg)
    print(maxDeg)



def smallestLast(nnodes, adj_list, adj_list_copy, degrees, smallestFirst, minDegVert, maxDegVert):
    print("nothing")
    orderedDict = OrderedDict(sorted(adj_list.items(), key=lambda t: len(t[1])))
    sum = 0
    degreesList = []
    degreesToNumVertices = []
    for key,value in orderedDict.iteritems():
        degrees[key] = len(value)
        sum += len(value)

    calculatedDeg = sum/nnodes
    print("AVERAGE DEGREE: " + str(calculatedDeg))
    maxDeg = len(next(reversed(orderedDict.items()))[1])
    minDeg = len(orderedDict.items()[0][1])
    print("MIN DEGREE: "+ str(minDeg))
    print("MAX DEGREE: "+ str(maxDeg))

    degreesToVertices = {}  #key: degree, value: dictionary of vertices with that degree
    for vert,neighbors in degrees.iteritems():
        #if that vertice is not already in that degree's dict
        if(neighbors not in degreesToVertices):
            degreesToVertices[neighbors] = {}
            degreesToVertices[neighbors][vert] = True
        else:
            degreesToVertices[neighbors][vert] = True

    for degree in degreesToVertices:
        degreesList.append(degree)
        degreesToNumVertices.append(len(degreesToVertices[degree]))
    for vert in degreesToVertices[maxDeg]:
        maxDegVert.append(vert)
    for vert in degreesToVertices[minDeg]:
        minDegVert.append(vert)
    #maxDegVert = degreesToVertices[maxDeg]
    degreesList, degreesToNumVertices = zip(*sorted(zip(degreesList,degreesToNumVertices)))

     #DEGREE DISTRIBUTION PLOT
    x = np.array(degreesList)
    y = np.array(degreesToNumVertices)
    plt.gcf().clear()
    barlist = plt.bar(x,y)
    plt.show()

    #print(degrees)
    #pprint(degreesToVertices)
    #print(adj_list)
    originalDegrees = []
    deletedDegrees = []

    minDegCopy = minDeg
    nnodesCopy = nnodes
    tempMin = 0
    deg = 0
    flag = False
    # while(nnodesCopy > 0):
    #     print(deg, nnodesCopy)
    #     # if(flag == True):
    #     #     deg = tempMin
    #     tempMin = deg
    #     flag = False
    #     currMin = deg
    #     if(deg in degreesToVertices):
    #         for vertice in degreesToVertices[deg].items():
    #             #remove it
    #             #if verticeCpy in degreesToVertice
    #             if vertice[0] in degreesToVertices[deg]:
    #                 del degreesToVertices[deg][vertice[0]]
    #             #for purposes of seq coloring plot
    #             #originalDegrees.append(degrees[vertice])
    #                 originalDegrees.append(deg)
    #                 deletedDegrees.append(len(adj_list_copy[vertice[0]]))
    #
    #                 smallestFirst.append(vertice[0])
    #                 #remove it from its neighbors
    #                 nnodesCopy -= 1
    #                 for neighbor in adj_list_copy[vertice[0]].items():
    #                     #remove that neighbor from its current degree spot
    #                     if neighbor[0] in adj_list_copy[len(adj_list_copy[neighbor[0]])]:
    #                         del degreesToVertices[len(adj_list_copy[neighbor[0]])][neighbor[0]]
    #                         #print("**")
    #
    #                     #remove it from its neighbor's   list
    #                     if vertice[0] in adj_list_copy[neighbor[0]]:
    #                         del adj_list_copy[neighbor[0]][vertice[0]]
    #                         print("!!")
    #                     if(len(adj_list_copy[neighbor[0]]) < deg):
    #                         tempMin = len(adj_list_copy[neighbor[0]])
    #                     #add it to the degree spot that is one less
    #                     if len(adj_list_copy[neighbor[0]]) not in degreesToVertices:
    #                         degreesToVertices[len(adj_list_copy[neighbor[0]])] = {}
    #                     degreesToVertices[len(adj_list_copy[neighbor[0]])][neighbor[0]] = True
    #
    #
    #
    #                 if nnodesCopy <= 0:
    #                     break
    #                 # if(tempMin < deg):
    #                 #     print("HIIIIII")
    #                 #     deg = tempMin
    #                 #     flag = True
    #                 #     break
    #                 # if(flag == True):
    #                 #     continue
    #     #check to see if cycle needs to repeat
    #     #print("******************************")
    #     if flag == False:
    #         deg += 1
    #     if(deg > maxDeg):
    #         deg = 0


    #iterate through degrees
    for deg in range(0,maxDeg+1):
        #print(deg, nnodesCopy)
        flag = False
        currMin = deg
        if(deg in degreesToVertices):
            for vertice in degreesToVertices[deg]:
                #for purposes of seq coloring plot
                originalDegrees.append(degrees[vertice])
                deletedDegrees.append(len(adj_list_copy[vertice]))

                smallestFirst.append(vertice)
                #remove it from its neighbors
                nnodesCopy -= 1
                if(nnodesCopy == deg):
                    print("Terminal Clique Size: " + str(nnodesCopy))
                for neighbor in adj_list_copy[vertice]:
                    #remove that neighbor from its current degree spot
                    del degreesToVertices[degrees[neighbor]][neighbor]
                    tempMin = degrees[neighbor]
                    #add it to the degree spot that is one less
                    degreesToVertices[tempMin][neighbor] = True

                    #remove it from its neighbor's list
                    del adj_list_copy[neighbor][vertice]
                    if(tempMin < deg):
                        deg = tempMin
                        flag = True
                        break
                if(flag == True):
                    break
        #check to see if cycle needs to repeat
        if((deg == (maxDeg - 1)) and (nnodesCopy != 0)):
            deg = 0
    # print(smallestFirst)
    # print(originalDegrees)
    # print(deletedDegrees)
    # print(len(originalDegrees))
    # print(maxDeg)
    revOrgDegList = list(reversed(originalDegrees))
    revDelDegList = list(reversed(deletedDegrees))
    print("Max Degree when deleted: " + str(max(revDelDegList)))
    x1 = np.array(revOrgDegList)
    x2 = np.array(revDelDegList)
    y = np.array(range(0,nnodes))
    plt.gcf().clear()
    plt.plot(y, x1)
    plt.plot(y, x2)
    plt.show()



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

def color(adj_list, smallestFirst, colorClassSizes, parallelColors, colorToVert, vertToColor):



    #colorToVert hashmap (float,  key: color code, value: vertices with that color

    #vertToColor hashmap (int, [float, dict of neighbor's colors]): key: vertice, value: tuple of color code, neighbor's colors
            ##vertToNeighborsColors (int, list of colors): key: vertice, value: neighbor's colors

    neighborsColors = {} #key: vertice, value: neighbor's colors
    smallestFirst = list(reversed(smallestFirst))
    for vert in adj_list:
        neighborsColors[vert] = {}
    for vert in smallestFirst:
        flag = False
        #vertToColor[vert] = []
        #if there are any available colors (iterate through colorToVert)
        #if any of the available colors are not being used by any of its neighbors, aka check, for each neighbor, if
            #is present within

        for color in colorToVert:
            #if vertToColor[vert][1] is None
            #if color not in vertToColor[vert][1]:
            if color not in neighborsColors[vert]:
                colorToVert.setdefault(color, []).append(vert)
                vertToColor[vert] = color
                #update all neighbors
                for neighbor in adj_list[vert]:
                    neighborsColors[neighbor][color] = True
                    #neighborsColors[neighbor].setdefault(color, {})[True]
                    #neighborsColors[neighbor].setdefault(color, {})[True]
                    #vertToColor[neighbor][1].setdefault(color, {})[True]
                flag = True
                break

        #if there are no colors preexisting or if all current colors are being used by neighbors
        if flag == False:
            #color = np.random.rand(3,)
            color = random.choice(cache.keys())
            #to avoid duplicates
            cache.pop(color)
            colorToVert.setdefault(color, []).append(vert)
            vertToColor[vert] = color
            #update all neighbors
            for neighbor in adj_list[vert]:
                neighborsColors[neighbor][color] = True
                #neighborsColors[neighbor].setdefault(color, {})[True]
                #vertToColor[neighbor].setdefault(color, {})[True]
    # for x in vertToColor:
    #     print(str(x) + ":" +vertToColor[x])
    # for x in colorToVert:
    #     print x + " : ", colorToVert[x]
    colors = len(colorToVert)
    max_key = max(colorToVert, key= lambda x: len(set(colorToVert[x])))
    maxColorClassSize = len(colorToVert[max_key])
    print("MAX COLOR CLASS SIZE: " + str(maxColorClassSize))
        # for y in vertToColor[x]:
        #     print(, ":", vertToColor[x])
    #get each colors set size
    # colorClassSizes = []
    # parallelColors = []
    for color in colorToVert:
        colorClassSizes.append(len(colorToVert[color]))
        parallelColors.append(color)
    #sort lists
    colorClassSizes, parallelColors = zip(*sorted(zip(colorClassSizes,parallelColors)))
    colorClassSizes = list(colorClassSizes)
    parallelColors = list(parallelColors)
    colorClassSizes = list(reversed(colorClassSizes))
    parallelColors = list(reversed(parallelColors))
    # print("length: " + str(len(colorClassSizes)))
    print("Colors in RGG: " + str(colors))

    plt.gcf().clear()
    barlist = plt.bar(np.array(range(0,colors)),np.array(colorClassSizes))
    for i in range(0,len(colorClassSizes)):
        barlist[i].set_color(parallelColors[i])
    plt.show()

def createBipartiteGraphs(G, pos, pairs, adj_list, smallestFirst, colorClassSizes, parallelColors, colorToVert, vertToColor):

    #bipartiteVertices
    #for 6 diff combos using top 4 colors
    color1 = [0,0,0,1,1,2]
    color2 = [1,2,3,2,3,3]
    colorClassSizes, parallelColors = zip(*sorted(zip(colorClassSizes,parallelColors)))
    colorClassSizes = list(colorClassSizes)
    parallelColors = list(parallelColors)
    colorClassSizes = list(reversed(colorClassSizes))
    print("MAX COLOR CLASS SIZE 2: " + str(colorClassSizes[0]))
    parallelColors = list(reversed(parallelColors))
    colorToVertWithDicts = {}
    for color in colorToVert:
        colorToVertWithDicts[color] = dict((k,True) for k in colorToVert[color])
    mostEdges = 1
    secondMostEdges = 0
    mostOptimalColors = []
    secondMostOptimalColors = []
    bestBackboneVertex = 0
    secondBestBackboneVertex = 0
    bestBipartitePairs = set()
    secondBestBipartitePairs = set()
    bestSubgraphAdjList = {}
    secondBestSubgraphAdjList = {}
    for j in range(0,len(color1)):
        subgraphAdjList = {}
        bipartitePairs = set()
        for pair in pairs:
            tuple = ()
            keep = False
            if pair[0] in colorToVertWithDicts[parallelColors[color1[j]]]:
                if pair[1] in colorToVertWithDicts[parallelColors[color2[j]]]:
                    tuple = (pair[0], pair[1])
                    #bipartitePairs[pair[0]] = pair[1]
                    keep = True
                    bipartitePairs.add(tuple)
            elif pair[1] in colorToVertWithDicts[parallelColors[color1[j]]]:
                 if pair[0] in colorToVertWithDicts[parallelColors[color2[j]]]:
                     tuple = (pair[1], pair[0])
                     #bipartitePairs[pair[1]] = pair[0]
                     keep = True
                     bipartitePairs.add(tuple)
        #create adj list for subgraph
        for i in bipartitePairs:
            if i[0] not in subgraphAdjList:
                subgraphAdjList[i[0]] = {}
            if i[1] not in subgraphAdjList:
                subgraphAdjList[i[1]] = {}
            subgraphAdjList[i[0]][i[1]] = True
            subgraphAdjList[i[1]][i[0]] = True
        #breadth first search
        print("HI")
        backbonePairs = set()
        maxEdges = 0
        bestStartingVertex = 0
        for vertex in subgraphAdjList:
            edges = 0
            vertQueue = deque()
            visited = {}
            startVertex = vertex
            visited[startVertex] = True
            # currVertex = startVertex
            vertQueue.append(startVertex)
            while len(vertQueue) != 0:
                currVertex = vertQueue.popleft()
                for neighbor in subgraphAdjList[currVertex]:
                    if neighbor not in visited:
                        visited[neighbor] = True
                        vertQueue.append(neighbor)
                    edges += 1
            if edges > maxEdges:
                bestStartingVertex = vertex
                maxEdges = edges
        #With best Vertex
        print("Edges in backbone: " + str(maxEdges))


        queue = deque()
        visited = {}
        startVertex = bestStartingVertex
        visited[startVertex] = True
        # currVertex = startVertex
        queue.append(startVertex)
        while len(queue) != 0:
            currVertex = queue.popleft()
            for neighbor in subgraphAdjList[currVertex]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    tuple = (currVertex,neighbor)
                    backbonePairs.add(tuple)
        #display largest component aka backbone
        visitedColors = []
        for vertex in visited:
            visitedColors.append(vertToColor[vertex])
        print("Nodes in Backbone: "+ str(len(visited)))
        print("% Domination: " + str(len(visited)/float(nnodes)))
        sum = 0
        for node in visited:
            sum += len(subgraphAdjList[node])

        calculatedDeg = sum/float(len(visited))
        print("AVERAGE DEGREE: " + str(calculatedDeg))

        plt.gcf().clear()
        nx.draw_networkx_nodes(G,pos,nodelist=visited,node_color=visitedColors,node_size=20, alpha=0.8)
        nx.draw_networkx_edges(G,pos,edgelist=list(backbonePairs),width=0.5,alpha=0.5,edge_color='b')
        plt.show()

        #see if it is one of the largest backbones
        if(maxEdges > mostEdges):
            mostOptimalColors.append(color1[j])
            mostOptimalColors.append(color2[j])
            bestBackboneVertex = bestStartingVertex
            # bestBipartitePairs = backbonePairs
            #bestSubgraphAdjList = subgraphAdjList
        elif(maxEdges > secondMostEdges):
            secondMostOptimalColors.append(color1[j])
            secondMostOptimalColors.append(color2[j])
            secondBestBackboneVertex = bestStartingVertex
            # secondBestBipartitePairs = backbonePairs
            #secondBestSubgraphAdjList = subgraphAdjList

    # subgraphAdjList = {}
    # bipartitePairs = set()
    # for pair in pairs:
    #     tuple = ()
    #     keep = False
    #     if pair[0] in colorToVertWithDicts[parallelColors[mostOptimalColors[0]]]:
    #         if pair[1] in colorToVertWithDicts[parallelColors[mostOptimalColors[1]]]:
    #             tuple = (pair[0], pair[1])
    #             #bipartitePairs[pair[0]] = pair[1]
    #             keep = True
    #             bipartitePairs.add(tuple)
    #     elif pair[1] in colorToVertWithDicts[parallelColors[mostOptimalColors[0]]]:
    #          if pair[0] in colorToVertWithDicts[parallelColors[mostOptimalColors[1]]]:
    #              tuple = (pair[1], pair[0])
    #              #bipartitePairs[pair[1]] = pair[0]
    #              keep = True
    #              bipartitePairs.add(tuple)
    # #create adj list for subgraph
    # for i in bipartitePairs:
    #     if i[0] not in subgraphAdjList:
    #         subgraphAdjList[i[0]] = {}
    #     if i[1] not in subgraphAdjList:
    #         subgraphAdjList[i[1]] = {}
    #     subgraphAdjList[i[0]][i[1]] = True
    #     subgraphAdjList[i[1]][i[0]] = True
    # #breadth first search
    # print("HI")
    # backbonePairs = set()
    # maxEdges = 0
    # for vertex in subgraphAdjList:
    #     edges = 0
    #     vertQueue = deque()
    #     visited = {}
    #     startVertex = vertex
    #     visited[startVertex] = True
    #     # currVertex = startVertex
    #     vertQueue.append(startVertex)
    #     while len(vertQueue) != 0:
    #         currVertex = vertQueue.popleft()
    #         for neighbor in subgraphAdjList[currVertex]:
    #             if neighbor not in visited:
    #                 visited[neighbor] = True
    #                 vertQueue.append(neighbor)
    #             edges += 1
    #
    # #With best Vertex
    # print("Edges in FINAL: " + str(maxEdges))
    #
    #
    # queue = deque()
    # visited = {}
    # startVertex = bestBackboneVertex
    # visited[startVertex] = True
    # # currVertex = startVertex
    # queue.append(startVertex)
    # while len(queue) != 0:
    #     currVertex = queue.popleft()
    #     for neighbor in subgraphAdjList[currVertex]:
    #         if neighbor not in visited:
    #             visited[neighbor] = True
    #             queue.append(neighbor)
    #             tuple = (currVertex,neighbor)
    #             backbonePairs.add(tuple)
    # #display largest component aka backbone
    # visitedColors = []
    # for vertex in visited:
    #     visitedColors.append(vertToColor[vertex])
    # plt.gcf().clear()
    # nx.draw_networkx_nodes(G,pos,nodelist=visited,node_color=visitedColors,node_size=20, alpha=0.8)
    # nx.draw_networkx_edges(G,pos,edgelist=list(backbonePairs),width=0.5,alpha=0.5,edge_color='b')
    # plt.show()
    #FIRST BACKBONE
    # bestSubgraphAdjList = {}
    # for i in bestBipartitePairs:
    #     if i[0] not in bestSubgraphAdjList:
    #         bestSubgraphAdjList[i[0]] = {}
    #     if i[1] not in bestSubgraphAdjList:
    #         bestSubgraphAdjList[i[1]] = {}
    #     bestSubgraphAdjList[i[0]][i[1]] = True
    #     bestSubgraphAdjList[i[1]][i[0]] = True
    #
    # queue = deque()
    # visited = {}
    # startVertex = bestBackboneVertex
    # visited[startVertex] = True
    # # currVertex = startVertex
    # queue.append(startVertex)
    # testEdges = 0
    # while len(queue) != 0:
    #     currVertex = queue.popleft()
    #     for neighbor in bestSubgraphAdjList[currVertex]:
    #         if neighbor not in visited:
    #             visited[neighbor] = True
    #             queue.append(neighbor)
    #             tuple = (currVertex,neighbor)
    #             bestBipartitePairs.add(tuple)
    #         testEdges += 1
    # #display largest component aka backbone
    # visitedColors = []
    # for vertex in visited:
    #     visitedColors.append(vertToColor[vertex])
    # plt.gcf().clear()
    # nx.draw_networkx_nodes(G,pos,nodelist=visited,node_color=visitedColors,node_size=20, alpha=0.8)
    # nx.draw_networkx_edges(G,pos,edgelist=list(bestBipartitePairs),width=0.5,alpha=0.5,edge_color='b')
    # print("Test edges: " + str(testEdges))
    # plt.show()


        #print(bipartitePairs)
        # plt.gcf().clear()
        # nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color1[i]]], node_color=parallelColors[color1[i]], node_size=20, alpha=0.8)
        # nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color2[i]]], node_color=parallelColors[color2[i]], node_size=20, alpha=0.8)
        # nx.draw_networkx_edges(G,pos,edgelist=list(bipartitePairs), width = 0.5, alpha =0.5, edge_color='b')
        # print("2 Color Class Sizes Total: " + str(len(colorToVert[parallelColors[color1[i]]] + colorToVert[parallelColors[color2[i]]])))
        # print("Edges: " + str(len(bipartitePairs)))
        # plt.show()

    #for i in range(0,len(color1)):

        #plt.gcf().clear()
        # nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color1[i]]], node_color=parallelColors[color1[i]], node_size=20, alpha=0.8)
        # nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color2[i]]], node_color=parallelColors[color2[i]], node_size=20, alpha=0.8)
        # #G.add_edges_from(list(pairs))
        #nx.draw_networkx_edges(G,pos,edgelist=list(pairs), width = 0.5, alpha =0.5, edge_color='b')

        #WORKING
    # for i in range(0,1):
        # print(len(colorToVert[parallelColors[color1[i]]] + colorToVert[parallelColors[color2[i]]]))
        # H = G.subgraph(colorToVert[parallelColors[color1[i]]] + colorToVert[parallelColors[color2[i]]])
        # print("Edges: " + str(len(H.edges())))
        # nx.draw_networkx_edges(H,pos,edgelist=H.edges(), width = 0.5, alpha =0.5, edge_color='b')
        # plt.show()



        #nx.draw(H,pos=pos,node_color=)

        # H.add_nodes_from(colorToVert[parallelColors[color1[i]]],node_color=parallelColors[color1[i]], node_size=20, alpha=0.8)
        # H.add_nodes_from(colorToVert[parallelColors[color2[i]]],node_color=parallelColors[color2[i]], node_size=20, alpha=0.8)
        # #nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color1[i]]], node_color=parallelColors[color1[i]], node_size=20, alpha=0.8)
        #nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[parallelColors[color2[i]]], node_color=parallelColors[color2[i]], node_size=20, alpha=0.8)




    # for color in colorToVert:
    #     nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[color], node_color=color, node_size=20, alpha=0.8)
    #     nx.draw_networkx_edges(G,pos,edgelist=list(pairs), width = 0.5, alpha =0.5, edge_color='b')

    #else generate a new color, add to colorToVert and vertToColor
def writetofile(adj_list,pairs):
    for i in pairs:
        if i[0] not in adj_list:
            adj_list[i[0]] = {} #create list for values
        if i[1] not in adj_list:
            adj_list[i[1]] = {} #create list for values
        adj_list[i[0]][i[1]] = True
        adj_list[i[1]][i[0]] = True
    # for i in pairs:
    #     adj_list.setdefault(i[0], []) #create list for values
    #     adj_list.setdefault(i[1], []) #create list for values
    #     adj_list[i[0]].append(i[1])
    #     adj_list[i[1]].append(i[0])
    count = 0
    # for key, val in adj_list.items():
    #     count += 1
    #     #print key, val
    #     for p in pos[key]:
    #         f.write(str(p) + " ") #write x and y of center vertice
    #     for p in val:               #write x and y of adjacent vertices
    #         for q in pos[p]:
    #             f.write(str(q) + " ")
    #     f.write('S' + '\n')
    # f.close()
    #print(count)


file = "blah.txt"
f = open(file, 'w')

nnodes = 1000
avg_deg = 32
#r = math.sqrt(avg_deg/float(nnodes))  #for disk
r = math.sqrt((avg_deg)/(nnodes*math.pi))  #for square

#r = 0.3
print(r)
start = time.time()
#r = 1
positions = []
positions =  np.random.rand(nnodes,2)
print("POSITIONS:")

count = 0
# while (count < nnodes):
#     coordinates = []
#     rad = random.uniform(0,1)
#     deg = random.uniform(0,(2*math.pi))   #generate random degree
#     #print(deg)
#     coordinates.append(math.sqrt(rad)*math.cos(deg))
#     coordinates.append(math.sqrt(rad)*math.sin(deg))
#     # coordinates.append(math.sqrt(r)*math.cos(math.radians(deg)))
#     # coordinates.append(math.sqrt(r)*math.sin(math.radians(deg)))
#     #print(coordinates)
#     positions.append(coordinates)
#     count += 1
kdtree = spatial.KDTree(positions)
#print("KDTREE: ")
pairs = kdtree.query_pairs(r)
#print("PAIRS: ")
#print(pairs)
print("GRAPH EDGES: "+ str(len(pairs)) )
G = nx.Graph()
# G.add_nodes_from(range(nnodes))
# G.add_edges_from(list(pairs))

pos = dict(zip(range(nnodes),positions))
# nx.draw(G,pos)
# plt.show()

adj_list = {}
writetofile(adj_list, pairs)
degrees = {}
adj_list_copy = copy.deepcopy(adj_list)
smallestFirst = []
minDeg = []
maxDeg = []
smallestLast(nnodes,adj_list, adj_list_copy,degrees, smallestFirst,minDeg, maxDeg)
colorClassSizes = []
parallelColors = []
colorToVert = {}
vertToColor = {}


#maxPairs = [item for item in ]
# pairs = dict(pairs)
# for maxVert in maxDeg:
#     if maxVert in pairs:
#         maxPairs.add(pairs[maxVert])


color(adj_list, smallestFirst, colorClassSizes, parallelColors, colorToVert, vertToColor)

nx.draw_networkx_nodes(G,pos,nodelist=range(nnodes),node_color='r',node_size=20,alpha=0.4)
print(maxDeg)
nx.draw_networkx_nodes(G,pos,nodelist=maxDeg,node_color='yellow',node_size=100, alpha=0.8)
nx.draw_networkx_nodes(G,pos,nodelist=minDeg,node_color='black',node_size=100, alpha=0.8)


for vert in maxDeg:
    maxPairs = set()
    for neighbor in adj_list[vert]:
        maxPairs.add((vert,neighbor))
    nx.draw_networkx_edges(G,pos,edgelist=list(maxPairs), width = 0.9, alpha =0.8, edge_color='black')
for vert in minDeg:
    minPairs = set()
    for neighbor in adj_list[vert]:
        minPairs.add((vert,neighbor))
    nx.draw_networkx_edges(G,pos,edgelist=list(minPairs), width = 0.9, alpha =0.8, edge_color='black')

plt.show()
nx.draw_networkx_nodes(G,pos,nodelist=range(nnodes),node_color='r',node_size=20,alpha=0.8)
nx.draw_networkx_edges(G,pos,edgelist=list(pairs),width=0.5,alpha=0.5,edge_color='b')
plt.show()
#nx.draw_networkx_edges(G,pos,edgelist=list(pairs), width = 0.5, alpha =0.5, edge_color='b')

# for i in adj_list:
#     print adj_list[i]

#WALKTHROUGH
# pprint(adj_list)
# labels = {}
# letter = 0
# for i in range(0,16):
#     labels[i] = i #string.ascii_lowercase[letter]
#     #letter +=1
# nx.draw_networkx_labels(G,pos,labels,font_size=10)
# nx.draw_networkx_nodes(G,pos,nodelist=range(nnodes),node_color='r',node_size=150,alpha=0.8)





#G.add_edges_from(list(pairs))
#nx.draw(G,pos)



# plt.gcf().clear()
# for color in colorToVert:
#     nx.draw_networkx_nodes(G,pos,nodelist=colorToVert[color], node_color=color, node_size=20, alpha=0.8)
# #G.add_edges_from(list(pairs))
# nx.draw_networkx_edges(G,pos,edgelist=list(pairs), width = 0.5, alpha =0.5, edge_color='b')
# plt.show()

createBipartiteGraphs(G, pos, pairs, adj_list, smallestFirst, colorClassSizes, parallelColors, colorToVert, vertToColor)
end = time.time()
print("Time Taken: " + str(end-start))
#degreeCalc(nnodes,adj_list, degrees)

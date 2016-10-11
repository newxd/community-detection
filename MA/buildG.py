import networkx as nx
import math
import csv
import random as rand
import sys
import numpy as np
import GeneticOperation as GO


def buildG(G, file_):
    row,column=file_.shape
    for i in range(row):
        for j in range(column):
            if file_[i, j] == 1:
                G.add_edge(i, j)
def initial_pop(G,n,pop,Alpha): #G is graph,n :numbers of vertex,pop:population of chromosome
    x=np.zeros([pop,n])
    for i in range(pop):
        x[i]=range(1,n+1)
    for i in range(pop):
        t=0
        while t<=n*Alpha:
            r=rand.randint(1,n)
            if r in G.nodes():
                ider=x[i][r-1]
                neighbors=G.edges(r)
                for j in range(len(neighbors)):
                    neighbor=neighbors[j][1]
                    x[i][neighbor-1]=ider
                t+=1
    return x
def UpdataPopulation(P,A,children,best):
    row,column=P.shape
    P_new=np.zeros([row,column])
    AllP=np.zeros([row+len(children)+len(best),column])
    AllP[0:row]=P
    AllP[row:row+len(children)]=children
    AllP[-1]=best
    L=np.zeros([1,len(AllP)])
    for i in range(len(AllP)):
        L[0][i]=GO.fitness(A,AllP[i])
    S=np.argsort(L[0])
    t=-1
    for i in range(len(P_new)):
        P_new[i]=AllP[S[t]]
        t-=1
    return P_new













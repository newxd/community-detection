import GeneticOperation as GO
import numpy as np
import copy
def GetCommunity(chromosome):
    L=[]
    cluster=()
    for i in range(len(chromosome)):
        V=()
        ider=chromosome[i]
        if ider in cluster:
            continue
        else:
            cluster+=(ider,)
            V+=(i,)
        for j in range(i+1,len(chromosome)):
            if chromosome[j]==ider:
                V+=(j,)
        L.append(V)
    return L

def FindNeighbors(chromosome):
    L=GetCommunity(chromosome)
    m=len(L)
    n=0
    for i in range(m):
        n+=len(L[i])
    neighbors=np.empty([n*(m-1),n])
    num=0
    for i in range(m):
        for k in range(len(L[i])):

            for j in range(m):
                if i==j:
                    continue
                else:
                    neighbors[num]=copy.deepcopy(chromosome)
                    neighbors[num][L[i][k]]=chromosome[L[j][0]]
                    num+=1
    return neighbors

def FindBest(P,A):
    best=0
    for i in range(len(P)):
        if GO.fitness(A,P[i])>GO.fitness(A,P[best]):
            best=i
    return P[best]














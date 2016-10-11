import networkx as nx
import numpy as np
import GenerateData
import buildG
import GenerateData as GD
import GeneticOperation as GO
import LocalSearch
Gm=50 #maximum numbers of generations
Sp=450   #populaton size
Spool=Sp/2 #population of mating pool
Stour=2    #number of tournament
Pc=0.8   #crossover probability
Pm=0.2   #mutate probability
Alaph=0.2 #initial population parmeter
data=GenerateData.generate(0.5)  #computer generated data,128 nodes,4 communities
A=data  #Graph data,adj_matrix
G=nx.Graph()
buildG.buildG(G,data)
population=buildG.initial_pop(G,128,Sp,Alaph) #initial population
t=0     #generation numbers
BestPop=np.zeros([Gm,128])
while t<Gm:
    parents=GO.selection(population,A,Spool,Stour)
    children=GO.CrossMutate(G,parents,Pc,Pm)
    Bestchild=LocalSearch.FindBest(children,A)
    IsLocal=False
    while not IsLocal:
        L=LocalSearch.FindNeighbors(Bestchild)
        best=LocalSearch.FindBest(L,A)
        if GO.fitness(A,best)>GO.fitness(A,Bestchild):
            Bestchild=best
        else:
            IsLocal=True
    population=buildG.UpdataPopulation(population,A,children,Bestchild)
    print 'Generation %d'%t
    print 'Max fitness=',GO.fitness(A,population[0])
    print LocalSearch.GetCommunity(population[0])
    BestPop[t]=population[0]
    t+=1
FinalResult=LocalSearch.FindBest(BestPop,A)
CommunityPartion=LocalSearch.GetCommunity(FinalResult)
print 'Community partition:',CommunityPartion






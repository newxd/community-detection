import numpy as np
import random
def generate(kout):
    nodes = 128; # the  number    of    nodes;
    nc = 4; # the    number    of    clusters;
    k = 16; # the    average    overall    degree    of    each    node;

    nm = nodes / nc;
    pin = float(k - kout)/(nm - 1);
    pout = float(kout)/ (nm * (nc - 1));

    y0 = np.zeros([nodes,nodes]);
    count = 1;

    for i in range(nodes):
        if i >= nm * count:
            count+=1

        for j in range(i+1,nodes):

            if j <= nm * count:
                p0 = pin
            else:
                p0 = pout
            if (random.random()<= p0):
                y0[i,j] = 1

    return (y0 + y0.T)



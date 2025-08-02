import habitat
import random
import matplotlib.pyplot as plt
import numpy as np
import math

max_effort=1000
no_f_genes=100

def init():
  genome = [[],[]]
  for i in range(6):
    genome[0].append(random.uniform(-1, 1))
  for i in range(6):
    genome[1].append(random.uniform(-1, 1))
  return genome

def mutate(genome):
  rtn = [genome[0].copy(), genome[1].copy()]
  for i in range(len(rtn[0])):
    rtn[0][i]+=random.uniform(-0.1, 0.1)
  for i in range(6):
    rtn[1][i]+=random.uniform(-0.1, 0.1)
  return rtn

def output(genome):
  print(entropy(genome))
  print("---------")
  x=0.0
  y=0.0
  xlist=[]
  ylist=[]
  for i in range(1, 1000):
    xlist.append(x)
    ylist.append(y)
    x=get_next(genome[0], x, y)
    y=get_next(genome[1], x, y)
  xpoints = np.array(xlist)  
  ypoints = np.array(ylist)
  plt.scatter(xpoints, ypoints)
  plt.show()
  

def entropy(genome):
  points = 10000
  score = 0
  x=0.0
  y=0.0
  map = {}
  for i in range(points):
    if abs(x)<1 and abs(y)<1:
      index = round((x+1)*50)+ round((y+1)*50)*100;
      newscore = map.setdefault(index, 0) + 1
      map[index]= newscore
    x=get_next(genome[0], x, y)
    y=get_next(genome[1], x, y)
  for key in map.keys():
    probability = map[key]/points
    score -= probability*math.log2(probability)
  return score

def evaluate(genome):
  return -abs(10.35-entropy(genome))

def get_next(gene, xcoord, ycoord):
  return gene[0] + xcoord * gene[1] + xcoord * xcoord* gene[2] + ycoord * gene[3] + ycoord * ycoord * gene[4] + xcoord * ycoord * gene[5]


habitat.run(init, mutate, output, evaluate)

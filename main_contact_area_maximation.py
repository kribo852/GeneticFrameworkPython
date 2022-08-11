import habitat
import random
import numpy as np

dimension = 20

def init():
  rtn = np.array([[False]*dimension]*dimension)
  for i in range(25):
    rtn[random.randrange(dimension), random.randrange(dimension)]=True
  return rtn

def mutate(genome):
  density = 0
  rtn = np.array([[False]*dimension]*dimension)
  for i in range(dimension):
    for j in range(dimension):
      rtn[i,j] = genome[i,j]
      if rtn[i,j]:
        density+=1

  for k in range(5):
    x = random.randrange(dimension)
    y = random.randrange(dimension)
    rtn[x, y] = True if random.uniform(0,1) < density/(dimension**2) else False
  
  return rtn

def output(genome):
  print("score: {}".format(evaluate(genome)))
  print("baseline: {}".format(evaluate(init())))
  for i in range(dimension):
    rowresult=""
    for j in range(dimension):
      rowresult += "XX" if genome[i, j]  else "  " 
    print(rowresult)
  print("--------")

def evaluate(genome):
  pathused = np.array([[0]*dimension]*dimension)
  for i in range(dimension):
    for j in range(dimension):
      pathused[i,j] = 0
  return path(genome, pathused)

def path(genome, pathused, x=0, y=0):
  if not outside(x, y):
    if not genome[x, y] and not pathused[x, y]:
      pathused[x, y] = True
      return path(genome, pathused, x+1, y)+path(genome, pathused, x-1, y)+path(genome, pathused, x, y+1)+path(genome, pathused, x, y-1)
    elif not pathused[x, y]:
      pathused[x, y] = True
      return 1
  return 0

def outside(x, y):
  return x>=dimension or y>=dimension or x<0 or y<0

def combine_specimen(genome1, genome2):
  rtn = np.array([[False]*dimension]*dimension)
  for i in range(dimension):
    for j in range(dimension):
      rtn[i, j] = genome1[i, j] if bool(random.getrandbits(1)) else genome2[i, j]
  return rtn

habitat.run(init, mutate, output, evaluate, combine_specimen)

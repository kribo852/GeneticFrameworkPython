import habitat
import random
import matplotlib.pyplot as plt
import numpy as np
import math

max_effort=1000
no_f_genes=100

def init():
  genome = []
  for i in range(no_f_genes):
    genome.append(random.uniform(0, 0.5))
  return scale(genome)

def mutate(genome):
  rtn = genome.copy()
  for i in range(len(genome)):
    if random.randrange(25) == 0:
      rtn[i] = max(0, rtn[i]+random.uniform(-0.5, 0.5))

  swapindex1 = random.randrange(len(genome))
  swapindex2 = random.randrange(len(genome))
  a = rtn[swapindex1]
  rtn[swapindex1] = rtn[swapindex2]
  rtn[swapindex2] = a
  
  return scale(rtn)

def output(genome):
  str = ""
  for gene in genome:
    str += "{:.2f}".format(gene)
    str += " "
  print(str)
  print(evaluate(genome))
  print("baseline: {}".format(evaluate(init())))
  print("---------")
  ypoints = np.array(genome)
  plt.plot(ypoints, marker = 'o')
  plt.show()
  

def evaluate(genome):
  chance_of_success = 0.1
  score = 0
  for gene in genome:
    score +=chance_of_success*effort_to_chance_multiplyer4(gene)
    chance_of_success *= 0.975
  return score


def effort_to_chance_multiplyer(effort):
  return 1 - 0.9**effort

def effort_to_chance_multiplyer2(effort):
  return min(1, effort/15)

def effort_to_chance_multiplyer3(effort):
  return effort/math.hypot(10, effort)

def effort_to_chance_multiplyer4(effort):
  if effort < 5:
    return 0.5*math.exp((effort-5)/12)
  else:
    return 1-0.5*math.exp((5-effort)/12)

def effort_to_chance_multiplyer5(effort):
  return 1.0

def scale(genome):
  rtn = genome.copy()
  sum = 0
  for gene in genome:
    sum += gene
  for i in range(len(rtn)):
    rtn[i] = rtn[i]*max_effort/sum
  return rtn


habitat.run(init, mutate, output, evaluate)

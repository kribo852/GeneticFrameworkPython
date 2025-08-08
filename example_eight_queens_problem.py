import habitat
import random
import math

#A example program that solves the eight queens problem

#Generate a initial untested solution
def init():
  genome = []
  for i in range(8):
    genome.append(i)
#permutate
  for i in range(24):
    permutate_once(genome)   
  return genome

#mutate a solution
def mutate(genome):
  rtn = genome.copy()
  permutate_once(genome);
  return rtn

def permutate_once(genome):
  index_a = random.randrange(len(genome));
  index_b = random.randrange(len(genome));
  tmp_val = genome[index_a]
  genome[index_a] = genome[index_b]
  genome[index_b] = tmp_val

#print a solution
def output(genome):
  for i in range(len(genome)):
    line = ""
    for j in range(len(genome)):
      if genome[i]==j:
        line += " X "
      else:
        line += " - "
    print(line)
  print() 

#evaluate a solution to compare it to other solutions
#the more queen pieces that can strike each other, the more negative score
#just checking the diagonals, as the solution representation guarantees that
#two queens can´t strike each other vertically or horizontally
def evaluate(genome):
  score = 0
  for i in range(len(genome)):
    for j in range(i+1, len(genome)):
      if j-i == abs(genome[j]-genome[i]):
        score -= 1
  return score


def finish(genome):
  return evaluate(genome) == 0


#run the algorithm
genome = habitat.run(init, mutate, output, evaluate, stop_condition=finish)
output(genome)



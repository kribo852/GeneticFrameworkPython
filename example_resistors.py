import habitat
import random
import math
import time

#A example program that produces a electronic network of resistors.
#The goal is to combine the given resistors into a network with the wanted
#resistance

GIVEN_OHM_RESISTORS = 200.0
WANTED_OHM = 37.0
TOLERANCE = 0.05


#Generate a initial untested solution
def init():
  genome = []
  number_of_parallel_resistor_lines = random.randrange(1, 20)
  for i in range(number_of_parallel_resistor_lines):
    genome.append(random.randrange(1, 20))
  return genome


#mutate a solution
def mutate(genome):
  rtn = genome.copy()
  if random.getrandbits(1) == 1:
    if random.getrandbits(1) == 1:
      rtn.append(random.randrange(1, 20))
    elif len(rtn) > 1:
      rtn.pop(random.randrange(0, len(rtn)))
  else:
    tmp_index = random.randrange(0, len(rtn))
    rtn[tmp_index] += random.randrange(-1, 2)
    if rtn[tmp_index] <= 0:
      rtn[tmp_index] = 1;
    
  return rtn

#print a solution
def output(genome):
  maximum_number_of_resistors = max(genome) 
  for i in range(len(genome)):
    line = "|-"
    for j in range(maximum_number_of_resistors):
      if j < genome[i]:
        line += "Ω"
      else:
        line += "-"
    print(line + "-|");
  
  print("result: "+ str(genome))
  print("score: " + str(evaluate(genome)))
  print("---------")
  

#evaluate a solution to compare it to other solutions
# this function is divided into two parts. Firstly, if the difference
# between the wanted and measured resistance is bigger than the tolerance,
# then return the negative difference -abs(resistance-WANTED).
# Otherwise, if the difference is within the tolerance,
# then return 1/ the number of used resistors, so that fewer resistors gives a
# higher score.
def evaluate(genome):
  resistance = calculate_resistance(genome)
  if(abs(resistance-WANTED_OHM) > WANTED_OHM*TOLERANCE):
    return -abs(resistance-WANTED_OHM)    
  else:
    return 1.0/sum_of_resistors(genome)
    

def calculate_resistance(genome):
  conductance = 0
  for i in range(len(genome)):
    conductance += 1.0/(genome[i]*GIVEN_OHM_RESISTORS)
  return 1.0/conductance

def sum_of_resistors(genome):  
  return sum(genome)

def finishFunction():
  start_time = time.time()
  return lambda genome: time.time() - start_time > 16


#run the algorithm
habitat.run(init, mutate, output, evaluate, stop_condition=finishFunction())

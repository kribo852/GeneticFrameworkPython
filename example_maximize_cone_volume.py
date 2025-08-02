import habitat
import random
import math

#A example program that maximizes the volume of a 3d cone, given a
#maximum surface area.


#Generate a initial untested solution
def init():
  genome = []
  for i in range(2):
    genome.append(random.uniform(0, 2.0))
  return genome


#mutate a solution
def mutate(genome):
  rtn = genome.copy()
  if random.getrandbits(1) == 1:
    if random.getrandbits(1) == 1:
      rtn[0] = random.uniform(0, 1.0)
    if random.getrandbits(1) == 1:
      rtn[1] = random.uniform(0, 1.0)
  elif random.getrandbits(1) == 1:
    rtn[0] += random.uniform(-0.01, 0.01)
    rtn[1] += random.uniform(-0.01, 0.01)
  else:
    changeradius = random.uniform(-0.001, 0.001)
    changeheight = -changeradius * (rtn[1]/rtn[0]) + random.uniform(-0.0001, 0.0001)
    rtn[0] = rtn[0] + changeradius;
    rtn[1] = rtn[1] + changeheight;

  return rtn

#print a solution
def output(genome):
  print("radius and height: "+ str(genome))
  print("score: " + str(evaluate(genome)))
  print("the ratio between radius and height is: " + str(genome[1]/genome[0]))
  print("---------")
  

#evaluate a solution to compare it to other solutions
def evaluate(genome):
  if calculate_surface_area(genome) > math.pi:
    return 0
  else:
    return calculate_volume(genome)


#genome[0] is the radius, genome[1] is the height
def calculate_surface_area(genome):
  return math.pi*genome[0]*(genome[0]+math.hypot(genome[0], genome[1]))

#genome[0] is the radius, genome[1] is the height
def calculate_volume(genome):
  return math.pi*(genome[0]*genome[0]*genome[1])/3


#run the algorithm
habitat.run(init, mutate, output, evaluate)

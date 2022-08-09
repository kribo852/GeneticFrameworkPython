import habitat
import random

def init():
  return [random.randrange(1, 25), random.randrange(1, 25)]

def mutate(genome):
  a=genome[0]
  b=genome[1]
  if bool(random.getrandbits(1)):
    a+=1
  else:
    a-=1
  if bool(random.getrandbits(1)):
    b+=1
  else:
    b-=1
  return [a, b]

def output(genome):
  print(genome[0])
  print(genome[1])
  print(genome[0]*genome[1])

def evaluate(genome):
  if genome[0]+genome[1]>100:
    return 0
  else:
    return genome[0] * genome[1]



habitat.run(init, mutate, output, evaluate)

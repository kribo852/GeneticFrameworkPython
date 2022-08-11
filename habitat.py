import random
import time


class NotImplementedException(Exception):
    pass

def combine_not_implemented(genome1, genome2):
  raise NotImplementedException()

def get_new_specimen(habitat, mutate, combine_specimen):
  if bool(random.getrandbits(1)):
    try:
      return combine_specimen(habitat[random.randrange(len(habitat))], habitat[random.randrange(len(habitat))]) 
    except NotImplementedException:
      return mutate(habitat[random.randrange(len(habitat))]) 
  else:
    return mutate(habitat[random.randrange(len(habitat))])


#runs evolutionary process
#if a stop condition is given the process returns a result specimen organism
# genome G then
# init() -> G
# mutate(G) -> G
# output(G) -> ()
# evaluate(G) -> number
# combine_specimen(G, G) -> G 
# stop_condition(G) -> bool
def run(initiate, mutate, output, evaluate, combine_specimen=combine_not_implemented, stop_condition= lambda genome: False):
  habitat = [initiate(), initiate(), initiate(), initiate(), initiate()]
  scores = []
  for specimen in habitat:
    scores.append(evaluate(specimen))
  iterationstart = time.time()
  iterations = 0
  while not stop_condition(habitat[0]):
    if time.time() - iterationstart >= 15:
      output(habitat[0])
      iterationstart = time.time()
      print("no. of iterations {}".format(iterations))
      iterations = 0
    else:
      iterations+=1
      testorganism = get_new_specimen(habitat, mutate, combine_specimen)
      newscore=evaluate(testorganism)
      for i in range(len(habitat)):
        if newscore > scores[i]:
          habitat[i]=testorganism
          scores[i]=newscore
          break
  return habitat[0]


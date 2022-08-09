import random
import time

def run(initiate, mutate, output, evaluate):
  habitat = [initiate(), initiate(), initiate(), initiate(), initiate()]
  scores = []
  for specimen in habitat:
    scores.append(evaluate(specimen))
  iterationstart = time.time()
  iterations = 0
  while True:
    if time.time() - iterationstart >= 15:
      output(habitat[0])
      iterationstart = time.time()
      print("no. of iterations {}".format(iterations))
      iterations = 0
    else:
      iterations+=1
      testorganism = mutate(habitat[random.randrange(len(habitat))])
      newscore=evaluate(testorganism)
      for i in range(len(habitat)):
        if newscore > scores[i]:
          habitat[i]=testorganism
          scores[i]=newscore
          break



# GeneticFramworkPython

A small and simple library for running genetic algorithms, in Python.

## Examples
The following examples are included
| Name | filename | Link to description of the problem |
|------|----------|------------------------------------| 
| Optimize volume of a cylinder | example_maximize_cylinder_volume.py ||
| Optimize volume of a cone | example_maximize_cone_volume.py ||
| Combine resistors into a network with the wanted resistance | example_resistors.py ||
| Eight queens problem | example_eight_queens_problem.py | https://en.wikipedia.org/wiki/Eight_queens_puzzle |

Use it by calling the run function in habitat.py, with the user specified function objects, for manipulating the genome.

## API

```Python
#runs evolutionary process
#if a stop condition is given the process returns a result specimen organism
# genome G then
# init() -> G
# mutate(G) -> G
# output(G) -> ()
# evaluate(G) -> number the fitness function, gives back a score so that two genomes can be compaired
# combine_specimen(G, G) -> G 
# stop_condition(G) -> bool the default implementation runs indefinately
def run(initiate, mutate, output, evaluate, combine_specimen=combine_not_implemented, stop_condition= lambda genome: False):
```

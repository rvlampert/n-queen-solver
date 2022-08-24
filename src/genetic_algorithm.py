from datetime import datetime
import random
import math
import yaml
import os
from src.utils import plot_values, print_solution

CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(""), "config.yaml"))
with open(CONFIG_PATH, 'r') as stream:
    config = yaml.safe_load(stream)

# N = config["board_size"]
N = 0
g = config["generations"]
n = config["individuals"]
k = config["tournament_size"]
m = config["mutation_probability"]
e = config["elitism"]

NEGATIVE_INF = -math.inf
POSITIVE_INF = math.inf

def get_values_generation(population):
  min_value = POSITIVE_INF
  max_value = NEGATIVE_INF
  total = 0
  for individual in population:
    conflicts = evaluate(individual)
    min_value = min(min_value,conflicts)
    max_value = max(max_value,conflicts)
    total+=conflicts
  average_value = total/len(population)
  return int(min_value),int(max_value),average_value

def partial_population(population,n):
  new_population = []
  for _ in range(n):
    new_population.append(population[random.randint(0,len(population)-1)])
  return new_population

def random_population(n):
  population = []
  for _ in range(n):
    individual = []
    for _ in range(N):
      individual.append(random.randint(1,N))
    population.append(individual)
  return population

def crossover(parent1,parent2,index):
  child1 = parent1[:index]
  child1.extend(parent2[index:])
  child2 = parent2[:index]
  child2.extend(parent1[index:])
  return child1, child2

def mutate(individual,m):
  if random.random() < m:
    index = random.randint(0,N-1)
    individual[index] = random.randint(1,N)
  return individual

def tournament(participants):
  best_individual = participants[0]
  best_score = evaluate(participants[0])
  for individual in participants[1:]:
    if evaluate(individual) < best_score:
      best_individual = individual
  return best_individual

def evaluate(individual):
  conflicts = 0
  for index, element in enumerate(individual):
    conflicts += get_conflicts(individual,index)
  return conflicts

def get_conflicts(individual,index):
  current = individual[index]
  conflicts = 0
  variation = 1
  for element in range(index+1,N):
    if individual[element] == current:
      conflicts += 1
    if individual[element] == current+variation:
      conflicts += 1
    if individual[element] == current-variation:
      conflicts += 1
    variation+=1      
  return conflicts


def run(input_n):
    global N
    N = int(input_n)
    print("="*60)
    print("Running genetic algorithm...")
    t1 = datetime.now()
    min_values=[]
    max_values=[]
    average_values=[]

    population = random_population(n)

    min_value, max_value, average_value = get_values_generation(population)
    min_values.append(min_value)
    max_values.append(max_value)
    average_values.append(average_value)

    for generation in range(g):

        new_population = []
        if e:
            new_population.append(tournament(population))
        while len(new_population) < n:
            parent1 = tournament(partial_population(population,k))
            parent2 = tournament(partial_population(population,k))
            # child1,child2 = crossover(parent1,parent2,4)
            child1,child2 = crossover(parent1,parent2,random.randint(0,N-1))
            child1 = mutate(child1,m)
            child2 = mutate(child2,m)
            new_population.append(child1)
            if len(new_population) < n:
                new_population.append(child2)
        population = new_population

        min_value, max_value, average_value = get_values_generation(population)
        min_values.append(min_value)
        max_values.append(max_value)
        average_values.append(average_value)

    solution = tournament(population)
    t2 = datetime.now()
    time = t2-t1
    print_solution(solution, time, N)
    input("press enter to plot the metrics")
    plot_values(min_values,max_values,average_values)
    return tournament(population) 
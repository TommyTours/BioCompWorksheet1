import random


class Individual:
    gene = []
    fitness = 0


population = []
number_of_genes = 10
population_size = 50

for x in range(0, population_size):
    tempGene = []
    for y in range(0, number_of_genes):
        tempGene.append(random.randint(0, 1))
    newInd = Individual()
    newInd.gene = tempGene.copy()
    population.append(newInd)

original_total_fitness = 0

for x in range(0, population_size):
    for i in range(0, number_of_genes):
        if population[x].gene[i] == 1:
            population[x].fitness += 1
    original_total_fitness += population[x].fitness

print("Original fitness : " + str(original_total_fitness))
print("Average fitness : " + str(original_total_fitness / population_size))

offspring = []
offspring_total_fitness = 0

for i in range(0, population_size):
    parent1 = random.randint(0, population_size - 1)
    off1 = population[parent1]
    parent2 = random.randint(0, population_size - 1)
    off2 = population[parent2]
    if off1.fitness > off2.fitness:
        offspring.append(off1)
        offspring_total_fitness += off1.fitness
    else:
        offspring.append(off2)
        offspring_total_fitness += off2.fitness


print("Offspring fitness : " + str(offspring_total_fitness))
print("Average offspring fitness : " + str(offspring_total_fitness / (population_size)))
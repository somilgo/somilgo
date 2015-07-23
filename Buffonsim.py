__author__ = 'Govani'
import random
from math import *


rep = 0
rep = int(rep)
piave = 0
piave = int(piave)
#Input values
while True:
    length = input("length of each needle >> ")

    try:
        length = float(length)
        break
    except ValueError:
        print("\n")
        print("Please input a valid number")
        print("\n")
        continue

while True:
    dist = input("distance between each line >> ")

    try:
        dist = float(dist)
        break
    except ValueError:
        print("\n")
        print("Please input a valid number")
        print("\n")
        continue

while True:
    quant = input("number of needles per trial >> ")

    try:
        quant = int(quant)
        break
    except ValueError:
        print("\n")
        print("Please input a valid integer")
        print("\n")
        continue

while True:
    trials = input("number of trials >> ")

    try:
        trials = int(trials)
        break
    except ValueError:
        print("\n")
        print("Please input a valid integer")
        print("\n")
        continue


#Find theoretical probability
prob = (2.0 * length) / (dist * 3.14159265359)

#Round theoretical probability and make it into an integer
rprob = int(round(prob, 5) * 100000)


#Implement random integer for experimental probability
for y in range(0, trials):
    cross = 0
    cross = int(cross)
    rep += 1

    if y == trials:
        break
    else:
        for x in range(0, quant+1):
            if x == quant:
                pi = (2 * length * quant) / (dist * cross)
                if rep == 1:
                    piave = piave + pi
                else:
                    piave = (piave * (rep - 1) + pi) / rep
                    continue
            else:
                eprob = random.randint(0, 100000)

                if eprob <= rprob:
                    cross += 1





#result
print("Average of " + str(trials) + " Pi Approximation(s): " + str(piave))
input("Press ENTER to exit")
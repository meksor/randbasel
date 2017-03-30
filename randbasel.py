import random
import fractions
import math
import sys


max_random = (256**3)
max_iterations = (256**3)

def get_random_pair():
    a, b = random.randint(0, max_random), random.randint(0, max_random)
    return a, b

def get_pi(count, iter):
    c = count / iter
    pi = math.sqrt(6/c)
    return pi

def approx_pi():
    count = 0
    lowest_error = 256
    best_pi = 0

    for i in range(1, max_iterations):
        if (fractions.gcd(*get_random_pair()) == 1):
            count += 1
        if (count > 0):
            d = get_pi(count, i)
            err = abs(d - math.pi)
            print("[" + str(i) + "/" + str(max_iterations) + "] Pi / Error: " + str(d) + " / " + str(err))
            if (0 < err < lowest_error):
                lowest_error = err
                best_pi = d

    accuracy = (lowest_error / math.pi) * 100
    rnd_acc = accuracy
    print("--------------------------------------------------------------")
    print("Aproximated PI: " + str(best_pi))
    print("------ math.pi: " + str(math.pi))

    print("\nAccuracy: " + str(rnd_acc) + "% " + " Lowest Error: " + str(lowest_error))
    print("--------------------------------------------------------------")

approx_pi()

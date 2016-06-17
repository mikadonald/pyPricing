import sys
import random as rd
from scipy.stats import norm

def random_walk(steps):
    	step = 0
    	routine = []
    	location = 0
    	currentstep = 0

    	if (steps >0):
    		routine.append(0)
    	else:
            sys.exit("Error message! Steps should be a positive integer!")

    	while (currentstep < steps):
    		location += rd.randint(-1, 1)
    		routine.append(location)
    		currentstep += 1

    	return routine


def brownian_motion(steps, dt, delta):
        step = 0
        routine = []
        location = 0
        currentstep = 0

        if (steps >0):
            routine.append(0)
        else:
            sys.exit("Error message! Steps should be a positive integer!")

        while (currentstep < steps):
            location += norm.rvs(scale=delta**2*dt)
            routine.append(location)
            currentstep += 1

        return routine





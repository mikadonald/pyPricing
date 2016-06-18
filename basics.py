import sys
import random as rd
from scipy.stats import norm
import numpy as np

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
            location += norm.rvs(scale=delta*np.sqrt(dt))
            routine.append(location)
            currentstep += 1

        return routine

def geometric_brownian_motion(steps, dt, mu, delta, starting_point):
        step = 0
        routine = []
        location = 0
        currentstep = 0
        t = dt 

        if (steps >0):
            routine.append(0)
        else:
            sys.exit("Error message! Steps should be a positive integer!")

        while (currentstep < steps):
            location = starting_point * np.exp((mu - 0.5 * delta ** 2) * t + norm.rvs(scale=delta*np.sqrt(t)))
            routine.append(location)
            currentstep += 1
            t += dt

        return routine




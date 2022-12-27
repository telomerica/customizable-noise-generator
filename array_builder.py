import numpy as np
import random
from perlin_noise import PerlinNoise
from img_map import *


def sigmoid_(array,float=False):
    return 1 / (1+np.exp(-array))

def bias_(array,bias,float=False):
    return array+bias

def random_(array,probability,choice,float=False):
    iter = int((array.shape[0]*array.shape[1])*probability)

    for i in range(iter):
        if choice == "rnd":
            choice=random.random()
        array[random.randrange(0,array.shape[0]-1)][random.randrange(0,array.shape[1]-1)]=choice
    return array


def perlin_(array,octaves,seed,object,bias=0,float=False):
    grid = array.shape
    perlin = PerlinNoise(octaves=octaves, seed=seed)
    temp = ([[perlin([_/grid[0], __/grid[1]]) for __ in range(grid[0])] for _ in range(grid[1])])
    temp = np.array(temp)+bias
    
    if float==False:
        temp = (np.rint(sigmoid_(temp))).astype(int)
        temp_w = np.where(temp==1)
        for x in range(len(temp_w[0])):
            array[temp_w[0][x]][temp_w[1][x]] = object
    else:
        array = array+temp
    return array

def array_build(grid,functionslist,float=False):
    print(float)
    mappe = np.zeros(grid)

    dict_of_functions={"random":random_,"perlin":perlin_,"sigmoid":sigmoid_,"bias":bias_}

    for fc in functionslist:
        function = dict_of_functions.get(fc[0])
        mappe = function(mappe,*fc[1],float) 

    return mappe
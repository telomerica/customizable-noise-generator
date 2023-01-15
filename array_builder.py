import numpy as np
import random
from perlin_noise import PerlinNoise

def array_builder(map_array, steps):
    temp_array = map_array
    for step in steps:
        temp_array=step["method"](temp_array,**step["args"])
    return temp_array

def sigmoid_(array,num,float=True):
    return num / (1+np.exp(-array))

def bias_(array,bias,float=False):
    return array+bias

def random_(array,probability,float=False):
    x = array
    for row in x:
        coords = np.random.randint(0,len(row),size=(int(len(row)*probability)))
        r = np.random.rand(*row.shape)
        row[coords] = r[coords]
        #print(row)
    return x

def perlins(howmany,float_):
    u = []
    for i in range(howmany):
        octave_random = random.choice([1,3,7,15])
        seed_random = random.randint(0,100)
        object_random = random.choice([0,1,2])
        bias_random = random.choice([0.15,0.1,0,-0.1,-0.2,-0.3,-0.4,-0.5])
        float_ = float_
        
        u.append({"method":perlin_,"args":{"octaves":octave_random,"seed":seed_random,"object":object_random,
        "bias":bias_random,"float":float_}})
    return u

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

def convert_float_to_int(array,segments):
    max=np.max(array)
    min=np.min(array)
    
    difference=max-min #60
    step = difference/segments #25

    for i in range(segments):
        array[array>max+(step*i)]=i
        array[array<min+(step*i)]=i
    return array
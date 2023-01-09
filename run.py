from array_builder import *
from img_map import *
from convoluter import *
import numpy as np
import os

def perlins(howmany):
    u = []
    for i in range(howmany):
        octave_random = random.choice([3,7,15])
        seed_random = random.randint(0,100)
        object_random = random.choice([0,1,2,3])
        bias_random = random.choice([0.1,0,-0.1,-0.2,-0.25])
        float_ = False

        u.append({"method":perlin_,"args":{"octaves":octave_random,"seed":seed_random,"object":object_random,
        "bias":bias_random,"float":float_}})
    return u

camos = [{0:(100,115,90),1:(130,130,108),2:(90,60,60),3:(200,200,200)}, #multicam
        {0:(80,70,51),1:(110,100,70),2:(90,60,45),3:(50,60,50)}, #flecktarn
        {0:(240,180,90),1:(210,60,50),2:(110,100,50),3:(50,60,50)}, #alpenflage
        {0:(220,200,190),1:(100,100,90),2:(170,160,150),3:(60,55,50)}, #tundra
        {0:(210,210,160),1:(90,140,80),2:(100,70,70),3:(50,60,50)}, #tropentarn
        {0:(120,140,105),1:(65,80,60),2:(50,60,50),3:(170,135,100)} #ratnik
    ]

for i in range(50):
    perlins_l = perlins(4)
    settings_l = [perlins_l]

    array = (array_builder(
        map_array=np.ones((500,500)),
        steps=[ 
    *perlins_l
    ]
    ))

    for camo in camos:
        save_map(array,color_dict=camo,draw=True,float=False,settings=settings_l)




    print(i)
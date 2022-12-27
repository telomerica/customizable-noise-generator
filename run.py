from array_builder import *
from img_map import *
import numpy as np

for x in range(30):
    mappe = array_build((900,900),[

        ["perlin",(random.choice([3,5,10]),random.randint(0,1000),random.random(),random.choice([-0.1,-0.2,-0.3]))],
        ["random",(random.choice([0.1,0.12,0.14]),random.random())],
        ],
        float = True)
            
    save_map(mappe,color_dict = None,float=True)
    print("step",x) 




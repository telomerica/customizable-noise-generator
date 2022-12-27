from array_builder import *
from img_map import *
import numpy as np

for x in range(30):
    mappe = array_build((750,750),[
        
        ["perlin",(random.choice([1,2]),random.randint(0,1000),random.random(),random.choice([0.4,0.2,-0.2,-0.4]))],
        ["perlin",(random.choice([3,5,10]),random.randint(0,1000),random.random(),random.choice([0.1,0.2,0.3,0,0,-0.1,-0.2,-0.3]))],
        ["random",(random.choice([0.02,0.05,0.1,0.12,0.14]),"rnd")],
        ],
        float = True)
            
    save_map(mappe,color_dict = None,float=True)
    print("step",x) 



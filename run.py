from array_builder import *
from img_map import *
from convoluter import *
import numpy as np
import os

def map_construct(amount,scale,borders,float_,value_sigmoid):
    for i in range(amount):
        print("GENERATED",i)
        perlins_l = perlins(random.randrange(2,10),float_=float_) #all of this needs to be added to the array builder`s methods
        

        value=value_sigmoid #maximum value to be sigmoided in

        map_array=np.zeros((100*scale,100*scale))
        
        steps = [*perlins_l,
            {"method":bias_,"args":{"bias":-200,"values":(225,275)}},
            {"method":sigmoid_,"args":{"num":value,"float":True}},
            {"method":convert_float_to_int,"args":{"segments":[45,50,115,150,9999999,999999999]}}
        ]
        settings_l = steps
        
        array = (array_builder(map_array,steps=steps
            ))
        
        max=np.max(array)
        min=np.min(array)
    
        print("max",max)
        print("min",min)

        if borders==True:
            grid = array.shape
            x = grid[0]+70
            y = grid[1]+70
            border = np.full((x,y),4)
            border[35:-35,35:-35] = array
            array = border

        
        save_map(array,color_dict=None,draw=True,float=False,settings=settings_l,value=value)

            #map drawing needs a smear mode for floats where the average of the 
            #nearest two integers` rgb values are taken, 
            # so 1:(100,100,100). 2:(200:200:200) -> a float of 1.5 has the value 150,150,150

map_construct(amount = 10, scale = 5,borders=True,float_=True,value_sigmoid=5)
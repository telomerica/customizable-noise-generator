from array_builder import *
from img_map import *
from convoluter import *
import numpy as np
import os

def map_construct(amount,scale,borders,float_,value_sigmoid):
    for i in range(amount):
        print("GENERATED",i)
        perlins_l = perlins(random.randrange(1,4),float_=float_) #all of this needs to be added to the array builder`s methods
        settings_l = [("scale:",scale),perlins_l]

        value=value_sigmoid #maximum value to be sigmoided in

        map_array=np.zeros((100*scale,100*scale))
        
        array = (array_builder(map_array,steps=[
            *perlins_l,
            {"method":sigmoid_,"args":{"num":value,"float":True}},
            {"method":convert_float_to_int,"args":{"segments":3}}

        ]))
        if borders==True:
            grid = array.shape
            x = grid[0]+70
            y = grid[1]+70
            border = np.full((x,y),3)
            border[35:-35,35:-35] = array
            array = border
        


        
        save_map(array,color_dict=None,draw=True,float=float_,settings=settings_l,value=value)

            #map drawing needs a smear mode for floats where the average of the 
            #nearest two integers` rgb values are taken, 
            # so 1:(100,100,100). 2:(200:200:200) -> a float of 1.5 has the value 150,150,150

map_construct(amount = 10, scale = 5,borders=False,float_=True,value_sigmoid=5)
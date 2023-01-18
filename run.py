from array_builder import *
from img_map import *
from convoluter import *
import numpy as np
import os

def map_construct(amount,scale,float_,value_sigmoid):
    for i in range(amount):
        print("GENERATED",i)
        perlins_l = perlins(random.randrange(2,10),float_=float_) #all of this needs to be added to the array builder`s methods
        value=value_sigmoid #maximum value to be sigmoided in

        map_array=np.zeros((100*scale,100*scale))
        
        settings_l0 = [*perlins_l,
            {"method":bias_,"args":{"bias":-200,"values":(225,275)}},
            {"method":sigmoid_,"args":{"num":value,"float":True}},
        ]
        
        settings_l1 = [*settings_l0,
        {"method":convert_float_to_int,"args":{"segments":[45,50,115,150,9999999,999999999]}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array1 = (array_builder(map_array,steps=settings_l1))
        save_map(array1,color_dict=None,draw=True,float=False,settings=settings_l1,value=value)

        settings_l2 = [*settings_l0,
        {"method":bias_,"args":{"bias":-2}},
        {"method":sigmoid_,"args":{"num":value,"float":True}},
        {"method":convert_float_to_int,"args":{"segments":[45,50,115,150,9999999,999999999]}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array2 = (array_builder(map_array,steps=settings_l2))
        save_map(array2,color_dict=None,draw=True,float=False,settings=settings_l2,value=value,extend="a")

        settings_l3 = [*settings_l0,
        {"method":bias_,"args":{"bias":2}},
        {"method":sigmoid_,"args":{"num":value,"float":True}},
        {"method":convert_float_to_int,"args":{"segments":[45,50,115,150,9999999,999999999]}},
        {"method":border,"args":{"bordersize":70,"object":4}}
        ]
        array3 = (array_builder(map_array,steps=settings_l3))
        save_map(array3,color_dict=None,draw=True,float=False,settings=settings_l3,value=value,extend="b")


        #map drawing needs a smear mode for floats where the average of the 
        #nearest two integers` rgb values are taken, 
        # so 1:(100,100,100). 2:(200:200:200) -> a float of 1.5 has the value 150,150,150

map_construct(amount = 10, scale = 5,borders=True,float_=True,value_sigmoid=5)
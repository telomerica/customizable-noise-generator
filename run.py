from array_builder import *
from img_map import *
import numpy as np

for i in range(100):
    array = (array_builder(
        map_array=np.zeros((750,750)),
        steps=[
    #{"method":bias_,"args":{"bias":0.1,"float":True}},
    {"method":perlin_,"args":{"octaves":random.choice([3,5,10]),"seed":random.randint(0,100),"object":1,
    "bias":random.choice([0,-0.1,-0.2,-0.25]),"float":True}},
    {"method":perlin_,"args":{"octaves":random.choice([10,20,30]),"seed":random.randint(0,100),"object":1,
    "bias":random.choice([0,-0.2,-0.4,-0.5]),"float":True}},
    {"method":random_,"args":{"probability":random.choice(0.5,0.1,0.15,0.2),"float":True}},

    ]
    ))

    #img=draw_map(array,color_dict=False,float=True)
    #img.show()

    save_map(array,color_dict=None,draw=True,float=True)
    print(i)
from array_builder import *
from img_map import *
import numpy as np

array = (array_builder(
    map_array=np.zeros((750,750)),
    steps=[
#{"method":bias_,"args":{"bias":0.1,"float":False}},
{"method":perlin_,"args":{"octaves":random.choice([3,5,10]),"seed":random.randint(0,100),"object":1,
"bias":random.choice([-0.1,-0.2,-0.3,0.1,0.2,0.3]),"float":True}},
{"method":perlin_,"args":{"octaves":random.choice([10,20,30]),"seed":random.randint(0,100),"object":0,
"bias":random.choice([-0.3,-0.5,-0.6,0.3,0.5,0.6]),"float":True}},
#{"method":sigmoid_,"args":{"float":False}},
{"method":random_,"args":{"probability":0.1,"choice":"rnd","float":True}}
]
))

print(array)
img=draw_map(array,color_dict=False,float=True)
img.show()

#["perlin",(random.choice([3,5,10]),random.randint(0,1000),random.random(),random.choice([-0.1,-0.2,-0.3]))],
#["random",(random.choice([0.1,0.12,0.14]),random.random())],

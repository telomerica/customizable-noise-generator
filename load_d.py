import numpy as np
import os
from array_builder import *
from img_map import *

ls = (os.listdir("saved_arrays"))[1:]
chosen = random.choice(ls)
mappe = np.load(f'{os.getcwd()}/saved_arrays/{chosen}',allow_pickle=True)

print(mappe)
print(chosen)
draw_map(mappe,color_dict=False,float=True).show()
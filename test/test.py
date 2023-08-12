# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:50:18 2023

@author: Jonathan
"""

import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,1, figsize=(20, 8))


data = [[0, 1, 2, 3], [4, 3, 2, 1]]
data[1] = np.linspace(0, 1, 4)

im = axes.imshow(data)
    
    

plt.show()
print(data)



for i in range(20):
    input()
    print(i)
    
    data2 = data
    data2[1] = np.linspace(0, i, 4)
    im.set_data(data2)
    
    print(data2)
    
    #fig.canvas.draw()
    #fig.canvas.flush_events()
    fig.canvas.draw()
    fig.show()
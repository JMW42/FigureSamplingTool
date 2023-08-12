# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:08:44 2023

@author: Jonathan
"""

import numpy as np
import matplotlib.pyplot as plt 
import time
dat = np.random.rand(100,10)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

init = np.random.rand(10,10)
print(init)
image = ax.imshow(init)
fig.canvas.draw()
count = 0
while count < 100:
    print(count)
    image.set_data(dat[count:count+10])
    fig.canvas.draw()
    count += 10
    time.sleep(1)
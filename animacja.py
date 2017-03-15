# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 10:39:44 2017

@author: student
"""

import imageio
import os
import fnmatch

image_path = os.listdir('.')
images = []

for f in image_path:
    if fnmatch.fnmatch(f, '*.BMP'):
        print(f)
        images.append(imageio.imread(f))


#images = []
#for filename in filenames:
#    images.append(imageio.imread(filename))
    
    
imageio.mimsave(os.path.join(os.getcwd(), "animacja.gif"), images)
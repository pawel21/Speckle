# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 11:32:41 2017

@author: student
"""

import matplotlib
import matplotlib.pyplot as plt

from skimage import io

photo = io.imread("1T03610U.BMP")

#plt.imshow(photo, cmap=plt.cm.gray)

plt.hist(photo.ravel(), bins=256)
plt.show()
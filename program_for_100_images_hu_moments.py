# -*- coding: utf-8 -*-
"""Program for 100 images Hu Moments.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11p_c7948ViOLUZBJCZVeLvQEZT1_lHXx
"""

import cv2
import pandas as pd
import numpy as np
import os
import math

def calculate_hu_moments(image_path):
    im = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    _,im = cv2.threshold(im, 80, 255, cv2.THRESH_BINARY)
    moments = cv2.moments(im)
    hu_moments = cv2.HuMoments(moments)
    for i in range(0,7):
      hu_moments[i] = -1* math.copysign(1.0, hu_moments[i]) * math.log10(abs(hu_moments[i]))
    hu_moments = np.ravel(hu_moments)
    return hu_moments

hu_moments_list = []
file_names = []

for i in range(1, 101):
    image_path =os.path.abspath(f"/content/Flower_Images/00{i}.png")
    hu_moments = calculate_hu_moments(image_path)
    hu_moments_list.append(hu_moments)
    file_names.append(f"00{i}.png")

df = pd.DataFrame(hu_moments_list, columns=['Hu Moment 1', 'Hu Moment 2', 'Hu Moment 3', 'Hu Moment 4', 'Hu Moment 5', 'Hu Moment 6', 'Hu Moment 7'])
df.insert(0, "File Name", file_names)

df.to_excel('/content/Hu_moments_100Flowers.xlsx', index=False)
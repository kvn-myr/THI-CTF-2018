#!/usr/bin/python

import sys
import numpy as np
import cv2
import random

img = cv2.imread(sys.argv[1])

random.seed("random")

h = img.shape[0]
w = img.shape[1]

img_out = np.zeros((h, w, 3), np.uint8)

for y in range(0, h):
	for x in range(0, w):
		img_out[y, x] = (img[y, x] - random.randrange(0, 256)) % 256

cv2.imwrite(sys.argv[2], img_out)

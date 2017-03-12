#!/usr/bin/env python
# Test of mapping depth to video using calibkinect, which doesn't seem to work
import numpy as np
import freenect, calibkinect
import matplotlib.pyplot as plt

depth = freenect.sync_get_depth()[0]
video = freenect.sync_get_video()[0]

depth = np.where(depth == 2047, 0, depth)

_, uv = calibkinect.depth2xyzuv(depth)
mapping = uv.astype(np.dtype('int16')).reshape(480, 640, 2)
mapped = np.zeros((480, 640, 3), np.dtype('uint8'))

for i, row in enumerate(mapping):
    for j, point in enumerate(row):
        mapped[i, j] = video[point[0], point[1]]

plt.figure(1)
plt.imshow(depth, cmap=plt.cm.gray)
plt.figure(2)
plt.imshow(mapped)
plt.figure(3)
plt.imshow(video)
plt.show()

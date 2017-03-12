#!/usr/bin/env python
import sys, time
import numpy as np
from scipy import ndimage, misc
import matplotlib.pyplot as plt

start = time.time()
base = misc.imread(sys.argv[1]).astype(np.dtype('int16'))[::2, ::2]
new = misc.imread(sys.argv[2]).astype(np.dtype('int16'))[::2, ::2]
print "Import: " + str(time.time() - start)
diff = -(new - base)  # Negative because presence of object reduces values
print "Diff: " + str(time.time() - start)

mask = np.logical_and(diff > 5, np.logical_and(base != 255, new != 255))
print "Mask: " + str(time.time() - start)

opened = ndimage.binary_opening(mask, iterations=3)
filled = ndimage.binary_fill_holes(opened)
print "Filter 1: " + str(time.time() - start)

revfiltered = ndimage.binary_opening(ndimage.binary_fill_holes(mask), iterations=3)
print "Filter 2: " + str(time.time() - start)

plt.figure(1)
plt.imshow(mask, cmap=plt.cm.gray)
plt.figure(2)
plt.imshow(filled, cmap=plt.cm.gray)
plt.figure(3)
plt.imshow(revfiltered, cmap=plt.cm.gray)
print "Prepare display: " + str(time.time() - start)
plt.show()

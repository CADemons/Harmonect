#!/usr/bin/env python
import sys
import numpy as np
from scipy import misc

depth = np.loadtxt(sys.argv[1], dtype=np.dtype('u1'), delimiter=',')
misc.imsave(sys.argv[1][:-4] + ".png", depth)

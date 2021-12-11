import numpy as np
from scipy import ndimage
from input import data

current = data.copy()
totalFlashes = 0
KERNEL = np.asarray([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
for i in range(100):
    current += 1
    flashed = np.full(current.shape, False, dtype=bool)
    justFlashed = (current > 9) & ~flashed
    while (justFlashed.any()):
        flashed |= justFlashed

        inc = ndimage.convolve(
            justFlashed.astype(int),
            KERNEL,
            mode='constant',
            cval=0
        )

        current += inc

        justFlashed = (current > 9) & ~flashed
    current[flashed] = 0
    totalFlashes += flashed.sum()
print("end levels")
print(current)
print("totalFlashes:")
print(totalFlashes)

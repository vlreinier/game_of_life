import numpy as np

h = 10
w = 10
arr = np.random.binomial(1, 0.9, h * w).reshape(h, w)

print(arr)
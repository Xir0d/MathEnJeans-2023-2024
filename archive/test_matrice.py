import numpy as np

clous = 9
height = 5
width = 5

motif = {}

for i in range(clous):
    for j in range(clous):
        if i < j:
            motif[i,j] = np.zeros((height,width))
            for m in range(width):
                for n in range(height):
                    motif[i,j][(m,n)] = motif[i,j][(m,n)] + 1

print(motif[1,3])
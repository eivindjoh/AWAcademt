import numpy as np

test1 = [[1, 0, 0, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
index = [[0, 3], [0, 1, 3], [1, 2]]

x = []
y = []
for count, v in enumerate(test1):
    for i in index[count]:
        z = np.zeros(len(v))
        z[i] = 1
        y.append(list(z))
        x.append(v)

print(len(x))
print(len(y))



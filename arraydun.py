import numpy as np

a = np.array([1,23,47])
filear = ([])

for i in a:
    if i>23:
        filear.append(True)
    else:
        filear.append(False)

new = a[filear]
print(filear)
print(new)

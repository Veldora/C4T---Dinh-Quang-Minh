import math

def _arrays(x):

    y = []
    z = []

    sum_z = 0
    for i in range(len(x)):
        y.append(math.pi/2 - x[i])
        z.append(math.cos(x[i]) - math.sin(x[i]))
        sum_z += z[i]

    return sum_z


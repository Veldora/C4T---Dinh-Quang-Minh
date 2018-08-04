import numpy as np
import matplotlib.pyplot as plt
import math

x1 = np.random.randint(0, 50, size=50)
x2 = np.random.randint(50, 100, size=50)
x = np.zeros((1, 100))
x[0, 0:50] = x1
x[0, 50:100] = x2
# print(x)

y1 = np.random.randint(0, 50, size=50)
y2 = np.random.randint(50, 100, size=50)
y = np.zeros((1, 100))
y[0, 0:50] = y1
y[0, 50:100] = y2
# print(y)


def euclid_dist(a, b):
    delta_x = a[0] - b[0]
    delta_y = a[1] - b[1]
    dist = math.sqrt(delta_x**2 + delta_y**2)
    return dist


c1 = np.random.randint(1, 100, size=2)
c2 = np.random.randint(1, 100, size=2)
# print(c1, c2)
epsilon = 5
while True:
    c1_array = []
    c2_array = []
    for i in range(100):
        dist1 = euclid_dist([x[0, i], y[0, i]], c1)
        dist2 = euclid_dist([x[0, i], y[0, i]], c2)
        if dist1 > dist2:
            c2_array.append([x[0, i], y[0, i]])
        if dist1 < dist2:
            c1_array.append([x[0, i], y[0, i]])
        if dist1 == dist2:
            c1_array.append([x[0, i], y[0, i]])
            c2_array.append([x[0, i], y[0, i]])

    c1_new = [0, 0]
    c2_new = [0, 0]
    for j in range(len(c1_array)):
        c1_new[0] += c1_array[j][0]/len(c1_array)
        c1_new[1] += c1_array[j][1]/len(c1_array)
    for j in range(len(c2_array)):
        c2_new[0] += c2_array[j][0]/len(c1_array)
        c2_new[1] += c2_array[j][1]/len(c1_array)

    if euclid_dist(c1, c1_new) + euclid_dist(c2, c2_new) < epsilon:
        break
    else:
        c1 = c1_new
        c2 = c2_new


for point in c1_array:
    plt.scatter(point[0], point[1], color="red")
for point in c2_array:
    plt.scatter(point[0], point[1], color="black")
plt.scatter(c1[0], c1[1], color="blue")
plt.scatter(c2[0], c2[1], color="green")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xticks([]), plt.yticks([])
plt.show()

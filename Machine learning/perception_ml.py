import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mtp

x1 = np.random.randint(0, 50, size=50)
x2 = np.random.randint(50, 100, size=50)
x = np.zeros((1, 100))
x[0, 0:50] = x1
x[0, 50:100] = x2

y1 = np.random.randint(0, 50, size=50)
y2 = np.random.randint(50, 100, size=50)
y = np.zeros((1, 100))
y[0, 0:50] = y1
y[0, 50:100] = y2


# Random initialize w and b
w = np.zeros((1, 2), dtype=np.float32)
b = 0

# label the data
# First array
P1 = []
L1 = []  # Label
for i in range(50):
    pi = [x1[i], y1[i]]
    P1.append(pi)
    L1.append(1)

P2 = []
L2 = []  # Label
for i in range(50):
    pi = [x1[i], y1[i]]
    P2.append(pi)
    L2.append(-1)


def multi_w_p(w, p):
    result = w[0] * p[0] + w[1] * p[1]
    return result


# Use harlim: If > 0 => set 1, else => set -1
def my_harlim(F):
    if F > 0:
        F = 1
    else:
        F = -1
    return F


def check_stop(w_new, b_new, P1, L1, P2, L2):
    FLAG_CHECK = False
    for index, i in enumerate(P1):
        result = multi_w_p(w_new, i)
        F = result + b_new
        a = my_harlim(F)
        # Calculate epsilon
        e1 = a - L1[index]
        if e1 != 0:
            FLAG_CHECK = True
            break
    if ~FLAG_CHECK:
        for index, i in enumerate(P2):
            result = multi_w_p(w_new, i)
            F = result + b_new
            a = my_harlim(F)
            # Calculate epsilon
            e2 = a - L2[index]
            if e2 != 0:
                FLAG_CHECK = True
                break
    if FLAG_CHECK:
        return True
    return False


while True:

    # Step 1
    # Loop through all points within P1
    for index, i in enumerate(P1):
        result = multi_w_p(w, i)
        F = result + b
        a = my_harlim(F)
        # Calculate epsilon
        e1 = a - L1[index]
        w_new = w + e1 * i

    # Step 2
    # Loop through all points within P2
    for index, i in enumerate(P2):
        result = multi_w_p(w, i)
        F = result + b
        a = my_harlim(F)
        # Calculate epsilon
        e2 = a - L2[index]
        w_new = w + e2 * i

    # Step 3
    # Conditional


plt.scatter([x1], [y1], color="red")
plt.scatter([x2], [y2], color="blue")
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xticks([]), plt.yticks([])
plt.show()
# ****mtp.lines.Lines2D()****

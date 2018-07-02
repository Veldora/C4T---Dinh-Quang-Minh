import cv2
import numpy as np

# Read Image
I = cv2.imread("E:\\AI files\\C4T_main_module\\anh.jpg")

# Resize Image
# I = cv2.resize(I, (320, 240))

# Create Window
# cv2.namedWindow("image", cv2.WINDOW_NORMAL)

# Convert RGB to gray
gray = cv2.cvtColor(I, cv2.COLOR_RGB2GRAY)

# Get Dimension
# for i in range(len(gray.shape)):
#     print("rows", gray.shape[i])

# mean filter
def mean_filter(gray, row, col):
    temp = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            temp += gray[row + j, col + i]
    return temp / 9

# median filter
def median_filter(gray, row, col):
    temp = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            temp.append(gray[row + j, col + i])
    sort_temp = sorted(temp)
    for value in range(len(temp)):
        if temp[value] == sort_temp[0] or temp[value] == sort_temp[-1]:
            temp[value] = sort_temp[int(len(sort_temp)/2)]
    return temp[int(len(temp)/2)]

gray_new_1 = gray.copy()
for col in range(1, gray.shape[1] - 1):
    for row in range(1, gray.shape[0] - 1):
        gray_new_1[row, col] = mean_filter(gray, row, col)

med_gray_new_1 = gray.copy()
for col in range(1, gray.shape[1] - 1):
    for row in range(1, gray.shape[0] - 1):
        med_gray_new_1[row, col] = median_filter(gray, row, col)

cv2.imshow("mean_filter", gray_new_1)
cv2.imshow("median_filter", med_gray_new_1)

cv2.waitKey(0)



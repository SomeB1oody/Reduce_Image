#Author: Stan Yin
#GitHub Name: SomeB1oody
#This project is based on CC 4.0 BY, please mention my name if you use it.
#This project requires opencv.
import cv2 as cv
import numpy as np
#ask for path of image
print("Please enter image location\t")
print("Example: C:\\Wallpaper\\02.png\t")
path = input("Enter HERE: ")
img = cv.imread(path, cv.IMREAD_COLOR)
#Determine if the read was successful
if img is None:
    raise ValueError("Could not open image\t")
#Setting Variables
row_number = img.shape[0]
col_number = img.shape[1]
#If the number of pixels is odd, one row/column is discarded
if img.shape[0] % 2 != 0: row_number -= 1
if img.shape[1] % 2 != 0: col_number -= 1
#Setting Variables
row_new = row_number // 2
col_new = col_number // 2

img_new = np.zeros((row_new, col_new, img.shape[2]), dtype=np.uint8)
#Reducing the amount of pixels by averaging over a two-by-two sector
for row in range(row_new):
    for col in range(col_new):
        symbol_row = row * 2
        symbol_col = col * 2
        sector = img[symbol_row:symbol_row + 2, symbol_col:symbol_col + 2]
        average_color = sector.mean(axis=(0,1)).astype(np.uint8)
        img_new[row, col] = average_color
#show
cv.namedWindow("small image")
cv.imshow("small image", img_new)
cv.waitKey(0)

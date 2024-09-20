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
sector_size_ = input("Please enter the size of a single pixel sector:")
sector_size = int(sector_size_)
#Determine if the read was successful
if img is None:
    raise ValueError("Could not open image\t")
if sector_size < 1:
    raise ValueError("\tsector size invalid\tSize is too small.")
if sector_size > img.shape[0] or sector_size > img.shape[1]:
    raise ValueError("\tsector size invalid\tSize is too big.")
#Setting Variables
row_number = img.shape[0]
col_number = img.shape[1]
#Croping Image
flag1 = True
flag2 = True
while flag1 and flag2:
    if row_number % sector_size != 0: row_number -= 1
    else: flag1 = False

    if col_number % 2 != 0: col_number -= 1
    else: flag2 = False
#Setting Variables
row_new = row_number // sector_size
col_new = col_number // sector_size
img_new = np.zeros((row_new, col_new, img.shape[2]), dtype=np.uint8)
#Reducing the amount of pixels by averaging over a two-by-two sector
for row in range(row_new):
    for col in range(col_new):
        symbol_row = row * sector_size
        symbol_col = col * sector_size
        sector = img[symbol_row:symbol_row + sector_size, symbol_col:symbol_col + sector_size]
        average_color = sector.mean(axis=(0,1)).astype(np.uint8)
        img_new[row, col] = average_color
#show
cv.namedWindow("Reduced Image")
cv.imshow("Reduced Image", img_new)
cv.waitKey(0)
cv.imwrite("Reduced_Image.jpg", img_new)

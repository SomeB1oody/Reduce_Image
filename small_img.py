import cv2 as cv
import numpy as np

print("Please enter image location")
print("Example: C:\\Wallpaper\\02.png")
path = input("Enter HERE: ")
img = cv.imread(path, cv.IMREAD_COLOR)

if img is None:
    raise ValueError("Could not open image")

row_number = img.shape[0]
col_number = img.shape[1]

if img.shape[0] % 2 != 0: row_number -= 1
if img.shape[1] % 2 != 0: col_number -= 1

row_new = row_number // 2
col_new = col_number // 2

img_new = np.zeros((row_new, col_new, img.shape[2]), dtype=np.uint8)

for row in range(row_new):
    for col in range(col_new):
        symbol_row = row * 2
        symbol_col = col * 2
        sector = img[symbol_row:symbol_row + 2, symbol_col:symbol_col + 2]
        average_color = sector.mean(axis=(0,1)).astype(np.uint8)
        img_new[row, col] = average_color

cv.namedWindow("small image")
cv.imshow("small image", img_new)
cv.waitKey(0)
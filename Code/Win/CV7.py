import numpy as np
import sys
import cv2

#image = cv2.imread("Iris.jpg")
image = cv2.imread("../New Folder/Resources/Iris.jpg")
height, width, v = image.shape
print height
print width
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#cv2.imwrite("../New Folder/Resources/image_grey.jpg",gray)
thresh = cv2.threshold(gray,130,255, cv2.THRESH_BINARY_INV)[1]

color = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
mask = np.zeros((height+2, width+2), np.uint8)

squares = []
for h in xrange(height):
    for w in xrange(width):
        if thresh[h, w]==0:
            a=cv2.floodFill(color, mask ,(w, h), (255, 0, 0))
            squares.append(a[1])

for coord in squares:
    x, y, w, h = coord
    if  w >20 or h >40:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0,0,255),thickness = 1,lineType=8)

cv2.imshow("Actual Image",image),cv2.waitKey(1)
cv2.imshow("Image_Gray",gray),cv2.waitKey(1)
cv2.imshow("Image_thresh",thresh),cv2.waitKey(1)
cv2.imshow("Image_Color",color),cv2.waitKey(1)
cv2.imshow("Image_Color",color),cv2.waitKey(1)
cv2.imshow("Image_Color",a),cv2.waitKey(1)


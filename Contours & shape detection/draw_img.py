import cv2
import numpy as np

img1 = np.zeros((300, 300), dtype="uint8")
img2 = np.zeros((300, 300), dtype="uint8")

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (100, 100), (250, 250), 255, -1)
cv2.imshow("Circle", img1)
cv2.imshow("Rectangle", img2)

cv2.imwrite("Contours & shape detection/circle.png", img1)
cv2.imwrite("Contours & shape detection/rectangle.png", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
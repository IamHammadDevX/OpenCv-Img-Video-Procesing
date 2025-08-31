import cv2

image = cv2.imread("phase-1\\image1.jpg")

if image is None:
    print("Error: Image does not loaded")
else:
    print("Image loaded successfuly")

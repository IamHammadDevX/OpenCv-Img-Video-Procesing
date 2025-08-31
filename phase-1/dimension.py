import cv2

image = cv2.imread("phase-1\\image1.jpg")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded Successfully\n Height: {h}\n Width: {w}\n Color Channel: {c}")
else:
    print("Could not load the image")
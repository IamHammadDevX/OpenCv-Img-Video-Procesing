import cv2

image = cv2.imread("phase-1\\image1.jpg")

if image is not None:
    cv2.imshow("Photo", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the image")

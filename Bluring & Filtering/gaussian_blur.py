import cv2

image = cv2.imread("Bluring & Filtering\\3992379.jpg")

if image is not None:
    print("Image Loaded")

    blurred = cv2.GaussianBlur(image, (7, 7), 5)

    cv2.imshow("Original", image)
    cv2.imshow("Blurred", blurred)
    cv2.imwrite("Bluring & Filtering\\blured.png", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
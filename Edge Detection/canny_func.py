import cv2

image = cv2.imread("Edge Detection\\4998869.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    print("Image Loaded")

    egdes = cv2.Canny(image, 50, 150)

    cv2.imshow("Original", image)
    cv2.imshow("Edges", egdes)
    cv2.imwrite("Edge Detection\\egde.png", egdes)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
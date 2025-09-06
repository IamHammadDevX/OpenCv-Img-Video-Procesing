import cv2

image = cv2.imread("Edge Detection\\7648144.jpg", cv2.IMREAD_GRAYSCALE)

if image is not None:
    print("Image Loaded")

    ret, thresh_img = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY)

    cv2.imshow("Original", image)
    cv2.imshow("Threshed Image", thresh_img)
    cv2.imwrite("Edge Detection\\threshed.png", thresh_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image not found")
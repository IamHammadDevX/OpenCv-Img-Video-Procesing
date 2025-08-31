import cv2

image = cv2.imread("Image Resizing & Reshaping\\8337512.jpg")

if image is not None:
    print("Image Loaded")
    resized = cv2.resize(image, (400, 400))

    cv2.imshow("Original Photo", image)
    cv2.imshow("Resized Photo", resized)
    cv2.imwrite("Image Resizing & Reshaping\\resized_image1.png", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Could'nt Load")
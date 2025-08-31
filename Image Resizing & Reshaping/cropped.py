import cv2

image = cv2.imread("Image Resizing & Reshaping\\7047294.jpg")

if image is not None:
    print("Image Loaded")

    cropped = image[50:450, 30:500] # [start-Y-axis:End-Y-axis, start-X-axis:End-X-axis]
    cv2.imshow("Original", image)
    cv2.imshow("Cropped", cropped)
    cv2.imwrite("Image Resizing & Reshaping\\cropped.png", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

else:
    print("Image Could'nt Load")

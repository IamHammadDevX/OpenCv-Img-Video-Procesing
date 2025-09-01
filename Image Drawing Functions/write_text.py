import cv2

image = cv2.imread("Image Drawing Functions\\6648550.jpg")

if image is not None:
    print("Image Loaded")

    cv2.imshow("Original", image)
    write_text = cv2.putText(image, "Yoga Exercise", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 255), 2)
    cv2.imshow("Test Edited", write_text)

    cv2.imwrite("Image Drawing Functions\\writeText.png", write_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Oops! Image Could'nt loaded")
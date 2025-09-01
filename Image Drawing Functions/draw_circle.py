import cv2

image = cv2.imread("Image Drawing Functions\\3779756.jpg")

if image is not None:
    print("Image Loaded")

    cv2.imshow("Original", image)
    draw_circle = cv2.circle(image, (435, 150), 70, (0,0, 255), 10)
    cv2.imshow("Circle", draw_circle)

    cv2.imwrite("Image Drawing Functions\\drawCircle.png", draw_circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Oops! Image Could'nt loaded")
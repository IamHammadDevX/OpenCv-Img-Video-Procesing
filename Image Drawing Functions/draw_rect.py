import cv2

image = cv2.imread("Image Drawing Functions\\9442076.jpg")

if image is not None:
    print("Image Loaded")

    cv2.imshow("Original", image)
    draw_rect = cv2.rectangle(image, (150, 100), (300, 300), (0,255,0), 4)
    cv2.imshow("Rectangle", draw_rect)

    cv2.imwrite("Image Drawing Functions\\drawRect.png", draw_rect)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Oops! Image Could'nt loaded")
import cv2

image = cv2.imread("Image Drawing Functions\\zoelifestyle172.jpg")

if image is not None:
    print("Image Loaded")

    cv2.imshow("Original", image)
    pt1 = (50, 100)
    pt2 = (300, 100)
    color = (255, 0, 0)
    thickness = 4
    draw_line = cv2.line(image, pt1, pt2, color, thickness)

  F:\OpenComputerVision-Python\Image Drawing Functions\9442076.jpg

else:
    print("Oops! Image Could'nt loaded")
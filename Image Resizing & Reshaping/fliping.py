import cv2

image = cv2.imread("Image Resizing & Reshaping\\jackcosplay095.jpg")

if image is not None:
    print("Image Loaded")

    flip_hor = cv2.flip(image, 1)
    flip_vert = cv2.flip(image, 0)
    flip_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("Flipped Horizontal", flip_hor)
    cv2.imshow("Flipped Vertical", flip_vert)
    cv2.imshow("Flipped", flip_both)

    cv2.imwrite("Image Resizing & Reshaping\\flipped.png", flip_both)
    print("Image Saved")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Could'nt Load")
import cv2

image = cv2.imread("phase-1\\image1.jpg")

if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    saved = cv2.imwrite("phase-1\\grayscale.png", gray)
    if saved:
        print("Image Saved as 'grayscale.png' successfully")
    else:
        print("Error: Image Does not saved")

    cv2.imshow("Gray Scale Photo", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: While loading image")

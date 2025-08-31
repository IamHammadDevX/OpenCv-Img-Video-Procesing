import cv2

image = cv2.imread("Image Resizing & Reshaping\\9207176.jpg")

if image is not None:
    print("Image Loaded")

    # center point
    (h, w) = image.shape[:2]
    center_point = (w//2, h//2) # w,h//2, integer division
    formula = cv2.getRotationMatrix2D(center_point, 90, 1.0)
    rotation = cv2.warpAffine(image, formula, (w, h))

    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotation)

    cv2.imwrite("Image Resizing & Reshaping\\rotated_img.png", rotation)
    print("Image Saved")
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image Could'nt Load")
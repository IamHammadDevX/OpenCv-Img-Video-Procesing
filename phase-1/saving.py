import cv2

image = cv2.imread("phase-1\\image1.jpg")

if image is not None:
    success = cv2.imwrite("phase-1\\output_workout.png", image)
    if success:
        print("Image Saved as 'output_workout.png' successfully")
    else:
        print("Error: Image Does'nt saved")
else:
    print("Error: While loading image")
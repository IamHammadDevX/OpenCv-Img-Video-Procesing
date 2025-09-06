import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # ret = True/False, frame = 1 image

    if not ret:
        print("Could'nt read frame")
        break
    
    cv2.imshow("Webcam Feed", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("Quiting.....")
        break

cap.release()
cv2.destroyAllWindows()
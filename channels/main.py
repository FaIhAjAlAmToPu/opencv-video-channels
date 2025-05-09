import cv2, numpy as np

cap = cv2.VideoCapture("resources/rgb.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't read frames(no more frames)")
        break
    h, w, _ = frame.shape
    frame = cv2.resize(frame, (w//4, h//4))
    cv2.imshow("Blue Frames", frame[:,:,0])
    cv2.imshow("Green Frames", frame[:,:,1])
    cv2.imshow("Red Frames", frame[:,:,2])
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
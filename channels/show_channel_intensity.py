import cv2, numpy as np

cap = cv2.VideoCapture("resources/rgb.mp4")

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
blue_out = cv2.VideoWriter("resources/grayscale_blue.mp4", fourcc, fps, (frame_width//4, frame_height//4), isColor=False)
green_out = cv2.VideoWriter("resources/grayscale_green.mp4", fourcc, fps, (frame_width//4, frame_height//4), isColor=False)
red_out = cv2.VideoWriter("resources/grayscale_red.mp4", fourcc, fps, (frame_width//4, frame_height//4), isColor=False)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't read frames(no more frames)")
        break
    h, w, _ = frame.shape
    frame = cv2.resize(frame, (w//4, h//4))

    blue_frame = frame[:,:,0]
    green_frame = frame[:,:,1]
    red_frame = frame[:,:,2]

    blue_out.write(blue_frame)
    green_out.write(green_frame)
    red_out.write(red_frame)
cap.release()
blue_out.release()
green_out.release()
red_out.release()

cv2.destroyAllWindows()
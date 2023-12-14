import cv2

cap = cv2.VideoCapture(r"movingball.mp4")

mog = cv2.createBackgroundSubtractorMOG2()


while cap.isOpened():
    ret, gray = cap.read()

    fgmask = mog.apply(gray)

    
    if ret:
        resizedFgmask = cv2.resize(fgmask, None, fx = 0.5, fy = 0.5)
        cv2.imshow("foreground", resizedFgmask)
    else:
       print('no video')
       cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
       continue

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
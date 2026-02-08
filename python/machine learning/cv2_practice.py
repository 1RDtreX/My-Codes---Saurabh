import cv2

open=cv2.VideoCapture(0)
while True:
    ok, frame=open.read()
    if ok:
        frame=cv2.flip(frame,10)
        cv2.imshow('Camera',frame)
    if cv2.waitKey(1) & 0xFF==ord(' '):
        break


frame.recover()
cv2.destroyAllWindows
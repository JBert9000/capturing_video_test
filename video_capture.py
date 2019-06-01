import cv2, time

video=cv2.VideoCapture(0)

how_many_frames=0

while True:
    how_many_frames=how_many_frames+1
    check, frame=video.read()

    print(check)
    print(frame)

    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capture1",frame)

    key=cv2.waitKey(1)

    if key==ord('q'):
        break
print("There were " + str(how_many_frames) + " many frames in this video.")

video.release()
cv2.destroyAllWindows()

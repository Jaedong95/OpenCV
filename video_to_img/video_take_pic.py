import cv2
import datetime

video_file = '1st_55.mp4'

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000/fps)
    print('FPS: %f, Delay: %dms' %(fps, delay))

    while True:
        ret, img = cap.read()
        now = datetime.datetime.now().strftime("%d_%H-%M-%S")
        print(now)

        if ret:
            cv2.imshow(video_file, img)
            key = cv2.waitKey(12)
            if key == 27:
                break

            cv2.imwrite('1st/'+ now + '.jpg',img)

            '''
            if cv2.waitKey(1) != -1:
                cv2.imwrite('tmp.jpg', img)
                break
            '''
        else:
            break
else:
    print("can't open video.")

cap.release()
cv2.destroyAllWindows()
import cv2

vidcap = cv2.VideoCapture('3rd_26_reversed.mp4')
stat, image = vidcap.read()

fps = vidcap.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
print('FPS: %f, Delay: %dms' % (fps, delay))

count = 1
idx = 1
success = True
img_cat = "3rd_video_"

while success:
    success, image = vidcap.read()
    if count % 12 == 0:
        cv2.imwrite("3rd_reversed/" + img_cat + "%d.jpg" % idx, image)
        #cv2.imwrite('TLH_11/A1_additional_procedures/img/%d.jpg' % idx, image)
        print("saved image %d.jpg" % idx)
        idx += 1

    if cv2.waitKey(10) == 27:
        break
    count += 1

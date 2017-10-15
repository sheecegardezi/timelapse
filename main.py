from mss import mss
import numpy as np
import cv2
import time

import os

start = time.time()

PERIOD_OF_TIME = 3600 # 5min


while True:
    sct = mss()
    noOfFiles = len([f for f in os.listdir('.') if os.path.isfile(f)])

    imgs=[]
    for filename in sct.save():

        imgs.append(cv2.imread(filename))  # Load an color image in grayscale

    for i in range(len(imgs)):

        imgs[i]= cv2.resize(imgs[i], (1680,1050)) #resize both images

    both = np.hstack((imgs[0],imgs[1]))
    both= cv2.resize(both, (1680,1050)) #shrink the combined image

    cv2.imwrite(str(noOfFiles)+'.png', both)

    if time.time() > start + PERIOD_OF_TIME : break #stop after an hour

    time.sleep(60)   # Delay for 1 minute

#Debug
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', both)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

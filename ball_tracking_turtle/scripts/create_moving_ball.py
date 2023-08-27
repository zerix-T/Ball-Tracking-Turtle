#!/usr/bin/env python
import os
import cv2
import numpy as np
import ament_index_python
import math

vid_codec = cv2.VideoWriter_fourcc(*'MP42')

share_directory = ament_index_python.get_package_share_directory('ball_tracking_turtle')
vid_path = share_directory + "/resource/moving_ball.avi"
vid = cv2.VideoWriter(vid_path, vid_codec, 30.0, (500,500))

f_no = 30*60
theta = np.linspace(0, 2*np.pi, num=f_no)

for t in theta:
    img = np.full((500,500,3), 255, np.uint8)

    x = 213*(math.cos(t) / (math.sin(t)**2 + 1))
    y = 213*(math.cos(t) * math.sin(t) / (math.sin(t)**2 + 1))

    x = int(np.interp(x, [-213,213], [37,463]))
    y = int(np.interp(y, [-75,75], [175,325]))

    img = cv2.circle(img, (x,y), 20, (10,255,0), -1)

    vid.write(img)

vid.release()


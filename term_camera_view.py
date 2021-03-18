import os
import time
import cv2
import moviepy.editor
from PIL import Image
import truecolor
import colour

cap = cv2.VideoCapture(0)

# camera settings go here

width = 640
height = 480
resolution_divisor = 6

while True:
    ret, frame = cap.read()
    if not ret:
        break
    pix = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).load()
    for y in range(0, height, resolution_divisor*2):
        for x in range(0, width, resolution_divisor):
            print(truecolor.fore_text("█", pix[x,y][:3]), end='')
        print("")
    print(f"\033[{int(height/(resolution_divisor*2))+1}F")
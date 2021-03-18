import os
import time
import moviepy.editor
from PIL import Image
import truecolor
import colour

vid = moviepy.editor.VideoFileClip("./fd_small.mp4") # input video file here

# video settings go here

width = 640
height = 360
fps = 15
resolution_divisor = 4

for frame in vid.iter_frames(fps=fps):
    pix = Image.fromarray(frame).load()
    for y in range(0, height, resolution_divisor*2):
        for x in range(0, width, resolution_divisor):
            print(truecolor.fore_text("█", pix[x,y][:3]), end='')
        print("")
    print(f"\033[{int(height/(resolution_divisor*2))+1}F")
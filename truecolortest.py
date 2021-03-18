import time
import os
try:
    import truecolor
    import colour
except ModuleNotFoundError:
    os.system("pip3 install truecolor colour")
    import truecolor
    import colour

os.system("clear")

colorList = []
for y in range(0, 240):
    colorList.append(truecolor.fore_text("█", colour.Color("red", hue=y/240).hex_l))

width = 64
fps = 60

while True:
    display = []
    for z in range(round(width/2)):
        display.append("".join(colorList[z:width+z]))
    print("\n".join(display), end="")
    time.sleep(1/fps)
    colorList.append(colorList.pop(0))
    print(f"\033[{round(width/2)}F")
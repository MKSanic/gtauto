import cv2 as cv
import numpy as np
import os
import shutil
import requests
from pathlib import Path
from datetime import datetime

threshold = 0.9
world = "naturalxp"


os.chdir(str(Path(__file__).parent) + "/worlds")
url = f"https://s3.amazonaws.com/world.growtopiagame.com/{world}.png"
file = open(f"{world}.png","wb")
r = requests.get(url,stream=True)
shutil.copyfileobj(r.raw,file)

t = datetime.now()
img = cv.imread(f"{world}.png",cv.IMREAD_UNCHANGED)
img = img[...,:3]
img = np.ascontiguousarray(img)
fossil = cv.imread(os.path.join(Path(__file__).parent,"fossil.png"),cv.IMREAD_UNCHANGED)
fossil = fossil[...,:3]
print((datetime.now()-t).seconds)
t = datetime.now()
result = cv.matchTemplate(img,fossil,cv.TM_CCOEFF_NORMED)
print(datetime.now()-t)
miv,mav,mil,mal = cv.minMaxLoc(result)
locations = list(zip(*np.where(result >= threshold)[::-1]))
rects = []
for x,y in locations:
    rects.append([x,y,fossil.shape[0],fossil.shape[1]])

#rects,weights = cv.groupRectangles(rects,1,0.5)
t = datetime.now()
result = img
for x,y,w,h in rects:
    result = cv.rectangle(result,(x,y),(x+w,y+h),color=(0,00,255),thickness=2,lineType=cv.LINE_4)
print(datetime.now()-t)
print("No. of fossils: " + str(len(rects)))
#cv.imwrite("result.jpg",result)
cv.imshow("result",result)

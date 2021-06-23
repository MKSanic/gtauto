import os
import time
import cv2 as cv
import numpy as np
import PIL as pillow
import pyautogui as pyag
#from pydub import AudioSegment as AS
#from pydub.playback import play
import pydirectinput as pyag2
from pathlib import Path
import time
import win32gui,win32ui,win32con
import threading
import keyboard as kb
from datetime import datetime
from PIL import ImageFont
#import pywinauto as pwa
os.chdir(Path(__file__).parent)
pyag2.PAUSE = 0.03
pyag.PAUSE = 0.03
class WindowCapture:
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    def __init__(self, window_name):
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y
    def screenshot(self):
        try:
            wDC = win32gui.GetWindowDC(self.hwnd)
            dcObj = win32ui.CreateDCFromHandle(wDC)
            cDC = dcObj.CreateCompatibleDC()
            dataBitMap = win32ui.CreateBitmap()
            dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
            cDC.SelectObject(dataBitMap)
            cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)
            signedIntsArray = dataBitMap.GetBitmapBits(True)
            img = np.fromstring(signedIntsArray, dtype='uint8')
            img.shape = (self.h, self.w, 4)
            dcObj.DeleteDC()
            cDC.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, wDC)
            win32gui.DeleteObject(dataBitMap.GetHandle())
            img = img[...,:3]
            img = np.ascontiguousarray(img)
            return img
        except:
            print("window not found")
            cv.destroyAllWindows()
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)
    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
defaultThreshold = 0.9
fossil = cv.imread("fossil2.png",cv.IMREAD_UNCHANGED)[...,:3]
hfossil = cv.imread("hfossil2.png",cv.IMREAD_UNCHANGED)[...,:3]
def fossilSearch(ss,threshold=defaultThreshold):
    result = cv.matchTemplate(ss,fossil,cv.TM_CCOEFF_NORMED)
    locations = list(zip(*np.where(result >= threshold)[::-1]))
    rects = []
    for x,y in locations:
        rects.append([x,y,fossil.shape[0],fossil.shape[1]])
    for x,y,w,h in rects:
        ss = cv.rectangle(ss,(x,y),(x+w,y+h),color=(0,00,255),thickness=2,lineType=cv.LINE_4)
    result = cv.matchTemplate(ss,hfossil,cv.TM_CCOEFF_NORMED)
    locations = list(zip(*np.where(result >= threshold)[::-1]))
    rects = []
    for x,y in locations:
        rects.append([x,y,hfossil.shape[0],hfossil.shape[1]])
    for x,y,w,h in rects:
        ss = cv.rectangle(ss,(x,y),(x+w,y+h),color=(0,255,0),thickness=2,lineType=cv.LINE_4)
    return ss
def zoomOut():
    for i in range(0,15):
        pyag.vscroll(-2000)
def annoy():
    play(AS.from_mp3("audio.mp3"))
def Break2():
    time.sleep(5)
    pos = pyag.position()
    x = pos[0]
    y = pos[1]
    while(True):
        while(pause):
            pass
        pyag2.click(x,y)
        time.sleep(0.05)
def Break():
    global die
    global pause
    try:
        block1 = 1100,500
        block2 = 1225,500
        addV = 500,400
        player = 950,500
        for i in range(0,25):
            for i2 in range(0,3):
                print(str(i+1) + ", " + str(i2+1))
                time.sleep(1)
                if(die):
                    return
                t = datetime.now()
                for i3 in range(0,99):
                    while(pause):
                        pass
                    if(die):
                        return
                    pyag2.click(block1[0],block1[1])
                    time.sleep(0.3)
                    if(die):
                        return
                    pyag2.click(block2[0],block2[1])
                    time.sleep(0.3)
                    if(die):
                        return
                    pyag2.keyDown("space")
                    time.sleep(4.5)
                    if(die):
                        return
                    pyag2.keyUp("space")
                    pyag2.keyDown("right")
                    time.sleep(1)
                    if(die):
                        return
                    pyag2.keyUp("right")
                    pyag2.press("space")
                    pyag2.press("space")
                    pyag2.press("space")
                    time.sleep(1)
                    if(die):
                        return
                print(f"This loop took {datetime.now() - t}")
                if(i2 != 2):
                    pyag2.keyDown("left")
                    time.sleep(5)
                    if(die):
                        return
                    pyag2.keyUp("left")
                    pyag2.press("space")
                    pyag2.press("space")
                    time.sleep(3)
                    if(die):
                        return
                    pyag2.keyDown("right")
                    time.sleep(5)
                    if(die):
                        return
                    pyag2.keyUp("right")
                    pyag2.press("space")
            if(die):
                return
            pyag2.keyDown("left")
            time.sleep(5)
            if(die):
                return
            pyag2.keyUp("left")
            pyag2.press("space")
            pyag2.press("space")
            time.sleep(3)
            if(die):
                return
            pyag2.press("tab")
            time.sleep(0.5)
            if(die):
                return
            pyag2.press("tab")
            time.sleep(1)
            if(die):
                return
            pyag2.click(player[0],player[1])
            time.sleep(5)
            if(die):
                return
            pyag2.click(addV[0],addV[1])
            time.sleep(3)
            if(die):
                return
            pyag2.press("tab")
            pyag2.keyDown("right")
            time.sleep(5)
            if(die):
                return
            pyag2.keyUp("right")
            pyag.click(pyag.locateOnScreen("chand_inv.png"))
            pyag.click(pyag.locateOnScreen("chand_inv2.png"))
            time.sleep(1)
            if(die):
                return
            pyag2.press("space")
            pyag2.press("space")
            if(die):
                return
            #annoy()
        #annoy()
    except KeyboardInterrupt:
        pause = True
        raise Exception("interrupted")
def Break3():
    global die
    global pause
    try:
        block1 = 1100,500
        block2 = 1225,500
        addV = 500,400
        player = 950,500
        for i in range(0,25):
            for i2 in range(0,3):
                print(str(i+1) + ", " + str(i2+1))
                time.sleep(1)
                if(die):
                    return
                t = datetime.now()
                for i3 in range(0,99):
                    while(pause):
                        pass
                    pyag2.click(player[0],player[1])
                    time.sleep(2.5)
                    if(die):
                        return
                print(f"This loop took {datetime.now() - t}")
                if(i2 != 2):
                    pyag2.keyDown("left")
                    time.sleep(5)
                    if(die):
                        return
                    pyag2.keyUp("left")
                    pyag2.press("space")
                    pyag2.press("space")
                    time.sleep(3)
                    if(die):
                        return
                    pyag2.keyDown("right")
                    time.sleep(5)
                    if(die):
                        return
                    pyag2.keyUp("right")
                    pyag2.press("space")
                    pyag2.press("space")
                    pyag2.press("space")
            if(die):
                return
            pyag2.keyDown("left")
            time.sleep(5)
            if(die):
                return
            pyag2.keyUp("left")
            pyag2.press("space")
            pyag2.press("space")
            time.sleep(3)
            if(die):
                return
            pyag2.press("tab")
            time.sleep(0.5)
            if(die):
                return
            pyag2.press("tab")
            time.sleep(1)
            if(die):
                return
            pyag2.click(player[0],player[1])
            time.sleep(5)
            if(die):
                return
            pyag2.click(addV[0],addV[1])
            time.sleep(3)
            if(die):
                return
            pyag2.press("tab")
            pyag2.keyDown("right")
            time.sleep(5)
            if(die):
                return
            pyag2.keyUp("right")
            pyag.click(pyag.locateOnScreen("chand_inv.png"))
            pyag.click(pyag.locateOnScreen("chand_inv2.png"))
            time.sleep(1)
            if(die):
                return
            pyag2.press("space")
            pyag2.press("space")
            pyag2.press("space")
            if(die):
                return
            #annoy()
        #annoy()
    except KeyboardInterrupt:
        pause = True
        raise Exception("interrupted")
kill = False
pause = False
die = False
def main(r):
    global die
    if(r):
        record()
    while(True):
        Break()
        while(die):
            pass
def pauser():
    def main():
        while(True):
            if(kb.is_pressed("f10")):
                global pause
                pause = not pause
                time.sleep(1)
    t = threading.Thread(target=main)
    t.start()
    return t
def disconnected():
    def main():
        login = 1330,960
        cancel = 400,950
        search = 1380,320
        color = (152, 194, 211)
        check = 1716,254
        checkColor = (15,54,72)
        exitWorld = 954,185
        worldName = "naturalxp"
        chandLoc = 390,873
        inv1 = 970,940
        inv2 = 970, 600
        invSearch = 760,770
        bfilter = 100,860
        global pause
        global die
        def out():
            return pyag.pixel(cancel[0],cancel[1]) == color
        while(True):
            while(pause):
                pass
            if(out()):
                print("cancelling")
                pyag2.click(cancel[0],cancel[1])
                die = True
                pause = True
                tries = 0
                Max = 3600
                success = False
                inWorld = False
                time.sleep(1)
                pyag2.click(login[0],login[1])
                while(tries <= Max):
                    tries += 1
                    time.sleep(60)
                    if(out()):
                        print("cancelling")
                        pyag2.click(cancel[0],cancel[1])
                        continue
                    else:
                        print("successfully reconnected")
                        success = True
                        break
                if(success):
                    print("success")
                    pyag2.press("enter")
                    time.sleep(1)
                    while(True):
                        if(pyag.pixel(check[0],check[1]) == checkColor):
                            pyag2.click(search[0],search[1])
                            time.sleep(1)
                            for i in range(1,25):
                                pyag2.press("backspace")
                                time.sleep(0.1)
                            pyag2.typewrite(worldName,0.5)
                            pyag2.press("enter",2)
                            time.sleep(10)
                            inWorld = True
                            break
                        else:
                            pyag2.press("esc")
                            time.sleep(1)
                            pyag2.click(exitWorld[0],exitWorld[1])
                            time.sleep(5)
                if(inWorld):
                    time.sleep(5)
                    pyag2.keyDown("right")
                    time.sleep(5)
                    pyag.keyUp("right")
                    pyag2.press("space")
                    time.sleep(10)
                    pyag2.click(inv1[0],inv1[1])
                    time.sleep(3)
                    pyag2.click(bfilter[0],bfilter[1])
                    pyag2.click(invSearch[0],invSearch[1])
                    for i in range(0,100):
                        pyag2.press("backspace")
                        time.sleep(0.05)
                    pyag2.typewrite("chand",0.5)
                    pyag2.press("enter")
                    pyag2.click(bfilter[0],bfilter[1])
                    time.sleep(1)
                    pyag2.click(chandLoc[0],chandLoc[1])
                    time.sleep(1)
                    pyag2.click(inv2[0],inv2[1])
                    die = False
                    pause = False
    t = threading.Thread(target = main)
    t.start()
    return t
def record():
    def main():
        wincap = WindowCapture("Growtopia.exe")
        fourcc = cv.VideoWriter_fourcc(*"XVID")
        for i in range(0,30):
            out = cv.VideoWriter("logs/" + str(i+1) + ".avi",fourcc,2.0,(1920,1080))
            try:
                for i2 in range(0,3600):
                    global kill
                    if(kill):
                        kill = False
                        raise Exception("killed")
                    t = time.time()
                    img = wincap.screenshot()
                    #img = pyag.screenshot()#pillow.ImageDraw.Draw(pyag.screenshot()).text((0,0),str(datetime.now()),font=ImageFont.truetype("C:/Windows/Fonts/Arial.ttf",64))
                    frame = cv.cvtColor(np.array(img),cv.COLOR_BGR2RGB)
                    print(1/(time.time()-t))
                    out.write(frame)
            except Exception as e:
                print(e)
                print("kb interrupted")
                return
        print("finished recording")
    t = threading.Thread(target=main)
    t.start()
    return t
def transfer():
    drop = 1720,980
    ok = 960,660
    while(True):
        while(pause):
            pass
        pyag2.keyDown("left")
        time.sleep(2)
        pyag2.keyUp("left")
        print(1)
        pyag2.press("space",2)
        print(2)
        time.sleep(1)
        pyag2.press("right")
        print(3)
        pyag.click(pyag.locateOnScreen("chand_inv.png"))
        print(4)
        pyag2.click(drop[0],drop[1])
        print(5)
        time.sleep(1)
        pyag2.click(ok[0],ok[1],5)
        print(6)
        time.sleep(0.5)
        pyag2.press("up")
        time.sleep(1)
def keybinds():
    def main():
        slot1 = 900,1020
        slot2 = 1000,1020
        slot3 = 1100,1020
        while(True):
            while(not (kb.is_pressed("1") ^ kb.is_pressed("2") ^ kb.is_pressed("3"))):
                pass
            global kill
            if(kill):
                return
            pos = pyag.position()
            if(kb.is_pressed("1")):
                pyag2.click(slot1[0],slot1[1])
            elif(kb.is_pressed("2")):
                pyag2.click(slot2[0],slot2[1])
            elif(kb.is_pressed("3")):
                pyag2.click(slot3[0],slot3[1])
            pyag.moveTo(pos[0],pos[1])
            print("yeee")
    t = threading.Thread(target=main)
    t.start()
    return t
pauser()

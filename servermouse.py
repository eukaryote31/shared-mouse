import pymouse
import screenutils
import threading
import time


mouse = pymouse.PyMouse()
center = (int(screenutils.monitors[0].width / 2),
          int(screenutils.monitors[0].height / 2))
lastpos = center
counter = 0


def callback():
    return None


def active_center():
    set_interval(center_mouse, 0.005)


def center_mouse():
    callback(dist_center())
    global counter
    counter += 1

    if counter >= 100:
        mouse.move(*center)


def dist_center():
    x, y = mouse.position()
    global lastpos
    dist = (x - lastpos[0],
            y - lastpos[1])
    lastpos = (x, y)
    return dist


def set_interval(func, sec):
    def func_wrapper():
        while True:
            func()
            time.sleep(sec)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

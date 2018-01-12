import hidemouse
import servermouse
import time


def func(n):
    print(n)


hidemouse.show()
servermouse.callback = func
servermouse.active_center()
time.sleep(10)

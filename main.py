# :) by @L.E.
# MALWAREMAN(AKA:LE CET) VERSION HAVE SOME ERRORS, SO THIS IS FULLY FIXED BY ME.
import win32api
import win32gui
import random
import win32con
from win32gui import *
from win32gui import GetDesktopWindow, GetWindowDC, StretchBlt, BitBlt
from win32api import GetSystemMetrics
import math
import time
import threading
import ctypes

hwnd = GetDesktopWindow()
hdc2 = GetWindowDC(hwnd)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)
x2 = GetSystemMetrics(0)
y2 = GetSystemMetrics(1)

desktop = GetDesktopWindow()
left, top, right, bottom = GetWindowRect(desktop)


def redraw():
    RedrawWindow(0, None, None, win32con.RDW_ERASE | win32con.RDW_INVALIDATE | win32con.RDW_ALLCHILDREN)


def radial_move():
    while True:
        hdc = GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc, x, y)
        sel = SelectObject(memdc, hbit)

        val = random.randint(1, 2)
        rateofturning = 30
        print(val)

        if val == 1:
            PlgBlt(memdc, [(left - rateofturning, top + rateofturning),
                           (right - rateofturning, top - rateofturning),
                           (left + rateofturning, bottom + rateofturning)],
                   hdc, 0, 0, x2, y2, 0, 0, 0)

        if val == 2:
            PlgBlt(memdc, [(left + rateofturning, top - rateofturning),
                           (right + rateofturning, top + rateofturning),
                           (left - rateofturning, bottom - rateofturning)],
                   hdc, 0, 0, x2, y2, 0, 0, 0)

            AlphaBlend(hdc, random.randint(-10, 10), random.randint(-10, 10), x, y, memdc, 0, 0, x, y,
                       (0, 0, 70, 0))

        SelectObject(memdc, sel)
        DeleteObject(sel)
        DeleteObject(hbit)
        DeleteDC(memdc)
        DeleteDC(hdc)


def sliding():
    while True:
        hdc = GetDC(0)
        r = random.randint(0, 1)
        if r == 1:
            for _ in range(10):
                StretchBlt(hdc, 0, -50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
                StretchBlt(hdc, 0, y - 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
        else:
            for _ in range(10):
                StretchBlt(hdc, 0, 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)
                StretchBlt(hdc, 0, -y + 50, x, y, hdc, 0, 0, x, y, win32con.SRCCOPY)


def blurring():
    while True:
        hdc = GetDC(0)
        memdc = CreateCompatibleDC(hdc)
        hbit = CreateCompatibleBitmap(hdc, x, y)
        sel = SelectObject(memdc, hbit)
        BitBlt(memdc, 0, 0, x, y, hdc, 0, 0, win32con.SRCCOPY)

        AlphaBlend(hdc, random.randint(-10, 10), random.randint(-10, 10), x, y, memdc, 0, 0, x, y,
                   (0, 0, 70, 0))

        SelectObject(memdc, sel)
        DeleteObject(sel)
        DeleteObject(hbit)
        DeleteDC(memdc)
        DeleteDC(hdc)

        time.sleep(0.2)


def room_vertical():
    hdc = GetDC(0)
    for _ in range(15):
        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0, 0 - 10, x2, y2 + 20, hdc, 0, 0, x2, y2, win32con.SRCCOPY)
        time.sleep(0.2)


def room_horizontal():
    hdc = GetDC(0)
    for _ in range(15):
        SetStretchBltMode(hdc, 4)
        StretchBlt(hdc, 0 - 10, 0, x2 + 20, y2, hdc, 0, 0, x2, y2, win32con.SRCCOPY)


def zoom_vertical():
    room_vertical()


def zoom_horizontal():
    room_horizontal()


def combined_streaching():
    while True:
        zoom_vertical()
        redraw()
        zoom_horizontal()


def kill_thread(thread):
    """
    thread: a threading.Thread object
    """
    thread_id = thread.ident
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, ctypes.py_object(SystemExit))
    if res > 1:
        ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
        print('Exception raise failure')


# Starting Threads
t1 = threading.Thread(target=radial_move)
t1.start()
time.sleep(15)
kill_thread(t1)

t2 = threading.Thread(target=sliding)
t2.start()
time.sleep(15)
kill_thread(t2)

t3 = threading.Thread(target=blurring)
t3.start()
time.sleep(15)
kill_thread(t3)

t4 = threading.Thread(target=combined_streaching)
t4.start()
time.sleep(15)
kill_thread(t4)

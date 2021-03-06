# from PIL import *
import win32gui
import pyscreenshot as ImageGrab

# Test for Github
def get_window():
    toplist, winlist = [], []

    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    league_client = [(hwnd, title) for hwnd, title in winlist if 'league client' in title.lower()]
    print("Number of Process" + str(len(league_client)))
    league_client = league_client[2]
    hwnd = league_client[0]

    return hwnd


def take_screenshot():
    window = get_window()
    win32gui.SetForegroundWindow(window)
    rect = win32gui.GetWindowRect(window)
    print(rect[0])
    print(rect[1])
    print(rect[2])
    print(rect[3])
    bbox = (rect[0], rect[1], rect[2], rect[3])
    im = ImageGrab.grab(bbox)
    im.show()

if __name__ == "__main__":
    take_screenshot()

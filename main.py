import time

import cv2
import numpy
import vlc
from mss import mss

from get_text import get_text
from get_zone import get_zone
from rect import Rect
from template import Template
from viewer import view

direct_message_template = Template(cv2.imread('res/dm_received.png', cv2.IMREAD_GRAYSCALE))


def look_for_dms(rect):
    with mss() as sct:
        monitor_number = 1
        mon = sct.monitors[monitor_number]
        monitor = {
            "top": mon["top"] + rect.y,
            "left": mon["left"] + rect.x,
            "width": rect.width,
            "height": rect.height,
            "mon": monitor_number,
        }
        preview = numpy.array(sct.grab(monitor))
        view("Zone Preview", preview, True)
        lastString = ""
        while True:
            loop = numpy.array(sct.grab(monitor))
            gray = cv2.cvtColor(loop, cv2.COLOR_BGR2GRAY)
            gotText, text = get_text(gray)
            print(text)
            # view("captured", gray, True)
            # found_locations = direct_message_template.match(gray, 0.3)
            if gotText and "to You (Direct" in text:
                if lastString != text:
                    notify()
                    print("match found")
                else:
                    print("already reported that string")
                # decide on how to detect if the direct message is new
            else:
                print("no match found")
            if gotText:
                lastString = text
            time.sleep(0.25)

        # consider grayscaling screenshots for better matching?
        # play a sound when a match is found


def on_zone_defined(points):
    rect = Rect(points[0][0], points[0][1], points[1][0] - points[0][0], points[1][1] - points[0][1])
    print(str(rect))
    look_for_dms(rect)


def notify():
    vlc.MediaPlayer("res/notif.wav").play()


if __name__ == '__main__':
    notify()
    # view("template", direct_message_template.template, True)
    get_zone(on_zone_defined)

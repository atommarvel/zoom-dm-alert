import cv2
import numpy as np

from rect import Rect


class Template:
    def __init__(self, template):
        self.template = template
        self.h = template.shape[0]
        self.w = template.shape[1]

    def match(self, img, threshold=0.8):
        res = cv2.matchTemplate(img, self.template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        found_locations = []
        for pt in zip(*loc[::-1]):
            found_locations.append(Rect(pt[0], pt[1], self.w, self.h))
        if len(found_locations) > 0:
            return found_locations
        return False
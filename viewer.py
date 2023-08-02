import cv2

def view(name, img, wait=False):
    cv2.imshow(name, img)
    cv2.setMouseCallback(name, gen_on_mouse(img))
    if wait:
        cv2.waitKey(0)


def gen_on_mouse(img):
    def on_mouse(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print('x = %d, y = %d' % (x, y))
            print("BGR is", img[y, x])
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            print("HSV is", hsv[y, x])

    return on_mouse
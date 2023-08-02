from pynput.mouse import Listener

zone_points = []

def on_move(x, y):
    print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    global zone_points
    print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    if not pressed:
        zone_points.append((x,y))
    if len(zone_points) >= 2:
        print(zone_points)
        # Stop listener
        return False


def on_scroll(x, y, dx, dy):
    print('Scrolled {0}'.format(
        (x, y)))


def get_zone(callback):
    # Collect events until released
    with Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
    global zone_points
    callback(zone_points)

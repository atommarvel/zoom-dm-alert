class Rect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.x2 = x + width
        self.y2 = y + height
        self.start_point = (x, y)
        self.end_point = (self.x2, self.y2)
        self.meta = {}

    def get_img_subsection(self, img):
        return img[self.y:self.y2, self.x:self.x2]

    def move(self, x=0, y=0):
        return Rect(self.x + x, self.y + y, self.width, self.height)

    def __str__(self):
        return f'({self.x}, {self.y}) + ({self.x2}, {self.y2}) = {self.width}x{self.height}'

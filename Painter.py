from Figure import Point


class Painter(object):

    def __init__(self):
        self.shortcuts = {
            Point: self.put_pixel
        }

    def put_pixel(self, canvas, point):
        """ canvasの座標(x,y)をrgbに塗る """
        assert False, "Override me!"

    def draw(self, canvas, figure):
        """ canvasにfigureを描く """
        try:
            self.shortcuts[type(figure)](canvas, figure)
        except KeyError:
            for p in figure:
                self.draw(canvas, p)

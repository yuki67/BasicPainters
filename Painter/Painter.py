from Painter.Figure import Point


class Painter(object):

    def __init__(self):
        # draw_functionsで描画に使う関数を指定する
        # 何も指定しなければ、すべて点で描画される(遅い)
        self.draw_functions = {
            Point: self.put_pixel
        }

    def put_pixel(self, canvas, point):
        """ canvasの座標(x,y)をrgbに塗る """
        assert False, "Override me!"

    def draw(self, canvas, figure):
        """ canvasにfigureを描く """
        try:
            self.draw_functions[type(figure)](canvas, figure)
        except KeyError:
            for p in figure:
                self.draw(canvas, p)

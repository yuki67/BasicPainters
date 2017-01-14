from Painter.Figure import Point, Figure


class Painter(object):
    """ 絵を描くための基底クラス """

    def __init__(self) -> None:
        # draw_functionsで描画に使う関数を指定する
        # 何も指定しなければ、すべて点で描画される(遅い)
        self.draw_functions = {
            Point: self.put_pixel
        }

    def put_pixel(self, canvas, point: Point) -> None:
        """ canvasにpointを描画する """
        assert False, "Override me!"

    def draw(self, canvas, figure: Figure) -> None:
        """ canvasにfigureを描く """
        try:
            self.draw_functions[type(figure)](canvas, figure)
        except KeyError:
            for p in figure:
                self.draw(canvas, p)

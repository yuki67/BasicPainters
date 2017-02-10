from Figure.Figure import Point, Figure


class Painter(object):
    """ 絵を描くための基底クラス """

    def __init__(self) -> None:
        # draw_functionsで描画に使う関数を指定する
        # 何も指定しなければ、すべて点で描画される(遅い)
        self.draw_functions = {
            Point: self.put_pixel
        }

    def put_pixel(self, point: Point) -> None:
        """ canvasにpointを描画する """
        assert False, "Override me!"

    def split_and_draw(self, figure: Figure) -> None:
        """ figureを分解して描く """
        for sub_figure in figure:
            self.draw(sub_figure)

    def draw(self, figure: Figure) -> None:
        """ canvasにfigureを描く """
        self.draw_functions.get(type(figure), self.split_and_draw)(figure)

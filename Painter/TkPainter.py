from tkinter import Canvas
from typing import List

from Figure.Figure import Line, Point
from Painter.Painter import Painter


class TkPainter(Painter):
    """ TkinterのCanvas用のPainter """
    # Canvasの座標系は1始まりなので、例えばLine([1, 1], [1, 100])が表示されないことに注意

    def __init__(self, canvas: Canvas) -> None:
        super().__init__()
        self.canvas = canvas
        self.draw_functions[Line] = self.draw_line

    def draw_line(self, line: Line) -> None:
        """ canvasにlineを描画する """
        self.canvas.create_line([line.a.x + 1, line.a.y + 1, line.b.x + 1, line.b.y + 1],
                                fill="red")

    def put_pixel(self, point: Point) -> None:
        """ canvasにpointを描画する """
        self.canvas.create_rectangle(point.x + 0.5, point.y + 0.5,
                                     point.x + 1.5, point.y + 1.5,
                                     fill=self.x11_from_rgb(point.rgb),
                                     width=0)

    @staticmethod
    def x11_from_rgb(rgb: List[int]) -> str:
        """ 色のRGB表記(R, G, B)を#RGBに直す """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str

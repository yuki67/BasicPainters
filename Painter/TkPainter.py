from tkinter import Canvas
from typing import List

from Painter.Figure import Line, Point
from Painter.Painter import Painter


class TkPainter(Painter):
    """ TkinterのCanvas用のPainter """

    def __init__(self) -> None:
        super().__init__()
        self.draw_functions[Line] = self.draw_line

    def draw_line(self, canvas: Canvas, line: Line) -> None:
        """ canvasにlineを描画する """
        canvas.create_line([line.a.x, line.a.y, line.b.x, line.b.y],
                           fill="red")

    def put_pixel(self, canvas: Canvas, point: Point) -> None:
        """ canvasにpointを描画する """
        canvas.create_rectangle(point.x + 0.5, point.y + 0.5,
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

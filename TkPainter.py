from Painter import Painter
import tkinter


class TkPainter(Painter):

    def put_pixel(self, canvas, point):
        x = point.x
        y = point.y
        canvas.create_rectangle(x + 0.5, y + 0.5, x +
                                1.5, y + 1.5, fill='green')

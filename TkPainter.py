from Painter import Painter
import tkinter


class TkPainter(Painter):

    def put_pixel(self, canvas, point):
        x = point.x
        y = point.y
        canvas.create_rectangle(x + 0.5, y + 0.5, x +
                                1.5, y + 1.5, fill=self.x11_from_rgb(point.rgb),
                                width=0)

    @staticmethod
    def x11_from_rgb(rgb):
        """
        色のRGB表記(R, G, B)をX11表記(#RGB)に直す
        """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str

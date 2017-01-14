from Painter.Painter import Painter


class TkPainter(Painter):
    """ TkinterのCanvas用のPainter """

    def __init__(self):
        super().__init__()
        # self.draw_functions[Line] = self.draw_line

    def draw_line(self, canvas, line):
        canvas.create_line([line.a.x, line.a.y, line.b.x, line.b.y],
                           fill="red")

    def put_pixel(self, canvas, point):
        canvas.create_rectangle(point.x + 0.5, point.y + 0.5,
                                point.x + 1.5, point.y + 1.5,
                                fill=self.x11_from_rgb(point.rgb),
                                width=0)

    @staticmethod
    def x11_from_rgb(rgb):
        """ 色のRGB表記(R, G, B)を#RGBに直す """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str

from PIL import Image, ImageDraw

from Painter.Figure import Point
from Painter.Painter import Painter


class JPGPainter(Painter):
    """ PillowのImage用のPainter """

    def __init__(self, img: Image.Image=None) -> None:
        super().__init__()
        self.canvas = img
        self.drawer = ImageDraw.Draw(img)

    def put_pixel(self, point: Point) -> None:
        """ canvasにpointを描画する """
        if 0 <= point.x < self.canvas.width and 0 <= point.y < self.canvas.height:
            self.canvas.putpixel((int(point.x), int(point.y)),
                                 tuple(point.rgb))

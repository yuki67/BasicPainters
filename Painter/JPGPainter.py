from PIL import Image

from Painter.Figure import Point
from Painter.Painter import Painter


class JPGPainter(Painter):
    """ PillowのImage用のPainter """

    def __init__(self) -> None:
        super().__init__()

    def put_pixel(self, canvas: Image, point: Point) -> None:
        """ canvasにpointを描画する """
        if 0 <= point.x < canvas.width and 0 <= point.y < canvas.height:
            canvas.putpixel((int(point.x), int(point.y)),
                            tuple(point.rgb))

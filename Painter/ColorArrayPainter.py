from Painter.Figure import Point, ColorArray
from Painter.Painter import Painter


class ColorArrayPainter(Painter):
    """ 色配列を作ったりいじったりするためのクラス """

    def __init__(self) -> None:
        super().__init__()

    def put_pixel(self, canvas: ColorArray, point: Point) -> None:
        """
        座標(x, y)の色をrgbにする
        (x, y)が領域の外だったら何もしない
        """
        if 0 < point.x < len(canvas[0]) and 0 < point.y < len(canvas):
            canvas[int(point.y)][int(point.x)].rgb = point.rgb

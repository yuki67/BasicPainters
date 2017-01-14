from Painter.Painter import Painter


class ColorArrayPainter(Painter):
    """ 色配列を作ったりいじったりするためのクラス """

    def __init__(self):
        super().__init__()

    def put_pixel(self, canvas, point):
        """
        座標(x, y)の色をrgbにする
        (x, y)が領域の外だったら何もしない
        """
        if point.x > 0 and point.y > 0 and point.x < len(canvas[0]) and point.y < len(canvas):
            canvas[int(point.y)][int(point.x)].rgb = point.rgb

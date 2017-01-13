from Painter import Painter


class ColorArrayPainter(Painter):
    """ 色配列を作ったりいじったりするためのクラス """

    def put_pixel(self, canvas, point):
        """
        座標(x, y)の色をrgbにする
        (x, y)が領域の外だったら何もしない
        """
        if point.x < 0 or point.y < 0:
            return canvas
        width = len(canvas[0])
        height = len(canvas)
        if point.x < width and point.y < height:
            canvas[int(point.y)][int(point.x)] = point.rgb
        return canvas

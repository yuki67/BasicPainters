class Painter(object):

    def put_pixel(self, canvas, point):
        """
        canvasの座標(x,y)をrgbに塗る
        """
        assert False, "Override me!"

    def draw(self, canvas, figure):
        """
        canvasにfigureを描く
        """
        for p in figure.get_points():
            self.put_pixel(canvas, p)

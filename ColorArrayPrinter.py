class ColorArrayPrinter(object):
    """
    色配列を描画するための基底クラス
    """

    def print(self, color_array):
        """
        color_arrayを使って絵を描く
        """
        self.open(color_array)
        for x_array in color_array:
            for rgb in x_array:
                self.put_pixel(rgb)
            self.new_line()
        self.close()

    def open(self, color_array):
        """
        ファイルを(おそらくはself.fileに)開いて、初期設定を行う
        初期設定に使う情報を得るためにcolor_arrayも渡される
        """
        assert False, "Override me!"

    def put_pixel(self, rgb):
        """
        座標(self.x, self.y)をrgbの色で塗る
        描かれる順番は
        (0,0)->(0,1)->...->(0,n)->
        (1,0)->(1,1)->...->(1,n)->
        .................->(m,n)
        で決まっている。(シェルに出力するときにこの順番の方が良いため)
        """
        assert False, "Override me!"

    def new_line(self):
        """
        ファイルに改行を加える
        文字が記録される場合を想定した関数なので、何もしなくて済むこともあると思う
        """
        assert False, "Override me!"

    def close(self):
        """
        ファイルを閉じ、セーブする
        """
        assert False, "Override me!"

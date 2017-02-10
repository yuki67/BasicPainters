from typing import List

from ColorArray.ColorArrayPrinter import ColorArrayPrinter
from Figure.Figure import ColorArray, Point


class HtmlArrayPrinter(ColorArrayPrinter):
    """ HTMLでお絵かきするためのクラス """

    def __init__(self, filename: str) -> None:
        super().__init__()
        self.cell_width = None
        self.cell_height = None
        self.filename = filename + ".html"
        self.str = ""

    def open(self, color_array: ColorArray) -> None:
        """ 初期設定を行う """
        self.str += "<html>\n" + \
                    "<head><title>" + self.filename[:-5] + "</title></head>\n" + \
                    "<body><table width=\"10\" height=\"10\" border=\"0\" cellspacing=\"0\" >\n" + \
                    "<tr>\n"

    def put_pixel(self, point: Point) -> None:
        """ pointを描画する """
        self.str += "<th bgcolor=\"%s\"/>" % \
                    (self.color_code_from_rgb(point.rgb))

    def new_line(self) -> None:
        """ 行を改める """
        self.str += "</tr>\n<tr>"

    def close(self) -> None:
        """ ファイルを閉じる """
        self.str += "</body></html>"
        file = open(self.filename, "w+")
        file.write(self.str)
        file.close()

    @staticmethod
    def color_code_from_rgb(rgb: List[int]) -> str:
        """ 色のRGB表記(R, G, B)を#RGBに直す """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str

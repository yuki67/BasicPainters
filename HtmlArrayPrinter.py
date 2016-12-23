from ColorArrayPrinter import ColorArrayPrinter


class HtmlArrayPrinter(ColorArrayPrinter):
    """
    HTMLでお絵かきするためのクラス
    """

    def __init__(self, filename):
        super().__init__()
        self.cell_width = None
        self.cell_height = None
        self.filename = filename + ".html"

    def open(self, color_array):
        self.cell_width = int(100 / len(color_array[0]))  # パーセント
        self.cell_height = int(100 / len(color_array))  # パーセント
        self.file = open(self.filename, "w+")
        self.file.write("<html>\n" +
                        "<head><title>" + self.filename[:-5] + "</title></head>\n" +
                        "<body><table width=\"100%%\" height=\"100%%\ border=\"0\" cellspacing=\"0\" >\n" +
                        "<tr>\n")

    def put_pixel(self, rgb):
        self.file.write("<th bgcolor=\"%s\" width=\"%s%%\" height=\"%s%%\"></th>" %
                        (self.color_code_from_rgb(rgb), self.cell_width, self.cell_width))

    def new_line(self):
        self.file.write("</tr>\n<tr>")

    def close(self):
        self.file.write("</body></html>")
        self.file.close()

    @staticmethod
    def color_code_from_rgb(rgb):
        """
        色のRGB表記(R, G, B)をX11表記(#RGB)に直す
        r,g,bは0から255
        """
        r_str = hex(rgb[0])[2:].rjust(2, '0')
        g_str = hex(rgb[1])[2:].rjust(2, '0')
        b_str = hex(rgb[2])[2:].rjust(2, '0')
        return "#" + r_str + g_str + b_str

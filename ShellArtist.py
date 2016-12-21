import openpyxl
from ColorArrayArtist import ColorArrayArtist


class ShellArtist(ColorArrayArtist):
    """
    シェルでお絵かきするためのクラス
    """

    def __init__(self, filename):
        super().__init__()
        self.filename = filename + ".sh"

    def open(self, color_array):
        self.file = open(self.filename, "w+")
        self.file.write("#!/bin/bash\n")
        self.file.write("echo -e \"")
        return

    def put_pixel(self, rgb):
        color_number = self.clamp(rgb)
        self.file.write("\\e[48;5;%sm  " % color_number)

    def new_line(self):
        self.file.write("\\n")

    def close(self):
        self.file.write("\\e[48;5;0m\"")
        self.file.close()

    def clamp(self, rgb):
        return rgb[0] % 255

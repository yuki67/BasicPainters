# -*- coding: utf-8 -*-
""" 画像描画のデモ """
import argparse
import os
import tkinter
from PIL import Image

from ColorArray.ExcelArrayPrinter import ExcelArrayPrinter
from ColorArray.HtmlArrayPrinter import HtmlArrayPrinter
from ColorArray.ShellArrayPrinter import ShellArrayPrinter
from Painter.Figure import ColorArray
from Painter.TkPainter import TkPainter
from Painter.JPGPainter import JPGPainter


def make_parser() -> argparse.ArgumentParser:
    """
    パーサーを作って、パーサーを返す。
    返り値に直接parse_arg()することが前提になっている。
    """
    parser = argparse.ArgumentParser(description="Make files from image.")
    parser.add_argument(dest="filename", action="store",
                        help="Configure path to the image.")
    parser.add_argument("-n", dest="width", default=200, action="store",
                        help="Configure the width of generating image.")
    return parser


def print_array(array: ColorArray, filename: str) -> None:
    """ arrayPainterを使ってarrayを描く """
    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)


def setup_tk(width: int, height: int) -> (tkinter.Tk, tkinter.Canvas):
    """ Tkのrootとcanvasを作って返す """
    root = tkinter.Tk()
    root.title("Tk Painter")
    root.geometry("%dx%d+%d+%d" % (width + 10, height + 10, 256, 0))
    canvas = tkinter.Canvas(root, width=width, height=height)
    return root, canvas


def prompt() -> None:
    """ メイン処理 """
    args = make_parser().parse_args()
    array = ColorArray.from_image(args.filename, int(args.width))
    filename = os.path.join("images",
                            os.path.basename(args.filename).split(".")[0])
    if not os.path.exists("images"):
        os.mkdir("images")

    # ArrayPrinter
    print_array(array, filename)
    resize = ColorArray.resize(array, 100)
    print_array(resize, filename + "_resize")

    # JPGPainter
    img = Image.new("RGB", (len(array[0]), len(array)), "white")
    JPGPainter(img).draw(array)
    img.save(filename + ".jpg")

    # TkPainter
    root, canvas = setup_tk(len(array[0]), len(array))
    TkPainter(canvas).draw(array)
    canvas.place(x=5, y=5)
    root.mainloop()
    print("program ended.")

if __name__ == "__main__":
    prompt()

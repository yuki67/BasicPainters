# -*- coding: utf-8 -*-
import argparse
import os
import tkinter

from ColorArray.ExcelArrayPrinter import ExcelArrayPrinter
from ColorArray.HtmlArrayPrinter import HtmlArrayPrinter
from ColorArray.ShellArrayPrinter import ShellArrayPrinter
from Painter.Figure import ColorArray
from Painter.TkPainter import TkPainter


def make_parser():
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


def setup_tk(width, height):
    """ Tkのrootとcanvasを作って返す """
    root = tkinter.Tk()
    root.title("Tk Painter")
    root.geometry("%dx%d+%d+%d" % (width + 10, height + 10, 256, 0))
    canvas = tkinter.Canvas(root, width=width, height=height)
    return root, canvas

def prompt():
    """ メイン処理 """
    args = make_parser().parse_args()
    array = ColorArray.from_image(args.filename, args.width)

    # ArrayPrinter
    filename = os.path.join("images",
                            os.path.basename(args.filename).split(".")[0])
    if not os.path.exists("images"):
        os.mkdir("images")

    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)

    resize = ColorArray.resize(array, 100)
    HtmlArrayPrinter(filename + "_resize").print(resize)
    ExcelArrayPrinter(filename + "_resize").print(resize)
    ShellArrayPrinter(filename + "_resize").print(resize)

    # TkPainter
    root, canvas = setup_tk(len(array[0]), len(array))
    TkPainter().draw(canvas, array)
    canvas.place(x=5, y=5)
    root.mainloop()
    print("program ended.")


prompt()

# -*- coding: utf-8 -*-
import argparse
import os
import tkinter
from math import sin, cos, pi
from Figure import Point, Line, Circle, Ellipse, Diamond, Polygon
import ColorArray
from TkPainter import TkPainter
from ColorArrayPainter import ColorArrayPainter
from ExcelArrayPrinter import ExcelArrayPrinter
from ShellArrayPrinter import ShellArrayPrinter
from HtmlArrayPrinter import HtmlArrayPrinter


def make_parser():
    """
    パーサーを作って、パーサーを返す。
    返り値に直接parse_arg()することが前提になっている。
    """
    parser = argparse.ArgumentParser(description="Make excel from image.")
    parser.add_argument(dest="filename", action="store",
                        help="Configure path to the image.")
    parser.add_argument("-n", dest="width", default=200, action="store",
                        help="Configure the width of generationg image.")
    return parser


def test_image(args):
    """
    画像をロードする関数のテスト
    """
    array = ColorArray.load_image(args.filename, args.width)
    filename = os.path.splitext(args.filename)[0]

    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)

    array = ColorArray.change_size(array, 100)
    HtmlArrayPrinter(filename + "_resized").print(array)
    ExcelArrayPrinter(filename + "_resized").print(array)
    ShellArrayPrinter(filename + "_resized").print(array)

    print("image test ended.")


def test_figure(canvas, painter):
    """
    図形描画のテスト
    """
    p = [Point(1, 1, [0, 0, 0]),
         Point(canvas.width - 1, 1, [255, 255, 0]),
         Point(canvas.width - 1,
               canvas.height - 1, [255, 0, 255]),
         Point(1, canvas.height - 1, [0, 255, 255])]
    """
    Line, Polygon
    """
    painter.draw(canvas, Polygon(p))
    painter.draw(canvas, Line(p[0], p[2]))
    painter.draw(canvas, Line(p[1], p[3]))

    """
    Eillipe,Circle
    """
    center = Point(canvas.width / 2,
                   canvas.height / 2, [0, 255, 0])
    painter.draw(canvas, Circle(center, canvas.width / 4))
    center.rgb = [0, 0, 255]
    painter.draw(canvas, Ellipse(
        center, canvas.width / 4, canvas.width / 2))
    center.rgb = [255, 0, 0]
    painter.draw(canvas, Ellipse(
        center, canvas.width / 2, canvas.width / 4))

    """
    Diamond
    """
    painter.draw(canvas,
                 Diamond(center,
                         canvas.width / 2, 16,
                         lambda t: [128 + 127 * sin(2 * pi * t),
                                    128 + 127 * cos(2 * pi * t),
                                    128 + 127 * sin(2 * pi * t) * cos(2 * pi * t)]),)
    canvas.place(x=5, y=5)


def setup_tk(width, height):
    """
    Tkのrootとcanvsを作って返す
    """
    root = tkinter.Tk()
    root.title("Tk Painter")
    root.geometry("%dx%d+%d+%d" % (width + 10, height + 10, 256, 0))
    canvas = tkinter.Canvas(root, width=width, height=height)
    canvas.width = width
    canvas.height = height
    return root, canvas


def prompt():
    """
    対話処理など
    """
    args = make_parser().parse_args()

    """
    TkPainter
    """
    root, canvas = setup_tk(512, 512)
    test_figure(canvas, TkPainter())
    root.mainloop()
    # test_figure(args)
    # test_image(args)
    print("program ended.")

prompt()

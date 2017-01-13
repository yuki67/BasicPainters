# -*- coding: utf-8 -*-
import argparse
import os
import tkinter
from math import sin, cos, pi
from Figure import Point, Line, Circle, Ellipse, Diamond, Polygon
from ColorArray import colorarray_blank, colorarray_load_image, colorarray_resize
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
                        help="Configure the width of generating image.")
    return parser


def test_image(args):
    """
    画像をロードする関数のテスト
    """
    array = colorarray_load_image(args.filename, args.width)
    filename = os.path.splitext(args.filename)[0]

    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)

    array = colorarray_load_image(array, 100)
    HtmlArrayPrinter(filename + "_resize").print(array)
    ExcelArrayPrinter(filename + "_resize").print(array)
    ShellArrayPrinter(filename + "_resize").print(array)

    print("image test ended.")


def test_figure(canvas, painter, width, height):
    """
    図形描画のテスト
    """
    p = [Point(1, 1, [0, 0, 0]),
         Point(width - 1, 1, [255, 255, 0]),
         Point(width - 1,
               height - 1, [255, 0, 255]),
         Point(1, height - 1, [0, 255, 255])]
    """
    Line, Polygon
    """
    painter.draw(canvas, Polygon(p))
    painter.draw(canvas, Line(p[0], p[2]))
    painter.draw(canvas, Line(p[1], p[3]))

    """
    Ellipse,Circle
    """
    center = Point(width / 2,
                   height / 2, [0, 255, 0])
    painter.draw(canvas, Circle(center, width / 4))
    center.rgb = [0, 0, 255]
    painter.draw(canvas, Ellipse(
        center, width / 4, width / 2))
    center.rgb = [255, 0, 0]
    painter.draw(canvas, Ellipse(
        center, width / 2, width / 4))

    """
    Diamond
    """
    painter.draw(canvas,
                 Diamond(center,
                         width / 2, 16,
                         lambda t: [128 + 127 * sin(2 * pi * t),
                                    128 + 127 * cos(2 * pi * t),
                                    128 + 127 * sin(2 * pi * t) * cos(2 * pi * t)]),)


def test_array_printer(canvas, filename):
    ExcelArrayPrinter(filename).print(canvas)
    ShellArrayPrinter(filename).print(canvas)
    HtmlArrayPrinter(filename).print(canvas)


def setup_tk(width, height):
    """
    Tkのrootとcanvasを作って返す
    """
    root = tkinter.Tk()
    root.title("Tk Painter")
    root.geometry("%dx%d+%d+%d" % (width + 10, height + 10, 256, 0))
    canvas = tkinter.Canvas(root, width=width, height=height)
    return root, canvas


def prompt():
    """
    対話処理など
    """
    args = make_parser().parse_args()

    """
    ArrayPainter
    """
    width, height = 100, 100
    canvas = colorarray_blank(width, height)
    test_figure(canvas, ColorArrayPainter(), width, height)
    test_array_printer(canvas, "figures")

    canvas = colorarray_load_image(args.filename, width)
    filename = os.path.splitext(args.filename)[0]
    test_array_printer(canvas, filename)
    test_array_printer(colorarray_resize(canvas, 50), filename)

    """
    TkPainter
    """
    width, height = 512, 512
    root, canvas = setup_tk(512, 512)
    test_figure(canvas, TkPainter(), width, height)
    canvas.place(x=5, y=5)

    root.mainloop()

    # test_figure(args)
    # test_image(args)
    print("program ended.")

prompt()

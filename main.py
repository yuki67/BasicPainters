# -*- coding: utf-8 -*-
import argparse
import os
import tkinter
from Figure import Point, Line, Circle
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


def test_figure(args):
    """
    図形描画のテスト
    """
    painter = ColorArrayPainter()
    array = ColorArray.blank_colorarray(args.width, args.width)

    p = [Point(0, 0, [0, 0, 0]),
         Point(args.width, 0, [255, 255, 0]),
         Point(args.width, args.width, [255, 0, 255]),
         Point(0, args.width, [0, 255, 255])]

    painter.draw(array, Line(p[0], p[1]))
    painter.draw(array, Line(p[1], p[2]))
    painter.draw(array, Line(p[2], p[3]))
    painter.draw(array, Line(p[3], p[0]))
    painter.draw(array, Line(p[0], p[2]))
    painter.draw(array, Line(p[1], p[3]))

    circle = Circle(Point(args.width / 2, args.width /
                          2, [0, 255, 0]), args.width / 2)
    painter.draw(array, circle)

    ExcelArrayPrinter("figure").print(array)
    ShellArrayPrinter("figure").print(array)
    HtmlArrayPrinter("figure").print(array)
    print("figure test ended.")


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


def test_tk(args):
    width = 512
    height = 512
    root = tkinter.Tk()
    root.title("Tk Painter")
    root.geometry("%dx%d+%d+%d" % (width, height, 256, 0))
    canvas = tkinter.Canvas(root, width=width, height=height)
    p = [Point(0, 0, [0, 0, 0]),
         Point(width - 1, 0, [255, 255, 0]),
         Point(width - 1, height - 1, [255, 0, 255]),
         Point(0, height - 1, [0, 255, 255])]

    painter = TkPainter()
    painter.draw(canvas, Line(p[0], p[1]))
    painter.draw(canvas, Line(p[1], p[2]))
    painter.draw(canvas, Line(p[2], p[3]))
    painter.draw(canvas, Line(p[3], p[0]))
    painter.draw(canvas, Line(p[0], p[2]))
    painter.draw(canvas, Line(p[1], p[3]))

    circle = Circle(Point(width / 2, height / 2, [0, 255, 0]), args.width / 2)
    painter.draw(canvas, circle)
    canvas.place(x=0, y=0)
    root.mainloop()


def prompt():
    """
    対話処理など
    """
    args = make_parser().parse_args()
    # test_figure(args)
    # test_image(args)
    test_tk(args)
    print("program ended.")

prompt()

# -*- coding: utf-8 -*-
import argparse
import os
from Figure import Point, Line, Circle
from ColorArray import ColorArray
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
    parser.add_argument("-n", dest="width", default=50, action="store",
                        help="Configure the width of generationg image.")
    return parser


def prompt():
    """
    対話処理など
    """
    arg = make_parser().parse_args()
    painter = ColorArrayPainter()

    array = ColorArray(100, 100)
    # array = ColorArray.load_image(arg.filename, arg.width)
    filename = os.path.splitext(arg.filename)[0]

    p = [Point(0, 0, [0, 0, 0]),
         Point(99, 0, [255, 255, 0]),
         Point(99, 99, [255, 0, 255]),
         Point(0, 99, [0, 255, 255])]

    painter.draw(array, Line(p[0], p[1]))
    painter.draw(array, Line(p[1], p[2]))
    painter.draw(array, Line(p[2], p[3]))
    painter.draw(array, Line(p[3], p[0]))
    painter.draw(array, Line(p[0], p[2]))
    painter.draw(array, Line(p[1], p[3]))

    circle = Circle(Point(50, 50, [0, 255, 0]), 50)
    painter.draw(array, circle)

    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)
    print("ended.")

prompt()

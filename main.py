# -*- coding: utf-8 -*-
import argparse
import os
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

    array = ColorArrayPainter.load_image(arg.filename, int(arg.width))

    filename = os.path.splitext(arg.filename)[0]

    for y in range(0, array.height, 5):
        for x in range(0, array.width, 5):
            array.put_pixel(x, y, (255, 0, 0))

    excel_printer = ExcelArrayPrinter(filename)
    excel_printer.draw(array)

    shell_printer = ShellArrayPrinter(filename)
    shell_printer.draw(array)

    html_printer = HtmlArrayPrinter(filename)
    html_printer.draw(array)
    print("ended.")

prompt()

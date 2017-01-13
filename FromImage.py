# -*- coding: utf-8 -*-
import argparse
import os
from ColorArray.ColorArray import colorarray_load_image, colorarray_resize
from ColorArray.ExcelArrayPrinter import ExcelArrayPrinter
from ColorArray.HtmlArrayPrinter import HtmlArrayPrinter
from ColorArray.ShellArrayPrinter import ShellArrayPrinter


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


def prompt():
    """ メイン処理 """
    args = make_parser().parse_args()

    array = colorarray_load_image(args.filename, args.width)

    filename = os.path.join(
        "images", os.path.basename(args.filename).split(".")[0])
    if not os.path.exists("images"):
        os.mkdir("images")
    ExcelArrayPrinter(filename).print(array)
    ShellArrayPrinter(filename).print(array)
    HtmlArrayPrinter(filename).print(array)

    array = colorarray_resize(array, 100)
    HtmlArrayPrinter(filename + "_resize").print(array)
    ExcelArrayPrinter(filename + "_resize").print(array)
    ShellArrayPrinter(filename + "_resize").print(array)

    print("program ended.")

prompt()

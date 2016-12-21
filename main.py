# -*- coding: utf-8 -*-
import argparse
import os
from ColorArray import ColorArray
from ExcelArtist import ExcelArtist
from ShellArtist import ShellArtist
from HtmlArtist import HtmlArtist


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

    array = ColorArray()
    color_array = array.load_image(arg.filename, int(arg.width))

    filename = os.path.splitext(arg.filename)[0]

    excel_artist = ExcelArtist(filename)
    excel_artist.draw(color_array)

    shell_artist = ShellArtist(filename)
    shell_artist.draw(color_array)

    html_artist = HtmlArtist(filename)
    html_artist.draw(color_array)
    print("ended.")

prompt()

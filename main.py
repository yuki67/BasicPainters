# -*- coding: utf-8 -*-
import argparse
import os
from ColorArray import ColorArray
from ExcelArtist import ExcelArtist


def make_parser():
    """
    パーサーを作って、パーサーを返す。
    返り値に直接parse_arg()することが前提になっている。
    """
    parser = argparse.ArgumentParser(description="Make excel from image.")
    parser.add_argument(dest="filename", action="store",
                        help="Configure path to the image.")
    return parser


def prompt():
    """
    対話処理など
    """
    arg = make_parser().parse_args()
    filename = os.path.splitext(arg.filename)[0] + ".xlsx"
    artist = ExcelArtist(filename)
    array = ColorArray()
    color_array = array.load_image(arg.filename, 100)
    artist.draw(color_array)
    print("ended.")

prompt()

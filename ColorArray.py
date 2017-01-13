"""
二次元の色配列をいじるための関数
"""


def colorarray_blank(height, width):
    """
    [255, 255, 255](白)に初期化された横width, 縦heightの色配列を返す
    """
    array = []
    for _ in range(height):
        array.append([])
        for _ in range(width):
            array[-1].append([255, 255, 255])
    return array


def colorarray_resize(array, width):
    """
    arrayを幅widthに縮小して返す
    """
    return from_source(width, len(array[0]), len(array), lambda x, y: array[int(y)][int(x)])


def colorarray_load_image(filename, width):
    """
    画像から色配列を作って返す
    widthは出来上がる色配列の幅
    """
    from PIL import Image

    image = Image.open(filename)
    w, h = image.size
    return from_source(width, w, h, lambda x, y: image.getpixel((int(x), int(y))))


def from_source(width, source_width, source_height, sampler):
    """
    samplerを使って幅widthの色配列を作って返す
    sampler: [0, source_width] * [0, source_height] -> RGB
    """
    height = width / source_width * source_height
    diff_x = (source_width - 1) / (width - 1)
    diff_y = (source_height - 1) / (height - 1)

    x = 0
    y = 0
    array = []
    while y <= source_height:
        array.append([])
        x = 0
        while x <= source_width:
            array[-1].append(sampler(x, y))
            x += diff_x
        y += diff_y
    return array

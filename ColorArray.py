from PIL import Image


class ColorArray(list):
    """
    色配列を作ったりいじったりするためのクラス。
    """

    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0

    def put_pixel(self, x, y, rgb):
        """
        座標(x, y)の色をrgbにする
        (x, y)が領域の外だったら何もしない
        """
        if x < self.width and y < self.height:
            self[y][x] = rgb

    @staticmethod
    def load_image(filename, width):
        """
        画像から色配列を作る。
        widthは出来上がる色配列のx方向の要素数。
        """
        image = Image.open(filename)
        original_width, original_height = image.size
        height = width / original_width * original_height
        diff_x = (original_width - 1) / (width - 1)
        diff_y = (original_height - 1) / (height - 1)

        x = 0
        y = 0
        array = ColorArray()
        while y <= original_height:
            array.append([])
            x = 0
            while x <= original_width:
                color = image.getpixel((int(x), int(y)))
                array[-1].append(color)
                x += diff_x
            y += diff_y
        array.width = len(array[0])
        array.height = len(array)
        return array

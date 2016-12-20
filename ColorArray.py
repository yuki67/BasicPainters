from PIL import Image


class ColorArray(list):
    """
    色配列を作ったりいじったりするためのクラス。
    """

    def __init__(self):
        super().__init__()

    def load_image(self, filename, width):
        """
        画像から色配列を作る。
        widthは出来上がる色配列のx方向の要素数。
        すなわち、width == len(from_image(filename, width)[0])
        """
        image = Image.open(filename)
        original_width, original_height = image.size
        height = width / original_width * original_height
        diff_x = (original_width - 1) / (width - 1)
        diff_y = (original_height - 1) / (height - 1)

        x = 0
        y = 0
        self = []
        while y <= original_height:
            self.append([])
            x = 0
            while x <= original_width:
                color = image.getpixel((int(x), int(y)))
                self[-1].append(color)
                x += diff_x
            y += diff_y
        return self

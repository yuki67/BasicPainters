from PIL import Image


class ColorArray(list):
    """
    二次元の色配列
    """

    def __init__(self, height, width):
        """
        [255, 255, 255](白)に初期化された横width, 縦heightの色配列を返す
        """
        array = []
        for _ in range(height):
            array.append([])
            for _ in range(width):
                array[-1].append([255, 255, 255])
        super().__init__(array)

    @staticmethod
    def load_image(filename, width):
        """
        画像から色配列を作って返す
        widthは出来上がる色配列のx方向の要素数
        """
        image = Image.open(filename)
        original_width, original_height = image.size
        height = width / original_width * original_height
        diff_x = (original_width - 1) / (width - 1)
        diff_y = (original_height - 1) / (height - 1)

        x = 0
        y = 0
        array = []
        while y <= original_height:
            array.append([])
            x = 0
            while x <= original_width:
                color = image.getpixel((int(x), int(y)))
                array[-1].append(color)
                x += diff_x
            y += diff_y
        return array

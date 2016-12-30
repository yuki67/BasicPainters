from math import sin, cos


class Point(object):
    """
    図形を扱うときの基本となる点
    """

    def __init__(self, x, y, rgb=None):
        """
        座標が(x,y)で色がrgbの点を返す
        """
        self.x = x
        self.y = y
        if rgb is not None:
            rgb[0] = int(rgb[0])
            rgb[1] = int(rgb[1])
            rgb[2] = int(rgb[2])
        self.rgb = rgb

    def interpolate(self, b, r):
        """
        selfとbをr:(1-r)に内分する点を返す(0<r<1)
        r = 0 で self
        r = 1 で b
        """
        x = (b.x - self.x) * r + self.x
        y = (b.y - self.y) * r + self.y
        rgb = [0, 0, 0]
        if self.rgb is not None:
            rgb[0] = (b.rgb[0] - self.rgb[0]) * r + self.rgb[0]
            rgb[1] = (b.rgb[1] - self.rgb[1]) * r + self.rgb[1]
            rgb[2] = (b.rgb[2] - self.rgb[2]) * r + self.rgb[2]
        return Point(x, y, rgb)


class Figure(object):
    """
    図形の基底クラス
    """

    def get_points(self):
        """
        図形の表す点が詰まったリストを返す
        """
        assert False, "Override me!"


class Line(Figure):
    """
    線分
    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_points(self):
        winner = int(max(abs(self.a.x - self.b.x), abs(self.a.y - self.b.y)))
        ans = []
        for i in range(winner):
            ans.append(Point.interpolate(self.a, self. b, i / winner))
        return ans


class Polygon(Figure):
    """
    多角形
    """

    def __init__(self, points):
        self.points = points

    def get_points(self):
        ans = []
        for i in range(len(self.points)):
            ans += Line(self.points[i - 1], self.points[i]).get_points()
        return ans


class Ellipse(Polygon):
    """
    楕円
    """

    def __init__(self, center, a, b):
        # 全体の色はcenter.rgbで指定される
        points = []
        for i in range(0, 64):
            t = 2 * 3.14159 / 64 * i
            points.append(Point(a * cos(t) + center.x,
                                b * sin(t) + center.y,
                                center.rgb))
        super().__init__(points)


class Circle(Ellipse):
    """
    円
    """

    def __init__(self, center, r):
        super().__init__(center, r, r)

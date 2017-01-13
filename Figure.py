from math import ceil, floor, pi, sin, cos
from itertools import chain


def circular_points(center, r, n, color=lambda t: [0, 0, 0]):
    """ 円周上の点へのイテレータを返す """
    return (Point(r * cos(2 * pi * i / n) + center.x,
                  r * sin(2 * pi * i / n) + center.y,
                  color(i / n)) for i in range(n))


class Point(object):
    """ 図形を扱うときの基本となる点 """

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
        """ selfとbをr:(1-r)に内分する点を返す(0<r<1) """
        # r = 0 で self
        # r = 1 で b
        x = (b.x - self.x) * r + self.x
        y = (b.y - self.y) * r + self.y
        rgb = [0, 0, 0]
        if self.rgb is not None:
            rgb[0] = (b.rgb[0] - self.rgb[0]) * r + self.rgb[0]
            rgb[1] = (b.rgb[1] - self.rgb[1]) * r + self.rgb[1]
            rgb[2] = (b.rgb[2] - self.rgb[2]) * r + self.rgb[2]
        return Point(x, y, rgb)


class Figure(object):
    """ 図形の基底クラス """
    pass


class Line(Figure):
    """ 線分 """

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.stopper = max(abs(self.a.x - self.b.x), abs(self.a.y - self.b.y))

    def __iter__(self):
        return (Point.interpolate(self.a, self.b, i / self.stopper) for i in range(int(self.stopper)))


class Polygon(Figure):
    """ 多角形 """

    def __init__(self, points):
        self.points = points
        self.stopper = len(points)

    def __iter__(self):
        return (Line(self.points[i - 1], self.points[i]) for i in range(self.stopper))


class Ellipse(Figure):
    """ 楕円 """

    def __init__(self, center, a, b):
        # 全体の色はcenter.rgbで指定される
        self.center = center
        self.a = a
        self.b = b
        self.x_range = ceil((a**2 + b**2)**-0.5 * a ** 2)
        self.y_range = ceil((a**2 + b**2)**-0.5 * b ** 2)
        self.y = lambda x: b * (1 - (x / a)**2)**0.5
        self.x = lambda y: a * (1 - (y / b)**2)**0.5

    def __iter__(self):
        return chain((Point(self.center.x + x,
                            self.center.y + self.y(x),
                            self.center.rgb)
                      for x in range(-self.x_range, self.x_range)),
                     (Point(self.center.x + x,
                            self.center.y - self.y(x),
                            self.center.rgb)
                      for x in range(-self.x_range, self.x_range)),
                     (Point(self.center.x + self.x(y),
                            self.center.y + y,
                            self.center.rgb)
                      for y in range(-self.y_range, self.y_range)),
                     (Point(self.center.x - self.x(y),
                            self.center.y + y,
                            self.center.rgb)
                      for y in range(-self.y_range, self.y_range)))


class Circle(Ellipse):
    """ 円 """

    def __init__(self, center, r):
        super().__init__(center, r, r)


class Diamond(Figure):
    """ ダイヤモンドパターン """

    def __init__(self, center, r, n, color=lambda t: [0, 0, 0]):
        self.circle = lambda: circular_points(center, r, n, color)

    def __iter__(self):
        return (Line(p, q) for p in self.circle() for q in self.circle())

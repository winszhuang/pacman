# 12:00 ~ 2:00


# 遊戲中的一個
class Element:

    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    # 是否碰撞
    def is_collision(self, element):
        if isinstance(element, Element):
            return self.x == element.x and self.y == element.y
        else:
            raise ValueError(
                "Parameter 'element' must be an instance of Element class")

    # 是否靠近
    def is_adjacent_to(self, element):
        if isinstance(element, Element):
            distance = abs(self.x - element.x) + abs(self.y - element.y)
            return distance == 1
        else:
            raise ValueError(
                "Parameter 'element' must be an instance of Element class")


class Pacman(Element):

    def __init__(self, x, y):
        super().__init__(x, y, "🌝")


# class Engine:
#     def __init__(self):
#         self.pacman = Pacman(3, 3)
#         # self.wallList =
#     def run(self):
#         # while True:

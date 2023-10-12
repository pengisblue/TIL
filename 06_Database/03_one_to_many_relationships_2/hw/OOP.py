class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Nemo:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

P1 = Point(0, 0)
P2 = Point(2, 2)

nemo = Nemo(P1, P2)

print(nemo.p1.x)
print(nemo.p1.y)
print(nemo.p2.x)
print(nemo.p2.y)

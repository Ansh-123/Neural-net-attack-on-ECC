import copy
import time


class point:

    def __init__(self, x, y, order, a, b):
        self.x = x
        self.y = y
        self.order = order
        self.a = a
        self.b = b

    # Adds point Q to self, returns new point object - or original point
    def add(self, Q):
        if self.x is None and self.y is None:
            return Q
        if Q.x is None and Q.y is None:
            return self
        if (Q.x == self.x + self.y) and Q.x == Q.y:
            return point(None, None, self.order, self.a, self.b)
        if Q.x - self.x == 0:
            return point(None, None, self.order, self.a, self.b)
        else:
            # solve for slope
            inv = pow((Q.x - self.x) % self.order, -1, self.order)
            m = ((Q.y - self.y) * inv) % self.order
            rx = (m**2 - Q.x - self.x) % self.order
            ry = (m*(self.x - rx) - self.y) % self.order
            return point(rx, ry, self.order, self.a, self.b)

    # doubles point self, returns new point object - or self
    def double(self):
        if (self.x is None) and (self.y is None):
            return self
        elif self.y == 0:
            return point(None, None, self.order, self.a, self.b)
        else:
            inv = pow((self.y * 2) % self.order, -1, self.order)
            m = (((3*(self.x**2)) + self.a) * inv) % self.order
            rx = (m**2 - 2 * self.x) % self.order
            ry = (m*(self.x - rx) - self.y) % self.order
            return point(rx, ry, self.order, self.a, self.b)

    def multiply(self, d):
        bin = '{0:b}'.format(d)[::-1]
        base = copy.deepcopy(self)
        temp = point(None, None, self.order, self.a, self.b)
        for i in bin:
            if i == "1":
                temp = temp.add(base)
            base = base.double()
        return temp


if __name__ == "__main__":
    start = time.time()

    for i in range(10000):
        test = point(3, 6, 7919, 2, 3).multiply(i)
        print(test.x, test.y)
    end = time.time()

    print(end - start)
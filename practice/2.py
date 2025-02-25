class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2

    # def set_coords(self):
    #     print('вызов метода set_coords' + str(self))

    def set_coords(self, x, y):
        self.x = x
        self.y = y
    
    def get_coords(self):
        return(self.x, self.y)

# print(Point.set_coords)
# Point.set_coords()

# pt = Point()

# pt.set_coords()       [одно и то же  с Point.set_coords(pt)]
# Point.set_coords(pt)  [одно и то же с pt.set_coords()]

# работаем с def set_coords(self, x, y):
pt = Point()
pt.set_coords(1, 2)
print(pt.__dict__)

pt2 = Point()
pt2.set_coords(10, 20)
print(pt2.__dict__)

# работаем с def get_coords(self):

pt = Point()
pt.set_coords(1, 2)
print(pt.get_coords())

f = getattr(pt, 'get_coords')
print(f)
print(f())
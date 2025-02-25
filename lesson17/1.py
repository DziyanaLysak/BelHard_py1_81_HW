class Point:
    "Класс для представления координат на плоскости"
    color = 'red'
    circle = 2
    # dd = "ff"


Point.color = 'black'
Point.circle

Point.__dict__


print(Point.color)
print(Point.circle)
print(Point.__dict__)
print(Point.color)

a = Point()
b = Point()
#print(type(a))
#type(b) == Point
print(isinstance(b, Point))

Point.circle = 1
print(Point.circle)

print(b.__dict__)

print(a.color)

print(b.circle)
a.color = "green"

print(a.color)

print(a.__dict__)
print(b.__dict__)

Point.type_pt = "disc"
#print(Point.__dict__)
setattr(Point, "prop", 1)

#print(Point.__dict__)

setattr(Point, "type_pt", "square")
#print(Point.__dict__)

print(Point.circle)

res = Point.circle
print(res)

print(getattr(Point, 'a', False))
print(getattr(Point, 'color', False))
# print(getattr(Point, 'dd'))

# del Point.dd
print(getattr(Point, 'dd', False))

print(hasattr(Point, 'type_pt'))

delattr(Point, "type_pt")
print(hasattr(Point, 'type_pt'))
print("функция getattr")
print(getattr(Point, 'color'))
print(getattr(a, 'color'))
print(a.__dict__)
#print(hasattr(a, 'color'))

a = Point()
b = Point()
a.x = 1
a.y = 2
b.x = 10
b.y = 20

print(a.__dict__)

print(Point.__dict__)
print(Point.__doc__)
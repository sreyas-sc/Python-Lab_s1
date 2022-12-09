from graphics import rectangle, circle
from graphics.graphics_3d import cuboid
from graphics.graphics_3d.sphere import area as sphere_area

radius = float(input('Enter radius of circle:'))
print('Area of circle:', circle.area(radius))

length = float(input('Enter length of the rectangle:'))
breadth = float(input('Enter breadth of the rectangle:'))
print('Area of rectangle:', rectangle.area(length, breadth))

radius = float(input('Enter radius of sphere:'))
print('Area of sphere:', sphere_area(radius))


length = float(input('Enter length of the cuboid:'))
width = float(input('Enter width of the cuboid:'))
height = float(input('Enter height of the cuboid:'))
print('Area of cuboid:', cuboid.area(length, width, height))

import math


PI = 22/7


class Square:
    def area(side):
        return side*side

    def perimeter(side):
        return 4*side
    
    def diagonal(side):
        return math.sqrt(2)*side


class Rectangle:
    def area(length, breadth):
        return length*breadth

    def perimeter(length, breadth):
        return 2*(length + breadth)

    def diagonal(length, breadth):
        return math.sqrt(length**2 + breadth**2)


class Circle:
    def deg2rad(degree):
        return degree*PI/180

    def area(radius):
        return PI*radius**2

    def circumference(radius):
        return 2*PI*radius

    def sector(radius, central_angle):
        return (central_angle/360)*(PI*radius**2)

    def segment(radius, central_angle):
        return (1/2)*(radius**2)*(central_angle - math.sin(central_angle))

    def chord(radius, central_distance):
        return 2*math.sqrt(radius**2 - (central_distance/2)**2)


class Triangle:
    def area(base, height):
        return (1/2)*base*height
    
    def area(a, b, angle):
        return (1/2)*a*b*math.sin(angle)
    
    def heronsFormula(a, b, c):
        s = (a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    def perimeter(side):
        return 3*side
    
    def perimeter(common_side, third_side):
        return 2*common_side + third_side
    
    def perimeter(a, b, c):
        return a+b+c
    
    def isCongruent(self, **kwargs):
        for (key, value) in kwargs.items:
            if key == "side":
                if(self.value[0] == value[0], self.value[1] == value[1], self.value[2] == value[2]):
                    return True
                else:
                    return False
                
            elif key == "angle":
                pass

    def isSimilar():
        pass


class Parallelogram:
    def perimeter(side1, side2):
        return 2*(side1 + side2)
    
    def area(base, height):
        return base*height
    
    def area(a, b, angle):
        return a*b*math.sin(angle)


class Rhombus:
    def perimeter(side):
        return 4*side
    
    def area(diagonal1, diagonal2):
        return (1/2)*diagonal1*diagonal2


class Trapezium:
    def perimeter(side1, side2, side3, side4):
        return side1 + side2 + side3 + side4
    
    def area(side1, side2, height):
        return (1/2)*(side1 + side2)*height


class Kite:
    def perimeter(shorterSide, longerSide):
        return 2*(shorterSide + longerSide)
    
    def area(diagonal1, diagonal2):
        return (1/2)*diagonal1*diagonal2


class Cube:
    def surfaceArea(side):
        return 6*side*side
    
    def areaOfFourWalls(side):
        return 4*side*side

    def volume(side):
        return side**3
    
    def diagonal2D(side):
        return math.sqrt(2)*side
    
    def diagonal3D(side):
        return math.sqrt(3)*side


class Cuboid:
    def surfaceArea(length, breadth, height):
        return 2*(length*breadth + breadth*height + height*length)
    
    def areaOfFourWalls(length, breadth, height):
        return 2*(length*height + breadth*height)

    def volume(length, breadth, height):
        return length*breadth*height

    def diagonal2D(length, breadth):
        return math.sqrt(length**2 + breadth**2)
    
    def diagonal3D(length, breadth, height):
        return math.sqrt(length**2 + breadth**2 + height**2)



class Cylinder:
    def diagonal(radius, height):
        return ((2*radius)**2 + height**2)**0.5

    def totalSurfaceArea(radius, height):
        return 2*PI*radius*(height + radius)
    
    def curvedSurfaceArea(radius, height):
        return 2*PI*radius*height

    def volume(radius, height):
        return PI*radius*radius*height


class Cone:
    def slantHeight(radius, height):
        return (height**2 + radius**2)**0.5
    
    def totalSurfaceArea(radius, slantHeight):
        return PI*radius*(slantHeight + radius)
    
    def curvedSurfaceArea(radius, slantHeight):
        return PI*radius*slantHeight

    def volume(radius, height):
        return (1/3)*PI*radius*radius*height


class Frustum:
    def slantHeight(baseRadius, topRadius, height):
        return (height**2 + (baseRadius - topRadius)**2)**0.5
    
    def totalSurfaceArea(baseRadius, topRadius, slantHeight):
        return PI*slantHeight*(baseRadius + topRadius) + PI*baseRadius**2 + PI*topRadius**2
    
    def curvedSurfaceArea(baseRadius, topRadius, slantHeight):
        return PI*slantHeight*(baseRadius + topRadius)
    
    def volume(baseRadius, topRadius, height):
        return (1/3)*PI*height*(baseRadius**2 + baseRadius*topRadius + topRadius**2)


class Sphere:
    def surfaceArea(radius):
        return 4*PI*radius*radius
    
    def volume(radius):
        return (4/3)*PI*radius**3


class Hemisphere:
    def surfaceArea(radius):
        return 2*PI*radius*radius
    
    def volume(radius):
        return (2/3)*PI*radius**3


class Tetrahedron:
    pass


class Parallelopiped:
    pass



import math

PI = 22/7

class Square:
    def area(side):
        return side*side

    def perimeter(side):
        return 4*side

class Rectangle:
    def area(length, breadth):
        return length*breadth

    def perimeter(length, breadth):
        return 2*(length + breadth)

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
        return 2*(radius**2 - (central_distance/2)**2)**0.5
from math import tan, pi
a = int (input("Input number of sides: "))
b = int (input("Input the length of a side: "))
area = a * b * b / ( 4 * tan(pi/a))
area1 = area // 1
print("The area of the polygon is: ", area1)

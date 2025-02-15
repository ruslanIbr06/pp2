import math

#1 Write a Python program to convert degree to radian.
degrees = int(input("Enter degrees: "))
print(f"{degrees} degrees equals to {math.radians(degrees):.5f} radians")
'''
Enter degrees: 15
15 degrees equals to 0.26180 radians
'''

#2 Write a Python program to calculate the area of a trapezoid.
h = int(input("Enter the height: "))
baseFirst = int(input("Enter first base value: "))
baseSecond = int(input("Enter second base value: "))
print(f'Area of trapezoid with height {h}, and bases {baseFirst} and {baseSecond} equals to {((baseFirst+baseSecond)*h)/2:.2f}')
'''
Enter the height: 5
Enter first base value: 5
Enter second base value: 6
Area of trapezoid with height 5, and bases 5 amd 6 equals to 27.5
'''
#3 Write a Python program to calculate the area of regular polygon.

sides = int(input("Enter the number of sides: "))
length = int(input("Enter the length of one side: "))
result = (sides * length**2)/(4*math.tan(math.pi / sides))


print(f'Area of polygon with {sides} sides with length {length} is {result:.2f}')
'''
Enter the number of sides: 4
Enter the length of one side: 25
Area of polygon with 4 sides with length 25 is 625.00
'''

#4 Write a Python program to calculate the area of a parallelogram.
baseLength = int(input("Enter the length of a base: "))
height =  int(input("Enter the height: "))

print(f'The area of parallelogram with base {baseLength} and height {height} is {baseLength * height}')
'''
Enter the length of a base: 5
Enter the height: 6
The area of parallelogram with base 5 and height 6 is 30
'''
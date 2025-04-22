length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than or equal to area")

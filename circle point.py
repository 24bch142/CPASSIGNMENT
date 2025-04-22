import math
cx, cy = map(int, input("Enter circle center (cx cy): ").split())
r = float(input("Enter radius of the circle: "))
px, py = map(int, input("Enter point coordinates (px py): ").split())
distance = math.sqrt((px - cx) ** 2 + (py - cy) ** 2)
if distance < r:
    print("Point is inside the circle")
elif distance == r:
    print("Point is on the circle")
else:
    print("Point is outside the circle")

import math

x_degrees = float(input("Enter x in degrees: "))
x = math.radians(x_degrees)  # Convert degrees to radians

sin_x = sum((-1)**i * (x**(2*i + 1)) / math.factorial(2*i + 1) for i in range(10))
print("sin(x):", sin_x)

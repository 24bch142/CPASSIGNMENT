import math

n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))
nCr = math.comb(n, r)  
nPr = math.perm(n, r)  
print(f"nCr: {nCr}, nPr: {nPr}")

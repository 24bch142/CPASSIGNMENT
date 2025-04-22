num = int(input("Enter a number: "))

# Prime check
is_prime = num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
print("Prime:", is_prime)

# Perfect number check
is_perfect = num == sum(i for i in range(1, num) if num % i == 0)
print("Perfect:", is_perfect)

# Armstrong number check
digits = [int(d) for d in str(num)]
is_armstrong = num == sum(d ** len(digits) for d in digits)
print("Armstrong:", is_armstrong)

# Palindrome check
is_palindrome = str(num) == str(num)[::-1]
print("Palindrome:", is_palindrome)

# Automorphic number check
is_automorphic = str(num) == str(num**2)[-len(str(num)):]
print("Automorphic:", is_automorphic)

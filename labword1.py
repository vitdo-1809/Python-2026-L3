#ex1
r = float(input("Enter circle radius:"))
pi = 3.14
area = (r **2 ) * pi
print("the area of a circle ", area)


#ex2
c = float(input("Enter the temperature in Celsius:"))
f = c * 9 / 5 + 32
print(f"{c} (C) = {f} (F)")


#ex3
n = int(input("Enter a number? "))
prime = n > 1

for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        prime = False
        break

if prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a NOT prime number")


#ex4
n = int(input("Enter a number? "))
divisors_sum = sum(i for i in range(1, n) if n % i == 0)

if divisors_sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is a NOT perfect number")

#ex5
colors = ["White", "Black", "Blue", "Red", "Yellow","Pink"]

color = input("What is your favorite color? ")

if color in colors:
    print(f"Your color is at index {colors.index(color)} in my list")
else:
    print("Sorry, I could not find your color")


#ex6
range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", range1)
print("range2:", range2)
print("range3:", range3)
print("range4:", range4)


    #ex7
s = input("enter dollar money:")
def remove_dollar_sign(s):
  return s.replace("$", "")
print(remove_dollar_sign(s))


#ex8
def extract_even(l):
    return [x for x in l if x % 2 == 0]
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,36]
print(extract_even(l))


#ex9
n = int(input("Enter a nonnegative integer: "))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(n))


#ex10
n = int(input("enter a number:"))
def get_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]
print(get_divisors(n))


#ex11
import math

x1, y1 = map(float, input("Enter x1, y1? ").split())
x2, y2 = map(float, input("Enter x2, y2? ").split())

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = {distance}")


#ex12
m, n = map(int, input("Enter m, n? ").split())
def print_pattern(m, n):
    for row in range(m):
        if row == 0 or row == m - 1:
            print("* " * n)
        else:
            print("*" + " " * (2 * (n - 1) - 1) + "*")

print_pattern(m, n)
'''First of all enter coefficients, if it has no number, then go 1, consider negative ones'''
import equation_parse as ep
print(__doc__)

# ep.sayHi()

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = (b ** 2) - (4 * a * c)
print(d)
if d < 0:
    print(f'Discriminant is less than 0 so it has no roots \nD = {d}')
elif d == 0:
    print(f'Discriminant is zero so it has only one root')
    x1 = (-b + (d ** 0.5)) / (2 * a)
    print(round(x1, 3))
else:
    print(f"Discriminant is greater than 0 \nD = {d}")
    print('Find the equation roots')
    x1 = (-b + (d ** 0.5)) / (2 * a)
    x2 = (-b - (d ** 0.5)) / (2 * a)
    print(f'x1 = {round(x1, 3)} \nx2 = {round(x2, 3)}')

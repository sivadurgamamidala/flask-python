def square(x):
    return x*x
def cube(y):
    return y*y*y
def power4(z):
    return z*z*z*z
print("Squares of number 0 - 9:")
for i in range(10):
    print("{} square is {}".format(i, square(i)))
print("cubes of number 0 - 9:")
for i in range(10):
    print("{} cube is {}".format(i, cube(i)))
for i in range(10):
    print("{} power(4) is {}".format(i, power4(i)))
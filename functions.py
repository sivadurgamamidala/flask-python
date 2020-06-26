def square(x):
    return x*x
def cube(y):
    return y*y*y
print("Squares of number 0 - 9:")
for i in range(10):
    print("{} square is {}".format(i, square(i)))
print("cubes of number 0 - 9:")
for i in range(10):
    print("{} cube is {}".format(i, cube(i)))
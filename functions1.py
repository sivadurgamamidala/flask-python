def square(x):
    return x*x
def cube(y):
    return y*y*y
def main():
    print("Squares of number 0 - 9:")
    for i in range(10):
        print("{} square is {}".format(i, square(i)))
def main1():
    print("cubes of number 0 - 9:")
    for i in range(10):
        print("{} cube is {}".format(i, cube(i)))
if __name__ == "__main__": #this means only we can call main when name == main
    main()
if __name__ == "__main1__": #this means only we can call main when name == main1
    main1()
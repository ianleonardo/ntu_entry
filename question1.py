def swap(x, y):
    # check if x and y is numeric
    if not( (type(x) is int or type(x) is float) and
            (type(y) is int or type(y) is float) ):
        return -1

    # swapping the values of 2 variables using comma operator
    x, y = y, x

    # printing values after swapping
    print("value of x after swapping : ", x)
    print("value of y after swapping : ", y)

    return


swap("Apple", 10)
swap(9, 17)

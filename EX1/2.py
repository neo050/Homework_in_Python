def PrimeInrange(num1):
    """
    A function that finds prime numbers in a given range
    :param num1: the range
    :return:the prime num in the range
    """
    if num1 == 2 or num1 == 3:
        return 'prime'
    a1 = [2]
    test = True
    for i in range(3, num1 + 1):
        for j in range(2, i):
            if i % j == 0:
                test = False
                break
        if test:
            a1.append(i)
        test = True
    if 1 == a1.count(num1):
        return 'prime'
    return a1


def factorSum(Integer):
    """
    This function returns the sum of the multiplication factors of the prime numbers in any integer greater than one
    :param Integer: An integer greater than one
    :return: The product of the primary factors
    """
    if isinstance(Integer, int):
        assert Integer > 1, f'Integer={Integer} should be bigger than 1'
        answer = PrimeInrange(Integer)
        sum = 0
        if answer == 'prime':
            return Integer
        for i in range(len(answer)):
            if Integer % answer[i] == 0:
                sum += answer[i]

        return sum
    else:
        print("Error input only Integer > 1  !!!")


print("The program expects to get an integer greater than one,The plan will return the sum of the primary factors in "
      "the number.")
print("If you want to stop the program, insert non-digit input.")

while True:
    integer = input("Enter only integer > 1 !!")
    if integer.isdigit():
        assert int(integer) > 1, f'Integer={integer} should be bigger than 1'
        print(factorSum(int(integer)))
    else:
        break


def f(x):
    """
    This function accepts a number and returns a number with the addition of one
    :param x:
    :return: x+1
    """
    return x + 1


def onlyPositive(func):
    """
    This function returns the activation of the function f when it sends the parameter to it in absolute value
    :param func:The function parameter is the function f
    :return: the func positve
    """

    def positve(x):
        return func(abs(x))

    return positve


g = onlyPositive(f)

while True:
    num = input("Enter numbers for func g (ex2). to stop the program, insert non-digit input")
    if num.replace(".", "").replace("-", "").isdigit():
        print(g(float(num)))
    else:
        break


def interceptPoint(tuple1, tuple2):
    """
    A function that receives two points that represent a definition of two lines and returns the point of intersection
     between them if any
    :param tuple1: tuple
    :param tuple2: tuple
    :return:Returns the point of intersection if any other returns None
    """
    if tuple1[0] == tuple2[0]:
        return None
    x = (tuple2[1] - tuple1[1]) / (tuple1[0] - tuple2[0])
    y = x * tuple1[0] + tuple1[1]
    point = (x, y)
    return point


print("to stop the program, insert non-digit input")
while True:
    m1, m2 = input("Please enter the slope of the line1:"), input("Please enter the slope of the line2:")
    n1, n2 = input("Please enter the free number of the equation line1:"), input("Please enter the free number of the "
                                                                                 "equation line2:")
    if m1.replace(".", "").replace("-", "").isdigit() and m2.replace(".", "").replace("-", "").isdigit() and n1.replace(
            ".", "").replace("-", "").isdigit() and n2.replace(".", "").replace("-", "").isdigit():

        print(interceptPoint((float(m1), float(n1)), (float(m2), float(n2))))
    else:
        break


def printNumbers(StaRange, EndRange, numInRange):
    """
    A recursive function called printNumbers that accepts 3 parameters: domain start, domain end and number. On
The function is to print all the numbers from the domain except the number it received, each number
 printed in a separate line.

    :param StaRange:
    :param EndRange:
    :param numInRange:
    :return: The function does not return values
    """
    if StaRange == EndRange:
        if StaRange != numInRange:
            print(StaRange)
    if StaRange > EndRange:
        if StaRange != numInRange:
            print(StaRange)
        printNumbers(StaRange - 1, EndRange, numInRange)
    if StaRange < EndRange:
        if StaRange != numInRange:
            print(StaRange)
        printNumbers(StaRange + 1, EndRange, numInRange)


printNumbers(1, 5, 3)
printNumbers(2, -3, -1)


def arrProduct(arr1, arr2):
    """
    A function that receives two equal-order arrays of non-negative integers. On the function
Return a thread of subsets, where each subset is a value from the first array as the number of times in the place number
Corresponding in the second array
    :param arr1: list
    :param arr2: list
    :return: new list
    """
    arr6 = []
    for i in range(len(arr2)):
        j = arr2[i]
        while j > 0:
            arr6.append(arr1[i])
            j -= 1
    return arr6


arr = [6, 7, 8]
arr3 = [0, 7, 8]
print(arrProduct(arr, arr3))


def analyze(charArr):
    """
    A function called analyze that receives a string consisting of real numbers that represent a number
Mm of rain that fell in different months. Returns the number of months in which over 75 mm of rain fell in them.
    :param charArr:
    :return: Several months fulfilling the condition
    """
    count1 = 0
    for c in charArr.replace(" ", "").split(","):
        if float(c) > 75.0:
            count1 += 1
    return count1


print(analyze("45,65, 70.4, 82.6, 20.1, 90.8, 76.1, 67.1, 79.9"))

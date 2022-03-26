from random import randint

# Remember how to use this kind of variable?
count = 0

def main():
    print("Welcome to Recursion Fun")

    # aggienacci calculation
    value = eval(input("Enter a number to find it's aggienacci value: "))
    print("The aggienacci value of " + str(value) + " is " + str(round(aggienacci(value), 4)))

    print()

    # Recursive search and sort
    key = eval(input("Enter a number to search for: "))
    numList = []
    for i in range(200000):
        if randint(0, 2) == 0:
            numList.append(i)

    numPos = binarySearch(numList, key)

    if numPos == -1:
        print("Your number, " + str(key) + ", is not in the list")
    else:
        print("Your number, " + str(key) + ", is in the list at position " + str(numPos))

    print("Total recursive calls: " + str(count))

def aggienacci(value):
    global count
    count += 1
    if value == 0:
        return 0
    elif value == 1:
        return 1
    elif value == 2:
        return 2
    else:
        return (aggienacci(value - 3) + aggienacci(value - 2)) / aggienacci(value - 1)


def binarySearch(numList, key):
    global count
    count = 0
    low = 0
    high = len(numList) - 1
    return binarysearchLogic(numList, key, low, high)


def binarysearchLogic(numList, key, low, high):
    global count
    count += 1
    if high < low:
        return -1
    middle = (high + low) // 2
    if key == numList[middle]:
        return middle
    elif key < numList[middle]:
        return binarysearchLogic(numList, key, low, middle - 1)
    else:
        return binarysearchLogic(numList, key, middle + 1, high)

main()

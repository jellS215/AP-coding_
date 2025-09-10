numberList = [1, 5, 10, 20, 39, 48, 83, 89 ,72, 90]
value = 90
value2 = 1
def numberSearch(numberList, value):
    for x in numberList:
        if x==value:
            print("found the largest number, the largest number is 90")
            break
        else:
            print("not the largest number")
    for x in numberList:
        if x==value2:
            print("found the smallest number, the smallest number is 1")
            break
        else:
            print("not the smallest number")
            
numberSearch(numberList, value)
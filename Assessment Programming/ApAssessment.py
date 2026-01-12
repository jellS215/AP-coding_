num1 = 3
num2 = 7
num3 = 10


def calculate_average():
    num1 = 3
    num2 = 7
    num3 = 10
    avg = (num1 + num2 + num3) / 3
    return avg

print("The average is:", calculate_average())

def val():
    x = 10
    y = 20
    x = y
    y = x
    val = x + y
    return val

print("The value is:", val())

def count():
    count = 0
    for i in range(4):
        count += 2
        return count
    print(count)
    

def scores():
    scores = [85, 90, 75]
    scores.insert(2, 80)
    return scores

print(scores())


def calculate(n):
    if n < 5:
        return n * 2
    else:
        return n + 10

print("Calculate result:", calculate(3))

list = [1, 2, 3]
value = list[1]

for x in list: 

 if (x > value): 

  value = x 

print(value)  
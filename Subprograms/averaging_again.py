def hello():
    name = input("What's your name? ")
    print(f"Hello {name}, I hope you're doing well!")
    return name


def average(numbers):
    return sum(numbers) / len(numbers)


def numbers():
    running, numbers = True, []
    while (running):
        num = input("Number: ")
        if (num == "Q"):
            running = False
        else:
            numbers.append(float(num))

    return numbers


def result(average, name):
    print(f"Hey {name}, the result of the calculation is {average}!")


name = hello()
nums = numbers()
avg = average(nums)
result(avg, name)

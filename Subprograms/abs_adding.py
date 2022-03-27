def num_sum(*numbers):
    return sum([abs(num) for num in numbers])


a, b = float(input("First number: ")), float(input("Second number: "))
print(f"{a} + {b} = {num_sum(a, b)}")

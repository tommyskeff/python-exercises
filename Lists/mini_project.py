import statistics

count = int(input("How many numbers? "))
numbers = []

for i in range(count):
    numbers.append(int(input(f"Number {i + 1}: ")))

print("\n".join([f"Mean: {round(statistics.mean(numbers), 1)}", f"Median: {statistics.median_low(numbers)}"]))

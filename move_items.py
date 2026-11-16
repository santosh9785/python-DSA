
numbers = [0, 1, 0, 3, 12]

write = 0


for num in numbers:
    if num != 0:
        numbers[write] = num
        write += 1


while write < len(numbers):
    numbers[write] = 0
    write += 1

print(numbers)

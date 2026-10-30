numbers = [1, 2, 3, 2, 1]

left = 0
right = len(numbers) - 1

while left < right:
    if numbers[left] != numbers[right]:
        print("Not palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
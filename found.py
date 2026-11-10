numbers = [15, 7, 22, 9, 31, 4]

found = False
for num in numbers:
    if num == 20:
        found = True
        break
if found:
    print("found")
else:
    print("not found")
    
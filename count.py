n = [2, 5, 2, 8, 2, 5]
count2 = 0
count5 = 0
count8 = 0
for num in n:
    if num == 2:
        count2  +=1
    if num == 5:
        count5 +=1
    if num == 8:
        count8 += 1
print(count2)
print(count5)
print(count8)
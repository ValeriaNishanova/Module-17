multiple = 1
for i in range(1, 11):
    if i % 2 == 0:
        continue
    else:
        multiple *= i
print(multiple)

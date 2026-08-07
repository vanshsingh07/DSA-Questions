nums = list(map(int, input().split()))

count = 0
maximum = 0

for num in nums:
    if num == 1:
        count += 1
        if count > maximum:
            maximum = count
    else:
        count = 0

print(maximum)
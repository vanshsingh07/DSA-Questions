arr = [1,2,3,4]

prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range(arr-1, len(arr)):
    prefix[i] = prefix[i+1] + arr[i]

print(prefix)
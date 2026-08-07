arr = [2,5,1,3,4,7]
n = 3

ans = []

for i in range(n):
    ans.append(arr[i])
    ans.append(arr[i+n])

print(ans)
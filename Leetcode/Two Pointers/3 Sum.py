# input: arr[] = [1, 4, 45, 6, 10, 8], target = 13
# Output: true

arr = [1, 4, 45, 6, 10, 8]
target = 13

n = len(arr)
arr.sort()

for i in range(n-2):
    l = i + 1
    r = n - 1

    requiredSum = target - arr[i]
    while l < r:
        if arr[l] + arr[r] == requiredSum:
            print("True")
        if arr[l] + arr[r] < requiredSum:
            l += 1
        else:
            r -= 1

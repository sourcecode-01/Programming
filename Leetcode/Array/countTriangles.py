# Input: arr[] = [4, 6, 3, 7]
# Output: 3
# Explanation: There are three triangles possible [3, 4, 6], [4, 6, 7] and [3, 6, 7].

arr = [4, 6, 3, 7]

res = 0
arr.sort()

for i in range(2, len(arr)):
    left, right = 0, i - 1

    while left < right:
        if arr[left] + arr[right] > arr[i]:
            res += right - left

            right -= 1
        else:
            left += 1

print(res)

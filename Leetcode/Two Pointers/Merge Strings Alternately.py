# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

word1 = "abc"
word2 = "pqr"

n, m = len(word1), len(word2)
i, j = 0, 0
res = []

while i < n or j < m:
    if i < n:
        res.append(word1[i])
    if j < m:
        res.append(word2[j])
    i += 1
    j += 1

print(''.join(res))
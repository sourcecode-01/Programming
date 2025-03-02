# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
result = defaultdict(list)

for i in strs:
    sorted_list = ''.join(sorted(i))
    result[sorted_list].append(i)

print(list(result.values()))
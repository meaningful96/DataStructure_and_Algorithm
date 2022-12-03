# Deep Learning for AI engineer
"""
Created on Youminkk


Nil sine magno vitae labore dedit mortalibus
"""

# Permutaion 순열 4P2  = 4x3
from itertools import permutations
from itertools import combinations

arr = ['A','B','C']
# 원소 중에서 2개를 뽑는 모든 순열 계산
result1 = list(permutations(arr, 1))
result2 = list(permutations(arr, 2))
result3 = list(permutations(arr, 3))

print(result1)
print(result2)
print(result3)

print()
## Combination 조합 4C2 = (4x3)/(2x1)

arr = ['A','B','C']
result4 = list(combinations(arr, 1))
result5 = list(combinations(arr, 2))
result6 = list(combinations(arr, 3))

print(result4)
print(result5)
print(result6)


from itertools import product

arr = ['A','B','C']

# 원소 중에서 2개를 뽑는 모든 중복 순열 계산
result1 = list(product(arr,repeat = 2))
result2 = list(product(arr,repeat = 3))
result3 = list(product(arr,repeat = 4))

print(result1)
print(result2)
print(result3)

print(len(result1))
print(len(result2))
print(len(result3))


from itertools import combinations_with_replacement

arr = ['A','B','C']

# 원소 중에서 2개를 뽑는 모든 중복 조합 계산
result1 = list(combinations_with_replacement(arr, 2))
result2 = list(combinations_with_replacement(arr, 3))
result3 = list(combinations_with_replacement(arr, 4))

print(result1)
print(result2)
print(result3)
print(len(result1))
print(len(result2))
print(len(result3))


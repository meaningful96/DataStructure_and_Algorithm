"""
Algorithm
2023-08-22
"""

#%% Example 1) Big O

arr = [3,5,1,2,4]
summary = 0

for i in arr:
    summary  += i
    
print(summary)


def for_twice(x: list):
    result = []
    for i in range(len(x)):
        for j in range(len(x)):
            result.append(x[i] * x[j])
    
    return print(result)
#%% Example 2) 수행시간 측정
import time
import numpy as np
x = [np.random.randn(100000000)]
start_time = time.time()

for_twice(x)

end_time = time.time()
print("time:", (end_time - start_time))

#%% Example 3) 선택 정렬 수행 시간 

from random import randint
import time

# 배열에 10,000개의 정수를 삽입
arr = []
for i in range(10000):
    arr.append(randint(1, 100)) # 1 ~ 100사이의 랜덤한 정수

# 선택 정렬 프로그램 시간 측정 시작
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(arr)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(arr)):
        if arr[min_index] > arr[j]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    
end_time = time.time()
print("Running Time:", (end_time - start_time))

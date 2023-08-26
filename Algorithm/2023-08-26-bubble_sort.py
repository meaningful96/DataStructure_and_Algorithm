# %% 버블 정렬의 첫 번째 패스
list = [23,21,22,24,23,27,26]
lastElementsIndex = len(list) - 1
print(0, list)
for idx in range(lastElementsIndex):
    if list[idx] > list[idx + 1]:
        list[idx], list[idx + 1] = list[idx + 1], list[idx]
    print(idx + 1, list )
    

# %% 재사용이 편리하도록 함수로 구현한 버블 정렬 코드
def BubbleSort(list):
    # 리스트에 담긴 데이터를 순서대로 정렬합니다.
    lastElementsIndex = len(list) - 1
    for passNo in range(lastElementsIndex, 0, -1): # range(시작, 끝, 간격)
        for idx in range(passNo):
            if list[idx] > list[idx + 1]:
                list[idx], list[idx + 1] = list[idx + 1], list[idx]
    return list
a = [23,21,22,24,23,27,26]
print(BubbleSort(a))
# %%
def BubbleSort(list):
    for i in range(len(list) - 1):
        swapped = False
        for j in range(i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break

# %%
def BubbleSort(list):
    end = len(list) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                last_swap = i
        end = last_swap

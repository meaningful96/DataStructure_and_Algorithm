# Deep Learning for AI engineer
"""
Created on Youminkk


Nil sine magno vitae labore dedit mortalibus
"""
# %%

import numpy as np

def InsertSort(list):
    for i in range(1, len(list)):
        j = i - 1
        elements_next = list[i]
        while(list[j]> elements_next) and (j>=0):
            list[j+1] = list[j]
            j = j - 1
        list[j + 1] = elements_next
    return list

if __name__ == "__main__":
    # np.random.seed(5)
    list_1 = np.random.randint(0,30,10)
    Out = InsertSort(list_1)
    print(Out)

# %%

def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

## Input
if __name__ == "__main__":
    InputList  = [70,15,25,19,34,44]
    print(InputList)
    OutputList = SelectionSort(InputList)
    print(OutputList)
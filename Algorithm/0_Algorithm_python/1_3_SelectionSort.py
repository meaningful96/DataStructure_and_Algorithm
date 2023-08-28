# Deep Learning for AI engineer
"""
Created on Youminkk


Nil sine magno vitae labore dedit mortalibus
"""

import numpy as np

def SelectionSort(list):
    for i in range(len(list) - 1):
        min_idx = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_idx]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]



if __name__ == "__main__":    
    list_1 = np.random.randint(1,30,10)
    print(list_1)
    SelectionSort(list_1)
    print(list_1)       
            
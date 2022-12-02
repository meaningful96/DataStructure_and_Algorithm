# Deep Learning for AI engineer
def ShellSort(list):
    distance = len(list)//2
    while distance > 0:
        for i in range(distance, len(list)):
            temp = list[i]
            j = i
            # 하위 리스트 안에 든 요소들을 정렬합니다.
            while j >= distance and list[j - distance] > temp:
                j = j - distance
            list[j] = temp
        #다음 패스를 위해 거리를 반으로 줄입니다.
        distance = distance//2
    return list
    
if __name__ == "__main__":
    listIn = [26,17,20,11,23,21,13,18,24,14,12,22,16,15,19,25]
    print(listIn)
    Output = ShellSort(listIn)
    print(Output)
    
    
    

# 그리디 알고리즘(탐욕법)은 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 단순히 가장 좋은 것을 반복적으로 선택해도 최적의 해를 고를 수 있는지 검토해야 한다.

# 문제 1) 거스름돈으로 500원, 100원, 50원, 10원짜리 동전이 무한히 존재
#        거스름돈이 N원일 때 동전의 최소개수. N은 항상 10의 배수

N = 1260
cnt = 0

coin_types = [500, 100 ,50, 10]

for i in range(len(coin_types)):
    tmp = N//coin_types[i]
    cnt += tmp
    N -= tmp*coin_types[i]

print(cnt)
    
# 다른 풀이
for coin in coin_types:
    cnt += N //coin
    N %= coin

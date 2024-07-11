#1부터 45사이의 랜덤한 수 6개 생성
#result 리스트 변수 추가
#랜덤한 수 생성 방법
#import random
#random.randint(a: 1, b: 45)

import random


i = 0
result = []
while i < 6 :
    i = i + 1
    result.append(random.randint(a:1, b:45))
print(result)



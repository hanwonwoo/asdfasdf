#while문을 사용하여 1부터 100까지
#모든 홀수의 합



# i = 0
# a=[]
# while i < 100:
#     i = i + 1
#     if i%2==1:
#         a.append(i)
#
# b=sum(a)
# print(b)



# i = 0
# data = 0
# while i < 100:
#     i = i + 1
#     if i % 2 == 1:
#         data = data + i
# print(data)

# i 변수가 하는 역할 : 수열 만들기, 반복문 제어
index = 1
#result 하는 역할: 연산 결과 값을 저장
result = []
while index < 100 :
    index = index + 1
# 반복되는 수가 홀수인지를 확인
    if index % 2 == 1:
        result.append(index)

# 저장된 값들의 합을 구함
print(sum(result))

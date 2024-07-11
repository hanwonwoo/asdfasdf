#평균값을 구해라
#for 반복문을 사용해라
# my list = [100, 200, 400, 800, 1000, 1300 ]


my_list = [100, 200, 400, 800, 1000, 1300]
result = 0
for i in my_list :
    result = result + i
    #print(i)
    #len(my_list)
avg = result / len(my_list)
print(int(avg))

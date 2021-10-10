import pdb

start = int(input("N ="))
result = 0
num = []
for i in range(0, 1):
    for j in range(1, start+1):
        insert = int(input("정수값을 입력해주세요"))
        if insert >= -100 and insert <= 100:
            num.append(insert)
        else:
            print("정수가 100보다 그거나 -100보다 작습니다. 시발라마 :)")
            break
    abs_sum= 0
    for k in range(0, len(num)):
        if k < len(num):
            result = abs(num[k]-num[k+1])
            #pdb.set_trace()
            abs_sum += result
        else:
            break
            
    #pdb.set_trace()
    break
print(num)
print(result)

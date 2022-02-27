

exp = '123+12'
idx = tuple(3)                      # 7. '123+12' , '3 +' 받음
numA = int(exp[:idx])									# 8. 123+12[:3 +]
numB = int(exp[idx + 1:])								# 9.

print('numA, numB -' ,numA, numB)



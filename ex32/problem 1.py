#-*-coding:utf8
# 1~1000의 수 중 3의 배수이거나 5의 배수인 수에서 1~1000의 수 중 3의 배수이고 5의 배수인 수를 뺀다.
print(sum((x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0))-sum(x for x in range(1, 1000)if x %15 ==0))

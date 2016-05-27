#-*-coding:utf8
# 1~1000의 수 중 3의 배수이거나 5의 배수인 수.
print(sum((x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)))

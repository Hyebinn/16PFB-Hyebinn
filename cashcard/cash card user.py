#-*- coding: utf8 -*-
# 현금카드 모튤을 불러들임

import CashCard as CashCard_module

def chk_bal(message, account):
    """
    Print message and value
    :param message:
    :param account:
    :return:
    """
    print ("%s : %d"%(message, account.check_balance()))

# 현금카드모듈의 잔액확인
chk_bal("CashCard_module 잔액확인", CashCard_module)
# 현금카드에 10000원 입금
print ("1000원 출금")
# ex09cashcard.py 모듈안의 withdrw()함수를 호출
# ex09cashcard.py 모듈의 balance_won 값이 감소
CashCard_module.withdraw(1000)

# ex09cashcard.py 모듈안의 check_balace()함수를 호출
# ex09cashcard.py 모듈의 balance_won 값을 읽어 반환
chk_bal("출금 후 잔고확인", CashCard_module)

# 또다른 현금카드를 만들수있을까? 불러들임
# noinspection pypep8
import  CashCard as mysistersCard_module

chk_bal("CashCard_module 잔액확인", CashCard_module)
chk_bal("mysistersCard_module 잔액확인",mysistersCard_module)

#그러나이식으로는한장의카드만만들수있다
print ("CashCard_module : %s",%CashCard_module)
print("mysistersCard_module : %s", mysistersCard_module)
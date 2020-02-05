'''
Какова сумма цифр числа 2**1000?
'''
def solution(number, power):
    s = 0
    for i in str(number**power):
        s += int(i)
    return s
print(solution(2, 1000))
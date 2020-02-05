'''
Найдите первые десять цифр суммы следующих ста 50-значных чисел.
'''
def solution(number, number1):
    number1 = str(number1)
    cnt = len(number1)
    cnt2 = 0
    sum = 0
    for i in range(0, cnt):
        number1 = str(number1)
        sum += int(number1[i])
    sum2 = []
    for i in range(0, number):
        sum2 = sum2.insert(i, sum[i])
    sum2 = int(sum)
    return sum2

print(solution(2, 999999999955))





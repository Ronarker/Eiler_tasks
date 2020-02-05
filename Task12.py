'''
Каково первое треугольное число, у которого более пятисот делителей?
'''
def solution(divider):
    cnt = 1
    tnumber = 0
    divider1 = 2
    while divider1 <= divider:
        divider1 = 2
        tnumber += cnt
        cnt += 1
        for i in range(2, tnumber):
            if tnumber % i == 0:
                divider1 += 1
    return tnumber
print(solution(5))




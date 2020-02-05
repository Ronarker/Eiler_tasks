'''
Существует только одна тройка Пифагора, для которой a + b + c = 1000.
Найдите произведение abc.
'''
def solution(sum):
    sum1 = 0
    a = 3
    b = 4
    c = 5
    product = 0
    while sum1 != sum:
        if a < b < c and a ** 2 + b ** 2 == c ** 2:
            sum1 = a + b + c
            product = a * b * c
        if a + 1 < b:
            a += 1
        elif b + 1 < c:
            b += 1
        else:
            c += 1
    return product
print(solution(1000))






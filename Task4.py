'''
Найдите самый большой палиндром, полученный умножением двух трехзначных чисел
'''
def solution(bit):
    bit -= 1
    number = 10 ** bit
    limit = 10 ** (bit + 1) - 1
    for i in range(limit, number, -1):
        for n in range(i, number, -1):
            number2 = str(n * i)
            if number2 == number2[::-1]:
                return number2
    return None
print(solution(2))
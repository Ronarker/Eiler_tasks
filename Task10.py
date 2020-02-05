'''
Найдите сумму всех простых чисел меньше двух миллионов.
'''
def solution(number):
    cnt = 0
    for i in range(2, number + 1):
        is_prime = 1
        for k in range(2, i):
            if i % k == 0:
                is_prime = 0
                break
        if is_prime:
            cnt += i
    return (cnt)
print(solution(11))

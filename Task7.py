'''
Какое число является 10001-ым простым числом?
'''
def solution(n):
    m = 0
    number = 1
    while m < n:
        number += 1
        is_prime = True
        for k in range(2, number):
            if number % k == 0:
                is_prime = False
                break
        if is_prime == True:
            m += 1
    return number
print(solution(5))
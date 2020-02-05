def solution(n):
    number = 20
    m = 1
    while m <= n:
        if number % m == 0:
            m += 1
        else:
            m = 1
            number += 20
    return (number)
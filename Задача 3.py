"Простые делители числа 13195 - это 5, 7, 13 и 29.Каков самый большой делитель числа 600851475143, являющийся простым числом?"
def solution(number):
    prime = 2
    for i in range(1, number + 1):
        if number % i == 0:
            is_prime = 1
            for k in range(2, i):
                if i % k == 0:
                    is_prime = 0
                    break
            if is_prime:
                prime = i
    return (prime)
print(solution(13195))


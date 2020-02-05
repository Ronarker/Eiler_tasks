def solution(n):
    sum1 = 0
    sum_of_squares = 0
    for number in range(1, n + 1):
        sum1 += number
    squared_amount = sum1 ** 2
    for number1 in range(1, n + 1):
        sum_of_squares += number1 ** 2
    return(squared_amount - sum_of_squares)



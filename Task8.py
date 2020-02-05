'''
Найдите наибольшее произведение тринадцати последовательных цифр в данном числе.
'''
def solution(number, numbers):
    number = str(number)
    n = 0
    composition1 = 1
    composition = 0
    while numbers + 1 <= len(number):
        for i in range(n, numbers + 1):
            composition1 = composition1 * int(number[i])
        n += 1
        numbers += 1
        if composition1 >= composition:
            composition = composition1
        composition1 = 1
    return composition
print(solution(3642, 2))
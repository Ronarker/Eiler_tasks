'''
Каково наибольшее произведение четырех подряд идущих чисел в таблице 20×20, расположенных в любом направлении (вверх, вниз, вправо, влево или по диагонали)?
'''
def solution(a, b, n):
    import random
    lis = str()
    n =0
    a1 = 0
    b1 = 1
    cnt = 0
    while b1 <= b:
        while a1 < a:
            lis += str(random.randint(1, 99))
            a1 += 1
            cnt += 1
        a1 = 0
        b1 += 1
    lis = list()
    for i in range(2, cnt, 3):
        cnt += 1
        lis.insert(i, ' ')

print(solution(3, 3, 4))
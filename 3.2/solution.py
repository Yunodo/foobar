def solution(l):
    length = len(l)
    counts = [0] * length
    triples = 0
    for product in range(0, length):
        for factor in range(0, product):
            if l[product] % l[factor] == 0:
                counts[product] += 1
                triples += counts[factor]
    return triples






lst = [1,2,4]
print(solution(lst))
#1


lst = [1,2,4,6]
print(solution(lst))
#2

lst = [1,2,4,6,6]
print(solution(lst))
#5


lst = [1,2,4,6,6,6]
print(solution(lst))
#11

lst = [1,2,4,6,6,6,6]
print(solution(lst))
#20

lst = [1,2,4,6,6,6,6,6]
print(solution(lst))
#35

lst = [1,1,2,4,6,6,6,6,6]
print(solution(lst))
#58


lst = [1,1,2,4,6,6,6,6,6,9]
print(solution(lst))
#59
lst = [1,1,2,4,6,6,6,6,6,9,18]
print(solution(lst))
#89

lst = [2, 3, 5, 7, 13, 17, 21, 42, 84]
print(solution(lst))
#8

lst = [1,1,2,4,6,6,6,6,6,9,18,21]
print(solution(lst))
#90


lst = [1,1,1,2,4,6,6,6,6,6,9,18,21]
print(solution(lst))
#134

lst = [1,1,1,1,2,4,6,6,6,6,6,9,18,21]
print(solution(lst))
#189

lst = [3, 9, 22, 50, 100, 200, 999]
print(solution(lst))
#2

lst = [3, 3, 9, 22, 50, 100, 200, 999]
print(solution(lst))
#5

lst = [3, 3, 9, 22, 50, 75, 100, 200, 999]
print(solution(lst))
#6

lst = [3, 3, 9, 22, 50, 75, 100, 150, 200, 999]
print(solution(lst))
#9


lst = [1,1,1]
print(solution(lst))
#1

lst = [1,2,3,4,5,6]
print(solution(lst))
# 3

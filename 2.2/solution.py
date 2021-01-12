def solution(xs):
    mn = -1000
    count = 0
    product = 0
    for element in xs:
        if element != 0:
            if product != 0:
                product = product * element
            else:
                product = element
            count += 1
            if element < 0 and element > mn:
                mn = element
    if product > -1:
        return str(product)
    else:
        if count > 1:
            product = product / mn
            return str(product)
        else:
            if 0 in xs:
                return '0'
            else:
                return str(product)

print(solution([-1]))
print(solution([0]))
print(solution([1]))
print(solution([-1,1]))
print(solution([-1,0]))
print(solution([1,0]))
print(solution([-99,-99]))
print(solution([-1,1,0]))
print(solution([99, 99, -1, -99]))
print(solution([98, 98, -100]))

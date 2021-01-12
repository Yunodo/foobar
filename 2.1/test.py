def to_list(*args):
    """
    Input:
        args - variable number of integers represented as strings, e.g. to_list("15353", "025")

    Output:
        lst - a Python array of lists of strings, e.g. [[1,5,3,5,3],[0,2,5]]
    """
    lst = []
    for string in args:
        lst.append([int(digit) for digit in string])
    return lst



def from_list(*args):
    """
    Input:
        args - variable number of integers represented as lists, e.g. from_list([1,0,2], [5])

    Output:
        new_lst - a Python array of integers represented as strings, e.g. ['102','5']
    """
    new_lst = []
    for lst in args:
        new_string = ''
        for digit in lst:
            new_string += str(digit)
        new_lst.append(new_string)
    return new_lst




def sub(x,y,base):
    """
    Input: x,y  - two integers represented as lists, e.g. x = [3,0,1], y = [0,1,0]
           base - base of numeral system these integers are represented as, e.g. base = 4

    Output:
           new_number - the result of subtraction of two integers in the given base represented as list, e.g. [2,3,1]
    """
    def sub_one(x, base, index):
        if x[index-1] == 0:
            x[index-1] = base - 1
            return sub_one(x,base, index-1)
        else:
            x[index-1] = x[index-1] - 1
            return x
    length = len(x)
    new_number = [0] * length
    for i in range(0,length):
        if x[i] < y[i]:
            new_number = sub_one(new_number, base, i)
            new_number[i] = x[i] + base - y[i]
        else:
            new_number[i] = x[i] - y[i]
    return new_number






def descending(x):
    """
    Input: x - a list of integers, e.g. [2,5,6,0,1,3]

    Output:
           desc - next integer in descending order, e.g. [6]
           desc + descending(x) + ... - a list of integers in descending order, e.g. [6,5,3,2,1,0]
    """
    if len(x) == 0:
        return []
    else:
        mx = max(x)
        desc = [mx]
        x.remove(mx)
    return desc + descending(x)




def solution(n,b):
    x = descending(to_list(str(n))[0])
    y = x[:]
    y.reverse()
    values = [sub(x,y,b)]
    while True:
        print(values)
        temp = values[-1]
        x = descending(temp[:])
        y = x[:]
        y.reverse()
        z = sub(x,y,b)
        if z in values:
            return(len(values) - values.index(z))
        else:
            values.append(sub(x,y,b))

print(solution(210022,3))
print(solution(1502,10))
print(solution(728,10))
print(solution(50283,10))

def solution(n,b):

    def to_list(*args):
        lst = []
        for string in args:
            lst.append([int(digit) for digit in string])
        return lst

    def from_list(*args):
        new_lst = []
        for lst in args:
            new_string = ''
            for digit in lst:
                new_string += str(digit)
            new_lst.append(new_string)
        return new_lst

    def sub(x,y,base):
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
        if len(x) == 0:
            return []
        else:
            mx = max(x)
            desc = [mx]
            x.remove(mx)
        return desc + descending(x)

    x = descending(to_list(str(n))[0])
    y = x[:]
    y.reverse()
    values = [sub(x,y,b)]
    while True:
        temp = values[-1]
        x = descending(temp[:])
        y = x[:]
        y.reverse()
        z = sub(x,y,b)
        if z in values:
            return(len(values) - values.index(z))
        else:
            values.append(sub(x,y,b))

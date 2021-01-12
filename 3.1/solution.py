def solution(map):
    length = 1
    walls = 0
    map[0][0] = 2
    def copy_map(map):
        new_map = []
        for row in map:
            new_map.append(row[:])
        return new_map
    def go(matrix, length, walls, position):
        if matrix[position[0]][position[1]] == 2:
            return 999
        elif matrix[position[0]][position[1]] == 1:
            if walls == 1:
                return 999
            else:
                walls += 1
        length += 1
        if position[0] == (len(matrix) - 1) and position[1] == (len(matrix[0])-1):
            return length
        else:
            matrix[position[0]][position[1]] = 2
            return min(go(matrix, length, walls, (position[0], max(0, position[1] - 1))),go(copy_map(matrix), length, walls, (position[0], min(position[1]+1,len(matrix[0])-1))),go(copy_map(matrix), length, walls, (max(0,position[0] - 1),position[1])),go(copy_map(matrix), length, walls, (min(position[0]+1,len(matrix)-1), position[1])))
    return min(go(map, length, walls, (1,0)),go(copy_map(map), length, walls, (0,1)))

print(solution([[0,0,0,0,0,0],[1,1,1,1,1,0],[0,0,0,0,0,0],[0,1,1,1,1,1],[0,1,1,1,1,1],[0,0,0,0,0,0]]))
#11
print(solution([[0,0,0,1], [1,1,1,1], [0,1,1,1], [0,0,0,0]]))
#7
print(solution([[0,1], [1,0]]))
#3
print(solution([[0,0,0],[1,1,1], [0,1,0]]))
#5
print(solution([[0,0,1,0],[1,1,0,1],[0,1,0,0]]))
#6
print(solution([[0,0,1,1,1], [1,0,1,1,1], [0,0,1,1,1], [0,1,1,1,1], [0,0,0,1,0]]))
#11
print(solution([[0,0,0,0,0,1,0,1,1,1],[0,0,0,1,1,0,1,1,0,0],[0,1,0,1,0,0,0,1,1,0],[0,0,0,1,0,1,0,1,0,1],[1,0,1,0,0,1,0,0,0,0],[0,0,0,0,1,1,0,0,0,0],[1,1,0,0,0,0,1,0,0,0],[1,0,0,1,0,0,1,1,0,1],[1,0,1,0,1,0,1,1,0,1],[1,0,1,0,0,0,0,0,0,0]]))
#19

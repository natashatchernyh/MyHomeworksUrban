def get_matrix(n, m, volume):
    matrix = []
    for i in range(n):            # i = row
        matrix.append([])
        for j in range(m):               # j = column
            matrix[i].append(volume)
            #print(matrix, i, j)
    return matrix

result=get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result)
print(result2)
print(result3)
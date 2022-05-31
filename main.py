matrix = [[6, 1, -1, 2], [2, 14, -4, 5], [4, 7, 16, 3], [-7, 6, 3, 19]]
B = [25, 90, -38, 33]
e = 0

def Jacobi(a, b):
    temp = [0, 0, 0, 0]
    next_temp = [0, 0, 0, -1]
    i = 0
    while abs(sum(list(map(lambda x, y: x - y, temp, next_temp)))) > e:
        for j in range(0, len(b)):
            next_temp[j] = 1 / a[j][j]
            t = 0
            for k in range(0, len(b)):
                if j != k:
                    t -= temp[k] * a[j][k]
            t += b[j]
            next_temp[j] *= t
        i += 1
        print(i, next_temp)
        temp, next_temp = next_temp, temp
    return temp


def Gauss(a, b):
    temp = [0, 0, 0, 0]
    prev_step = temp.copy()
    diff = -1
    i = 0
    while abs(diff) > e:
        for j in range(0, len(b)):
            prev_step = temp.copy()
            temp[j] = 1 / a[j][j]
            t = 0
            for k in range(0, len(b)):
                if j != k:
                    t -= temp[k] * a[j][k]
            t += b[j]
            temp[j] *= t
        diff = abs(sum(list(map(lambda x, y: x - y, temp, prev_step))))
        i += 1
        print(i, temp)
    return temp


if __name__ == "__main__":
    Jacobi(matrix, B)

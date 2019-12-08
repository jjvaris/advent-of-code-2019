n = list(map(int, open("2.txt", "r").readline().split(",")))


def one():
    numbers = n.copy()
    numbers[1] = 12
    numbers[2] = 2
    return execute(numbers, 0)


def execute(n, i):
    if(n[i] == 99):
        return n[0]
    if(n[i] == 1):
        n[n[i+3]] = n[n[i+1]] + n[n[i+2]]
        return execute(n, i+4)
    if(n[i] == 2):
        n[n[i+3]] = n[n[i+1]] * n[n[i+2]]
        return execute(n, i+4)
    else:
        return n[0]
    return execute(n, i+4)


def two():
    for i in range(100):
        for j in range(100):
            numbers = n.copy()
            numbers[1] = i
            numbers[2] = j
            result = execute(numbers, 0)
            if(result == 19690720):
                return 100 * i + j


print("Part one: ", one())
print("Part two: ", two())

numbers = list(map(int, open("2.txt", "r").readline().split(",")))


def one():
    numbers[1] = 12
    numbers[2] = 2
    return execute(0)


def execute(curPos):
    if(numbers[curPos] == 99):
        return numbers[0]
    if(numbers[curPos] == 1):
        numbers[numbers[curPos+3]] = numbers[numbers[curPos+1]] + \
            numbers[numbers[curPos+2]]
        return execute(curPos+4)
    if(numbers[curPos] == 2):
        numbers[numbers[curPos+3]] = numbers[numbers[curPos+1]] * \
            numbers[numbers[curPos+2]]
        return execute(curPos+4)
    return execute(curPos+4)


print("Part one: ", one())

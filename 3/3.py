import sys


file = open("3.txt", "r")
chord1 = file.readline().split(",")
chord2 = file.readline().split(",")


def one():
    intersections = getIntersections()
    m = sys.maxsize
    for c in intersections:
        xy = next(iter(c)).split(',')
        d = abs(int(xy[0])) + abs(int(xy[1]))
        if(d < m and d != 0):
            m = d
    return m


def getCoordinates(chord):
    x = 0
    y = 0
    chordCoordinates = {}
    step = 0
    for i in chord:
        if(i[0] == 'U'):
            for j in range(int(i[1:])):
                chordCoordinates[f"{x},{y}"] = step
                y += 1
                step += 1
        if(i[0] == 'D'):
            for j in range(int(i[1:])):
                chordCoordinates[f"{x},{y}"] = step
                y -= 1
                step += 1
        if(i[0] == 'R'):
            for j in range(int(i[1:])):
                chordCoordinates[f"{x},{y}"] = step
                x += 1
                step += 1
        if(i[0] == 'L'):
            for j in range(int(i[1:])):
                chordCoordinates[f"{x},{y}"] = step
                x -= 1
                step += 1
    return chordCoordinates


def getIntersections():
    c1 = getCoordinates(chord1)
    c2 = getCoordinates(chord2)
    intersections = []
    for k, v in c1.items():
        if(k in c2):
            intersections.append({k: v+c2[k]})
    return intersections


def two():
    intersections = getIntersections()
    return min(filter(lambda x: x != 0, map(
        lambda x: next(iter(x.values())), intersections)))


print("Part one: ", one())
print("Part two: ", two())

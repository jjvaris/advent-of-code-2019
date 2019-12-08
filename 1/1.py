lines = open("1.txt", "r").readlines()
masses = list(map(int, lines))


def one():
    return sum(map(fuelForMass, masses))


def fuelForMass(mass): return int(mass / 3) - 2


def two():
    return sum(map(fuelForMassAndFuel, masses))


def fuelForMassAndFuel(mass, totalFuel=0):
    fuel = fuelForMass(mass)
    if(fuel <= 0):
        return totalFuel
    return fuelForMassAndFuel(fuel, totalFuel + fuel)


print("Part one: ", one())
print("Part two: ", two())

def part1():
    with open('./inputs/day1.txt', "r") as inputs:
        values = list(map(int, inputs))

        for x in values:
            for y in values:
                if x + y == 2020:
                    return print(x*y)


def part2():
    with open('./inputs/day1.txt', "r") as inputs:
        values = list(map(int, inputs))

        for x in values:
            for y in values:
                for z in values:
                    if x + y + z == 2020:
                        return print(x*y*z)


if __name__ == '__main__':
    part1()
    part2()

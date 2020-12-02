def part1():
    with open('./inputs/day2.txt', "r") as inputs:
        each = inputs.readlines()

    valid_passwords = 0

    for i in each:
        numbers = i.split()[0].split("-")
        characters = i.split(":")
        char = characters[0][-1:]
        password = characters[1].strip(" \n")

        count = 0

        for x in password:
            if x == char:
                count += 1

        if not (count < int(numbers[0]) or count > int(numbers[1])):
            valid_passwords += 1

    return print(valid_passwords)


def part2():
    with open('./inputs/day2.txt', "r") as inputs:
        each = inputs.readlines()

    valid_passwords = 0

    for i in each:
        numbers = i.split()[0].split("-")
        characters = i.split(":")
        char = characters[0][-1:]
        password = characters[1].strip(" \n")

        valid = []
        pos = 0
        for x in password:
            pos += 1
            if x == char:
                if str(pos) in numbers:
                    valid.append(pos)

        if len(valid) > 1 or len(valid) == 0:
            pass
        else:
            if str(valid[0]) in numbers:
                valid_passwords += 1

    return print(valid_passwords)


if __name__ == '__main__':
    part1()
    part2()

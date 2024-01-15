import re
import math
from winpwn import *

context.newline = "\n"

p = remote("chal.tuctf.com", 30009)

p.recvuntil("Action: ")
p.sendline("F")
p.recvline()


def find_all(s):
    return list(map(int, re.findall(r'\d+', s)))


class Room:
    def __init__(self, x, y, z):
        self.point = (x, y, z)
        self.numbers = []

    def is_coprime(self):
        numbers = self.numbers
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if math.gcd(numbers[i], numbers[j]) != 1:
                    return False
        return True

    def print(self):
        print(self.numbers)


def parse_room():
    p.recvline()
    p.recvline()
    p.recvline()

    data = p.recvuntil("Action: ").split("\n")

    top = find_all(data[2])[0]
    left, front, right = find_all(data[13])
    bottom = find_all(data[24])[0]
    # print(top, left, front, right, bottom)

    p.sendline("L")
    p.recvline()

    p.recvline()
    p.recvline()
    p.recvline()
    data = p.recvuntil("Action: ").split("\n")

    behind = find_all(data[13])[0]

    p.sendline("R")
    p.recvuntil("Action: ")

    return (top, left, front, right, bottom, behind)


rooms = [[[Room(x, y, z) for z in range(6)] for y in range(6)]
         for x in range(6)]

for z in range(6):
    for y in range(6):
        for x in range(6):
            top, left, front, right, bottom, behind = parse_room()

            xm = x - 1
            ym = y - 1
            zm = z - 1
            xp = x + 1
            yp = y + 1
            zp = z + 1

            if xm == -1:
                xm = 5
            if ym == -1:
                ym = 5
            if zm == -1:
                zm = 5
            if xp == 6:
                xp = 0
            if yp == 6:
                yp = 0
            if zp == 6:
                zp = 0

            top_room = rooms[x][y][zp]
            top_room.numbers.append(top)
            bottom_room = rooms[x][y][zm]
            bottom_room.numbers.append(bottom)

            left_room = rooms[x][yp][z]
            left_room.numbers.append(left)
            right_room = rooms[x][ym][z]
            right_room.numbers.append(right)

            front_room = rooms[xp][y][z]
            front_room.numbers.append(front)
            behind_room = rooms[xm][y][z]
            behind_room.numbers.append(behind)

            p.sendline("F")
            p.recvline()

        p.recvuntil("Action: ")
        p.sendline("L")
        p.recvuntil("Action: ")
        p.sendline("F")
        p.recvuntil("Action: ")
        p.sendline("R")
        p.recvline()

    p.recvuntil("Action: ")
    p.sendline("U")
    p.recvline()

p.recvuntil("Action: ")

count = 0

for z in range(6):
    for y in range(6):
        for x in range(6):
            room = rooms[x][y][z]

            if room.is_coprime():
                count += 1
                if count == 26:
                    p.sendline("C")
                    p.interactive()
                    exit()

                p.sendline("C")
                p.recvuntil("Action: ")

            p.sendline("F")
            p.recvuntil("Action: ")

        p.sendline("L")
        p.recvuntil("Action: ")
        p.sendline("F")
        p.recvuntil("Action: ")
        p.sendline("R")
        p.recvuntil("Action: ")

    p.sendline("U")
    p.recvuntil("Action: ")

print("something error")

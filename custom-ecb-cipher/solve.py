from Crypto.Util import number


def to_bin(num):
    return list(map(int, list(bin(num)[2:].zfill(32))))


def xor_list(lhs, rhs):
    return [x ^ y for (x, y) in zip(lhs, rhs)]


def and_list(lhs, rhs):
    return [x & y for (x, y) in zip(lhs, rhs)]


def inverse1(msg, num, helper=None):
    lhs = msg[0:num]
    rhs = helper
    if helper == None:
        rhs = [0] * num
    first = xor_list(lhs, rhs)
    leftover = len(msg) - num
    if leftover == num:
        return first + xor_list(msg[num + 1:], first)
    elif leftover > num:
        # left = msg[num:num * 2]
        # ll = xor(left, first)
        # first += ll
        first += inverse1(msg[num:], num, first)
    else:
        left = msg[num:]
        first += xor_list(left, first[:leftover])
    return first


def inverse2(msg, num1, num2, helper=None):
    if isinstance(num2, int):
        num2 = to_bin(num2)
    a1 = helper
    if helper == None:
        a1 = [0] * num1
    a2 = num2[len(num2)-num1:]
    lhs = and_list(a1, a2)
    rhs = msg[len(msg)-num1:]
    last = xor_list(lhs, rhs)
    leftover = len(msg) - num1
    if leftover == num1:
        return xor_list(and_list(num2[:num1], last), msg[:num1]) + last
    elif leftover > num1:
        last = inverse2(msg[:len(msg)-num1], num1,
                        num2[:len(msg)-num1], last) + last
    else:
        last = xor_list(and_list(last[len(last)-leftover:],
                                 num2[:leftover]), msg[:leftover]) + last
    return last


def is_ascii(s):
    return all(c < 128 and c >= 32 for c in s)


def convert(msg):
    msg = msg ^ msg << 13 & 275128763
    msg = msg ^ msg << 20 & 2186268085
    msg = msg ^ msg >> 14
    return msg


def find_x(msg):
    block = msg[0:4]
    block = number.bytes_to_long(block)
    block = to_bin(block)
    block = inverse1(block, 14)
    block = inverse2(block, 20, 2186268085)
    block = inverse2(block, 13, 275128763)

    for j in range(1, 9999):
        temp = block
        block = inverse1(block, j)
        res = "".join(map(str, block))
        res = int(res, 2)
        s = number.long_to_bytes(res, 4)
        if is_ascii(s):
            return j
        block = temp

    return None


message = bytes.fromhex(
    "e34a707c5c1970cc6375181577612a4ed07a2c3e3f441d6af808a8acd4310b89bd7e2bb9")

x = find_x(message)

if x == None:
    print("Failed to find x!!!")
    exit()

result = ""

for i in range(int(len(message) / 4)):
    block = message[i * 4: i * 4 + 4]
    block = number.bytes_to_long(block)
    block = to_bin(block)
    block = inverse1(block, 14)
    block = inverse2(block, 20, 2186268085)
    block = inverse2(block, 13, 275128763)

    # x = 9
    block = inverse1(block, x)
    res = "".join(map(str, block))
    res = int(res, 2)
    s = number.long_to_bytes(res, 4)
    result += s

print("TUCTF{%s}" % result)

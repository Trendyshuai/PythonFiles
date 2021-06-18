def AND(x1, x2):
    w1 = 0.5
    w2 = 0.5
    theta = 0.7
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


def OR(x1, x2):
    w1 = 2
    w2 = 3
    theta = 2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 1
    elif tmp > theta:
        return 0


def NAND(x1, x2):
    w1 = 2
    w2 = 3
    theta = 2
    tmp = x1*w1 + x2*w2
    if tmp <= theta:
        return 1
    elif tmp > theta:
        return 0


if __name__ == '__main__':
    print(AND(0, 0))
TABLE = [
    0x00,
    0x08,
    0x0B,
    0x0A,
    0x0D,
    0x0E,
    0x0C,
    0x05,
    0x03,
    0x08,
    0x0B,
    0x0A,
    0x0D,
    0x0E,
    0x0C,
    0x07,
    0x09,
    0x0F,
    0x01,
    0x02,
    0x04,
    0x06,
]
LOOKUP = { c: i for (i, c) in reversed(list(enumerate(TABLE))) }

FG = '\x1b[38;5;{}m'
BG = '\x1b[48;5;{}m'
RESET = '\x1b[0m'


def bg(c):
    return BG.format(LOOKUP[c])

def fg(c):
    return FG.format(LOOKUP[c])


if __name__ == '__main__':
    for c in range(8):
        print(f'{bg(c)}  ', end='')
    print(RESET)
    for c in range(8, 16):
        print(f'{bg(c)}  ', end='')
    print(RESET)

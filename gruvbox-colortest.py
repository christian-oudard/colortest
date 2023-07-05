FG = '\x1b[38;5;{}m'
BG = '\x1b[48;5;{}m'
RESET = '\x1b[0m'


def bg(c):
    return BG.format(c)

def fg(c):
    return FG.format(c)


grays = [235, 237, 239, 241, 243, 245, 246, 248, 250, 223, 229]

neutral_colors = [124, 166, 172, 106, 72, 66, 132]
bright_colors = [167, 208, 214, 142, 108, 109, 175]
four_bit_colors = {
    235: 0,
    245: 8,
    246: 7,
    223: 15,
    124: 1,
    106: 2,
    172: 3,
    66: 4,
    132: 5,
    72: 6,
    167: 9,
    142: 10,
    214: 11,
    109: 12,
    175: 13,
    108: 14,
}
four_bit_colors_rev = { b: a for (a, b) in four_bit_colors.items() }


if __name__ == '__main__':
    print()

    # 4-bit Color aliases.
    for c in range(0, 8):
        print(f'{bg(c)}     ', end='')
    print(RESET)
    for c in range(0, 8):
        b = 0
        if c == b:
            b = 15
        print(f'{fg(c)}{bg(b)} {c:>3d} ', end='')
    print(RESET)
    print()

    for c in range(8, 16):
        print(f'{bg(c)}     ', end='')
    print(RESET)
    for c in range(8, 16):
        b = 0
        if c == b:
            b = 15
        print(f'{fg(c)}{bg(b)} {c:>3d} ', end='')
    print(RESET)
    print()
    print()

    # Grays.
    for c in grays:
        print(f'{bg(c)}     ', end='')
    print(RESET)
    for c in grays:
        b = grays[0]
        if c == b:
            b = grays[-1]
        print(f'{fg(c)}{bg(b)} {c:>3d} ', end='')
    print(RESET)
    print()

    # Neutral Colors.
    print('     '*2, end='')
    for c in neutral_colors:
        print(f'{bg(c)}     ', end='')
    print(RESET)
    print('     '*2, end='')
    for c in neutral_colors:
        print(f'{fg(c)} {c:>3d} ', end='')
    print(RESET)
    print()
 
    # Bright Colors.
    print('     '*2, end='')
    for c in bright_colors:
        print(f'{bg(c)}     ', end='')
    print(RESET)
    print('     '*2, end='')
    for c in bright_colors:
        print(f'{fg(c)} {c:>3d} ', end='')
    print(RESET)
    print()

def decimal_to_binary(num):
    binary = []
    if num < 0:
        return 'voce é podre e sua familia te odeia'
    if num == 0:
        return [0]
    while num > 0:
        rest = num % 2
        binary.insert(0, rest)
        num = num // 2
    return binary


def main():
    num = 25
    print(decimal_to_binary(num))


main()
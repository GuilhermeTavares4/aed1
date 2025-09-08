def fatorial(num):
    if num > 1:
        return num * fatorial(num - 1)
    return num

print(fatorial(5))
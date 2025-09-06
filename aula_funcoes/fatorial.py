def fatorial(num):
    if num > 1:
        return num * fatorial(num - 1)
    return True

print(fatorial(5))
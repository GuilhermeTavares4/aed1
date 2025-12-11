def sort(array, size):
    for i in range(size - 1):
        floor = i
        for j in range(floor + 1, size):
            if array[j] < array[floor]:
                floor = j
        if floor != i:
            temp = array[i]
            array[i] = array[floor]
            array[floor] = temp


def main():
    array = [64, 25, 12, 22, 11]
    size = 5
    sort(array, size)
    print(array)


main()
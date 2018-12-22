def median(array):
    array = sorted(array)
x, odd = div mod(len(array), 2)
    if odd:
        return array[x]
    return (array[x - 1] + array[x]) / 2.0

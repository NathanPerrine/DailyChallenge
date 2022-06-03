def max_water(arr):
    most_water = -1 
    out = 0
    l, r = 0, 1
    length = len(arr)-1

    if r > length:
        return r

    while l < r:
        n1 = arr[l]
        n2 = arr[r]

        if n2 <= n1:
            water = (n2 * n2) * (r-l)
        else:
            water = (n1 * n1) * (r-l)

        if water > most_water:
            most_water = water
            out = water / (r-l)

        r += 1

        if r > length:
            r = l + 2
            l += 1
            if l == length:
                break

    return out




heights = [1,8,6,2,5,4,8,3,7]
print(max_water(heights))

heights=[1]
print(max_water(heights))
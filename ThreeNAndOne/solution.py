def solver(a, b):
    if a > b:
        a,b = b,a

    max_cycle_length = 0

    while a <= b:
        res = a
        cycle_length = 1

        while res != 1:
            if res % 2 == 1:
                res = 3 * res + 1
                res >>= 1
                cycle_length += 2
            else:
                res >>= 1
                cycle_length += 1

        max_cycle_length = max(max_cycle_length, cycle_length)

        a += 1

    return max_cycle_length


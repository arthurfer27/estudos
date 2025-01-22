def fatorial(num, show=False):
    print("-"*20)
    fat = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
        fat *= c
    return fat


print(fatorial(6, True))

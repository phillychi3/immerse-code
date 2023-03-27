def move_zeros(lst):
    ct = 0
    try:
        while True:
            lst.remove(0)
            ct+=1
    except ValueError:
        pass
    print(lst)
    for _ in range(ct):
        lst.append(0)
    return lst
def draw_xyz(N):
    pattern = ""

    for i in range(N):
        for j in range(1, N + 1):
            if ((N * i) + j) % 3 == 0:
                pattern += "X "
            elif ((N * i) + j) % 2 == 0:
                pattern += "Z "
            elif ((N * i) + j) % 2 != 0:
                pattern += "Y "
        pattern += "\n"
    return pattern

if __name__ == '__main__':
    print(draw_xyz(3))
    """
    Y Z X
    Z Y X
    Y Z X
    """


    print(draw_xyz(5))
    """
    Y Z X Z Y
    X Y Z X Z
    Y X Y Z X
    Z Y X Y Z
    X Z Y X Y
    """
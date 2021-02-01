def compute_length(a: int) -> int:
    """
        Compute length of integer
    :param a: integer
    :return: length of integer
    """

    a_length = 1
    while abs(a) // (10 ** a_length) != 0:
        a_length += 1
    return a_length


def karatsuba_multiplication(x: int, y: int) -> int:
    """
        Function makes multiplication of two integers
    :param x: integer
    :param y: integer
    :return: product of x and y
    """

    x_length = compute_length(x)
    y_length = compute_length(y)

    if x_length == 1 or y_length == 1:
        return x * y

    middle = x_length // 2 if x_length > y_length else y_length // 2

    a = x // 10 ** middle
    b = x % 10 ** middle
    c = y // 10 ** middle
    d = y % 10 ** middle

    ac = karatsuba_multiplication(a, c)
    bd = karatsuba_multiplication(b, d)
    ad_bc = karatsuba_multiplication((a + b), (c + d)) - ac - bd

    return 10 ** (middle * 2) * ac + 10 ** middle * ad_bc + bd


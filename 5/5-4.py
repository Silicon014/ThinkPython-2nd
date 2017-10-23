def recurse(n, s):
    '''
    输出s + sum [1..n]
    :param n: int, >= 0
    :param s: int
    :return: void
    '''
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)


recurse(3, 0)

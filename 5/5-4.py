def recurse(n, s):
    '''
    
    :param n: int, >= 0
    :param s: int
    :return: void
    '''
    if n == 0:
        print(s)
    else:
        recurse(n - 1, n + s)
recurse(3, 0)
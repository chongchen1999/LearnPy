def test(a, b, *args, **kwargs):
    print('a: ', a, type(a))
    print('b: ', b, type(b))
    print('args: ', args, type(args))
    print('kwargs: ', kwargs, type(kwargs))

test(11, 22)
test(11, 22, 33, 44, 55)
test(11, 22, 33, 44, 55, c=66, d=77)
test(11, 22, c=66, d=77)
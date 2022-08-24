def count(a, b, c, *args, **kwargs):
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('args:', args)
params = [2,4,3,4,5,6,6]
count(*params)
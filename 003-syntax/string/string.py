def string_len():
    s = '''aaa
    '''

    print(s)
    print(len(s))

def string_index():
    a = "abcdef"
    a = a.replace("a", "A")
    print(a[-6])
    # print(a[-7])

def string_slice():
    a = "abcdef"[0 : : 2]
    print(a)

    a = "123456789"
    print(a[-1:-100:-2])

def string_split():
    a = "1,2,3,4,5,6,7,8,9"
    b = a.split(',')
    print(b)

def string_join():
    a = ['1','2','3']
    b = ''.join(a)
    print(b)

def join_vs_add():
    times = 10000000
    a = ""

    import time
    cur_time = time.time()
    for i in range(times):
        a += str(i)
    # print(a)
    print("Total cost of + : " + str(time.time() - cur_time))

    a = []
    for i in range(times):
        a.append(str(i))
    
    cur_time = time.time()
    b = ''.join(a)
    # print(b)
    print("Total cost of join : " + str(time.time() - cur_time))

join_vs_add()
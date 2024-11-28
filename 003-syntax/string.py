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

string_slice()
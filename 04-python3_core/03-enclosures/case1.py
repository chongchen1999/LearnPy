def test(number):
    print(number)
    def test_in(number_in):
        return number_in + number
    
    return test_in

ret = test(5)
print(ret)

print(ret(10))
print(ret(20))
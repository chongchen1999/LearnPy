import time

def calc(count=100000):
    sum = 0
    for i in range(count):
        sum += i ** 3
    print("Sum:", sum)

start_time = time.time()
calc()
elapsed_time = time.time() - start_time
print("Elapsed time:", elapsed_time)
print(type(elapsed_time))
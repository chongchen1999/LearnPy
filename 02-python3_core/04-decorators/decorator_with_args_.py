import time

def delay(delay_sec = 2):
    def inner(func):
        def wrapper(*args, **kwargs):
            time.sleep(delay_sec)
            return func(*args, **kwargs)
        return wrapper
    return inner

@delay(3)
def print_word(word = 'Hello!'):
    print(word)
    return f"Successfully printed the content :\"{word}\"."


x = delay(3)
print(type(x))

print(print_word('Hello!'))
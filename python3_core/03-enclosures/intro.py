def person(name):
    def say(content):
        print(f'{name} say: {content}')

    return say

p1 = person('Tom')
p2 = person('Jerry')

p1('Hello')
p2('Hi')


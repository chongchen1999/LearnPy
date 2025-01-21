from collections import deque

def search(lines, pattern, history=4):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

# Example use on a file
if __name__ == '__main__':
    # Writing content to somefile.txt
    with open('data/somefile.txt', 'w') as f:
        for i in range(10):
            f.write("This is line %d\n" % (i+1))

    with open('data/somefile.txt') as f:
        search_result = search(f, 'line', 3)
        print(search_result)
        for line, prevlines in search_result:
            for pline in prevlines:
                print("Previous line: ", pline, end='')
            print("This line: ", line, end='')
            print('-'*20)

    q = deque(maxlen = 3)
    for i in range(5):
        q.append(i)
        print(q)

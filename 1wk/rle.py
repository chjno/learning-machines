from sys import argv

tups = []

def encode():
    data = argv[1]
    print 'encoding ' + data + '...'

    index = 0
    while index < len(data):
        char = data[index]
        count = 1
        # print count
        # print 'index: ' + str(index)
        while index + count < len(data) and data[index + count] == char:
            count += 1
        #     print 'count: ' + str(count)
        # print data[index] + ' - ' + str(count)
        tups.append((count, char))
        index += count

    print tups



if len(argv) > 2:
    print 'too many arguments'
elif len(argv) < 2:
    print 'script must be run with a string argument to encode'
else:
    encode()



def decode():
    string = ''
    for tup in tups:
        string += tup[0] * tup[1]
    print 'decoded string: ' + string

decode()
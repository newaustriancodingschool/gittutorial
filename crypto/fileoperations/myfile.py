def readfile(filename):
    f = open(filename, 'r')
    message = f.read()
    f.close()
    return message


def writefile(filename, message):
    f = open(filename, 'w')
    f.write(message)
    f.close()

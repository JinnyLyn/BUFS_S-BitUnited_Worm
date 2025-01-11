import itertools
import random
import flag
from binascii import hexlify


def createMath():
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    c = random.randint(0, 99)
    d = random.randint(0, 99)
    e = random.randint(0, 99)
    f = random.randint(0, 99)
    g = random.randint(0, 99)

    question = "{} {} {} {} {} {} {}".format(a, b, c, d, e, f, g)

    a = a + b
    b = b + c
    c = c + d
    d = d + e
    e = e + f
    f = f + g

    a = a + b
    b = b + c
    c = c + d
    d = d + e
    e = e + f

    a = a + b
    b = b + c
    c = c + d
    d = d + e

    a = a + b
    b = b + c
    c = c + d

    a = a + b
    b = b + c

    answer = a + b

    dict = {"question": question, "answer": answer}
    return dict


def handler(req):
    req.sendall(b'Problem #2\nThe number of the top of the pyramid?\n\n')

    for i in range(100):
        req.sendall(bytes('Challenge {}/{}'.format(i + 1, 100), 'ascii'))
        req.sendall(b'\n')

        questionDict = createMath()
        req.sendall(bytes('{}\n'.format(questionDict["question"]), 'ascii'))
        req.sendall(b'answer = ')

        r = bytes(req.recv(256).decode('ascii').strip('\n').strip('\r'), 'ascii')

        if r == bytes('{}'.format(questionDict["answer"]), 'ascii'):
            req.sendall(b'Correct!\n\n')
            if i == 99:
                req.sendall(flag.problem2)
                req.sendall(b'\n')
                return True
        else:
            req.sendall(b'Incorrect...\n\n')
            break

    return False


if __name__ == '__main__':
    import sys
    handler(sys.stdin.buffer, sys.stdout.buffer)
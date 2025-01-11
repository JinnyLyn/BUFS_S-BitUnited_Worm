import itertools
import random
import flag
from binascii import hexlify


def createMath():
    a = random.randint(0, 99)
    b = random.randint(0, 99)
    operator = random.choice("+-*/")

    if operator == "+":
        question = str(a) + " + " + str(b) + " = "
        answer = a + b
    elif operator == "-":
        question = str(a) + " - " + str(b) + " = "
        answer = a - b
    elif operator == "*":
        question = str(a) + " * " + str(b) + " = "
        answer = a * b
    elif operator == "/":
        question = str(a) + " / " + str(b) + " = "
        answer = a // b
    else:
        question = None
        answer = None

    dict = {"question": question, "answer": answer}
    return dict


def handler(req):
    req.sendall(b'Problem #1\n\n')

    for i in range(100):
        req.sendall(bytes('Challenge {}/{}'.format(i + 1, 100), 'ascii'))
        req.sendall(b'\n')

        questionDict = createMath()
        req.sendall(bytes('{}'.format(questionDict["question"]), 'ascii'))

        r = bytes(req.recv(256).decode('ascii').strip('\n').strip('\r'), 'ascii')

        if r == bytes('{}'.format(questionDict["answer"]), 'ascii'):
            req.sendall(b'Correct!\n\n')
            if i == 99:
                req.sendall(flag.problem1)
                req.sendall(b'\n')
                return True
        else:
            req.sendall(b'Incorrect...\n\n')
            break

    return False


if __name__ == '__main__':
    import sys
    handler(sys.stdin.buffer, sys.stdout.buffer)
    
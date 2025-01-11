import itertools
import random
import flag
from binascii import hexlify


def createMath():
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)
    d = random.randint(1, 9)
    operator1 = random.choice("+-*/")
    operator2 = random.choice("+-*/")
    operator3 = random.choice("+-*/")

    if operator1 == "/":
        operator1 = "//"
    if operator2 == "/":
        operator2 = "//"
    if operator3 == "/":
        operator3 = "//"

    formula = str(a) + operator1 + str(b) + operator2 + str(c) + operator3 + str(d)
    result = eval(formula)

    question = "{} ? {} ? {} ? {} = {}".format(a, b, c, d, result)
    answer = None

    dict = {"question": question, "answer": answer, "a": a, "b": b, "c": c, "d": d, "result": result}
    return dict

def checkAnswer(r, questionDict):
    operators = str(r).strip('b').strip('\'').split(',')
    if operators[0] == "/":
        operators[0] = "//"
    if operators[1] == "/":
        operators[1] = "//"
    if operators[2] == "/":
        operators[2] = "//"
    formula = str(questionDict["a"]) + operators[0] + str(questionDict["b"]) + operators[1] + str(questionDict["c"]) + operators[2] + str(questionDict["d"])
    result = eval(formula)
    if result == questionDict["result"]:
        return True
    else:
        return False


def handler(req):
    req.sendall(b'Problem #3\nPlease give operators\n\n[ex]\n1 ? 2 ? 3 ? 4 = 3\nanswer = +,*,-\n\n')

    for i in range(100):
        req.sendall(bytes('Challenge {}/{}'.format(i + 1, 100), 'ascii'))
        req.sendall(b'\n')

        questionDict = createMath()
        req.sendall(bytes('{}\n'.format(questionDict["question"]), 'ascii'))
        req.sendall(b'answer = ')

        r = bytes(req.recv(256).decode('ascii').strip('\n').strip('\r'), 'ascii')

        if checkAnswer(r, questionDict):
            req.sendall(b'Correct!\n\n')
            if i == 99:
                req.sendall(flag.problem3)
                req.sendall(b'\n')
                return True
        else:
            req.sendall(b'Incorrect...\n\n')
            break

    return False


if __name__ == '__main__':
    import sys
    handler(sys.stdin.buffer, sys.stdout.buffer)
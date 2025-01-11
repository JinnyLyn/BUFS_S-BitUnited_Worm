import itertools
import random
import time
import flag
import subprocess
from binascii import hexlify


def createMath(number):
    qrElement = ['raccoon', 'dog', 'rabbit', 'cow', 'horse', 'wolf', 'hippopotamus', 'kangaroo', 'fox', 'giraffe', 'bear', 'koala', 'bat', 'gorilla', 'rhinoceros', 'monkey', 'deer', 'zebra', 'jaguar', 'skunk', 'elephant', 'animal', 'reindeer', 'rat', 'tiger', 'cat', 'mouse', 'buffalo', 'hamster', 'panda', 'sheep', 'leopard', 'pig', 'mole', 'goat', 'lion', 'camel', 'squirrel', 'donkey', 'seal', 'badger', 'anteater', 'armadillo', 'iguana', 'rabbit', 'tadpole', 'frog', 'bear', 'deer', 'skunk', 'raccoon', 'dog', 'rabbit', 'cow', 'horse', 'wolf', 'hippopotamus', 'kangaroo', 'fox', 'giraffe', 'bear', 'koala', 'bat', 'gorilla', 'rhinoceros', 'monkey', 'deer', 'zebra', 'jaguar', 'skunk', 'elephant', 'animal', 'reindeer', 'rat', 'tiger', 'cat', 'mouse', 'buffalo', 'hamster', 'panda', 'sheep', 'leopard', 'pig', 'mole', 'goat', 'lion', 'camel', 'squirrel', 'donkey', 'seal', 'badger', 'anteater', 'armadillo', 'iguana', 'rabbit', 'tadpole', 'frog', 'bear', 'deer', 'skunk']
    cmd = "qr {} | hexdump -e '16/1 \"%02x \" \" \"'".format(qrElement[number])
    question = subprocess.check_output(cmd, shell=True)
    answer = qrElement[number]

    dict = {"question": question, "answer": answer}
    return dict


def handler(req):
    req.sendall(b'Problem #4\n\n')

    for i in range(100):
        req.sendall(bytes('Challenge {}/{}'.format(i + 1, 100), 'ascii'))
        req.sendall(b'\n')

        questionDict = createMath(i)
        req.sendall(bytes('{}\n'.format(questionDict["question"]), 'ascii'))
        req.sendall(b'answer = ')

        r = bytes(req.recv(256).decode('ascii').strip('\n').strip('\r'), 'ascii')

        if r == bytes('{}'.format(questionDict["answer"]), 'ascii'):
            req.sendall(b'Correct!\n\n')
            if i == 99:
                time.sleep(1)
                req.sendall(flag.problem4)
                req.sendall(b'\n')
                return True
        else:
            req.sendall(b'Incorrect...\n\n')
            break

    return False


if __name__ == '__main__':
    import sys
    handler(sys.stdin.buffer, sys.stdout.buffer)
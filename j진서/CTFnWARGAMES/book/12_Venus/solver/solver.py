import sys
import socket
import re
import itertools
import qrtools


def problem4(client):
    for i in range(100):
        data = client.recv(4096)
        client.recv(4096)

        png = data.split('\n')[0]
        png = png.replace('b\'', '').replace('  ', '').replace('\'', '')
        png = png.split(' ')
        png_bin = ''

        for byte in png:
            if byte is not '':
            	png_bin += chr(int(byte, 16))

        open('qr.png', 'w').write(png_bin)
        qrcode = qrtools.QR(filename = 'qr.png')
        qrcode.decode()
        answer = qrcode.data

        print(answer)

        client.send(answer.encode('ascii'))

        if 'Correct!\n\n' in client.recv(4096):
            if i == 99:
                data = client.recv(4096)

                flag = data.decode('ascii').split('\n')[0]
                print('FLAG : ' + flag)

                return True
        else:
            print(i, 'False')
            break
 
        data = None
        client.recv(4096)

    sys.exit(1)


def problem3(client, data):
    operators = list(itertools.product(('+','-','*','/'), repeat = 3))

    for i in range(100):
        if data is None:
            data = client.recv(4096)
        
        formula = data.split('\n')[-2]
        formula, result = formula.split('=')
        result = int(result)

        for operator in operators:
            answer = formula.replace('?', '%c') % operator
            if eval(answer) == result:
                answer = re.sub(r'\(|\)|\'| ', '', str(operator))

                print(formula, '=', answer)

                client.send(answer.encode('ascii'))

                if 'Correct!\n\n' in client.recv(4096):
                    if i == 99:
                        data = client.recv(4096)
                        
                        flag = data.decode('ascii').split('\n')[0]
                        print('FLAG : ' + flag)

                        problem4(client)

                        return True
                else:
                    print(i, 'False')
                    break

                data = None
                break
            
    sys.exit(1)


def problem2(client, data):
    for i in range(100):
        if data is None:
            data = client.recv(4096)
        
        values = data.split('\n')[-2]
        values = values.split(' ')

        answer = int(values[0]) + 6 * int(values[1]) + 15 * int(values[2]) + 20 * int(values[3]) + 15 * int(values[4]) + 6 * int(values[5]) + int(values[6])

        print(values, '=', answer)

        client.send(str(answer).encode('ascii'))

        if 'Correct!\n\n' in client.recv(4096):
            if i == 99:
                data = client.recv(4096)
                
                flag = data.decode('ascii').split('\n')[0]
                print('FLAG : ' + flag)

                problem3(client, data)

                return True
        else:
            print(i, 'False')
            break

        data = None
    
    sys.exit(1)


def problem1(client):
    for i in range(100):
        data = client.recv(4096)

        formula = data.split('\n')[-1]
        formula = formula.split('=')[0]

        answer = eval(formula)

        print(formula, '=' , answer)

        client.send(str(answer).encode('ascii'))

        if 'Correct!\n\n' in client.recv(4096):
            if i == 99:
                data = client.recv(4096)
                
                flag = data.decode('ascii').split('\n')[0]
                print('FLAG : ' + flag)

                problem2(client, data)

                return True
        else:
            print(i, 'False')
            break
    
    sys.exit(1)


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 24154))

    data = client.recv(4096)

    problem1(client)
    client.close()

if __name__ == '__main__':
    main()

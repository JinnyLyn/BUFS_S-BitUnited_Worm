import socketserver
import sys
import problem1, problem2, problem3, problem4

class RequestHandler(socketserver.StreamRequestHandler):
    def handle(self):
        problems = [problem1, problem2, problem3, problem4]
        clear = True

        for i in range(len(problems)):
            self.request.sendall(b'-' * 64 + b'\n')
            result = problems[i].handler(self.request)
            self.request.sendall(b'-' * 64 + b'\n')
            if result is False:
                self.request.sendall(b'Bye.\n')
                clear = False
                break

        if clear:
            self.request.sendall(b'Congratulations!')

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

def main(argv):
    host, port = 'localhost', 24154

    if len(argv) == 2:
        port = int(argv[1])
    elif len(argv) >= 3:
        host, port = argv[1], int(argv[2])

    sys.stderr.write('Listening {}:{}\n'.format(host, port))
    server = ThreadedTCPServer((host, port), RequestHandler)
    server.allow_reuse_address = True
    server.serve_forever()

if __name__ == '__main__':
    main(sys.argv)

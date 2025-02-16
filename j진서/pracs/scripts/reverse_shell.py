import socket
import subprocess

host = 'localhost'
port = 65432

def handle_connection(conn, addr):
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        cmd = data.strip().decode('utf-8')

        try:
            result = subprocess.run(cmd, shell=True, check=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            response = result.stdout + result.stderr
            conn.sendall(response)
        except Exception as e:
            print(f"Error executing command: {e}")

    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen()
    print(f"Listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        handle_connection(conn, addr)

if __name__ == '__main__':
    main()

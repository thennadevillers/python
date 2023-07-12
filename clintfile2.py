import socket
s = socket.socket()
host = socket.gethostname()
port = 6000
s.connect((host, port))
with open('received.txt', 'w') as f:
    print ('downloading file..')
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data.decode())
    print('received: {}\n'.format(data.decode()))
    print('file downloaded successfully.')
s.close()
print('connection closed')

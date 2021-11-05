import socket


def server_program():
    host = socket.gethostname()
    port = 8080
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(3)
    conn, address = server_socket.accept()
    print("Connection from: ", address)
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected client: " + str(data))
        data = input("Type your text here -> ")
        conn.send(data.encode())
  
    conn.close()
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
 

if __name__ == '__main__':
    server_program()
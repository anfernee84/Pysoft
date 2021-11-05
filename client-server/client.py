import socket


def client_program():
    host = socket.gethostname()
    port = 8080
    ipaddr = socket.gethostbyaddr(socket.gethostname())
    client_socket = socket.socket()
    client_socket.connect((host, port))
    print("Connected to server: ", "IP = ",  str(ipaddr[2]),",", "Port = " , port)
    message = input("Type your text here -> ")
    

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode() 
        print('Received from server: ' + data) 
        message = input("Type your text here -> ")
    
    client_socket.close()
 

if __name__ == '__main__':
    client_program()
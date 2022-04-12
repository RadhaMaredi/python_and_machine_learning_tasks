#import the cocket
import socket


def client_program():

    """this function make a connection with the server by using the connection
    and port number to communicate"""

    host = socket.gethostname()  # as both code is running on same pc
    port = 5000                  # socket server port number

    client_socket = socket.socket()  # instantiate of socket
    client_socket.connect((host, port))  # connect to the server

    message = input(" Enter client text -> ")  # take input from the client side

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message to server
        data = client_socket.recv(1024).decode()  # receive response from the server
        print('Received from server: ' + data)  # show the conversation in terminal

        # again take input from the client to further conversation or stop conversation
        message = input("Enter client text -> ")  

    client_socket.close()  # close the connection with server

#driver code
if __name__ == '__main__':
    #calling the function
    client_program()

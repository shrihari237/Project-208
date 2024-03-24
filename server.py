import socket 
from threading import Thread

IP_ADDRESS = '127.0.0.1'
PORT = 8050
SERVER = None
BUFFER_SIZE = 4096
clients ={}

def setup():
    print('\t\t\t\t\t\t\tIP Messenger\t\t\t\t\t')
    global SERVER
    global IP_ADDRESS
    global PORT

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS,PORT))

    SERVER.listen(100)
    print("\t\t\t\t\t\t\t\tServer is waiting for upcoming connections...")
    print("\n")

    acceptConnections()

setup_thread = Thread(target=setup)
setup_thread.start()

def acceptConnections():
    global SERVER
    global clients
    while True:
        client,addr = SERVER.accept()    

    print(client.addr)    
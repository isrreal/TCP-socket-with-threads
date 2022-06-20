import socket
PORTA = 8080
SERVER = socket.gethostbyname(socket.gethostname())
FORMAT = 'utf-8'
ADDR = (SERVER, PORTA)
DISCONNECT_MESSAGE = "!CONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
def send(msg):
    # encapsula a mensagem no formato FORMAT cujo valor é, 'utf-8'
    message = msg.encode(FORMAT)
    try:
        client.send(message)
    except socket.error:
        print("erro")
while True: 
    mensagem = input("Digite sua mensagem\n")
    send(mensagem)
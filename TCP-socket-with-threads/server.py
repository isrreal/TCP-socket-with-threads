import threading
import socket
import time 
import os
# HEADER representa o tamanho da mensagem
HEADER = 64
#FORMAT representa a formatação da mensagem
FORMAT = "utf-8"
PORTA = 8080
# socket.gethostname() retorna o nome do host
# socket.gethostbyname(socket.gethostname())
# retorna o IP da máquina pelo nome
SERVER_IP = socket.gethostbyname(socket.gethostname())  
ADDR = (SERVER_IP, PORTA)
# mensagem para desconectar
DISCONNECT_MESSAGE = "!CONNECT"
# criando o socket TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# atribuindo um endereço ao socket 
server.bind(ADDR)
# maneja a conexão com o cliente
def client(connection, address):
    initial_thread_count = threading.active_count()
    load("Aguardado conexão")
    print_thread_count()
    while True:
        # recv() retorna os bytes da mensagem recebida
        # decode() converte os bytes em uma string
        # recebe a mensagem do cliente convertida pelo decode()
        msg = connection.recv(HEADER).decode(FORMAT)
        # printa se a quantidade de threads aumentou
        if threading.active_count() > initial_thread_count:
            print_thread_count()
        if msg == DISCONNECT_MESSAGE:
            print("socket desconectado!")
            break
        print(f"[{address}] : {msg}")
    connection.close()
def start_server():
    # abre a porta para receber conexões
    server.listen()
    while True:
    # server.accept() retorna um tupla contendo os valores do socket e endereço do cliente
        connection, address = server.accept()
        thread = threading.Thread(target = client, args = (connection, address))
        thread.start()
def print_thread_count():
    print(f"Quantidade de hosts conectados: {threading.active_count() - 1}\n")
def load(msg):
    for i in range(3):
        msg += '.'
        time.sleep(1)
        os.system("cls")  
        print(msg)
    time.sleep(1)
    os.system("cls")
init = "Servidor iniciando"
load(init)
start_server()



import socket
import os

from classes.rotina import Rotina
# from classes.ultra_sonico import UltraSonico

HOST = ''
PORT = 5001
ORIGEM = (HOST, PORT)
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


tcp.bind(ORIGEM)
tcp.listen(1)

# UltraSonico().start()

os.system('git -C /home/pi/raspberry-python-robo-server/ pull origin master')

rotina = Rotina()

while True:
    conexao, cliente = tcp.accept()
    print(f'conectado por {cliente}')

    while True:
        recebido_socket = conexao.recv(1024)
        if not recebido_socket: break

        rotina.executar(recebido_socket)
    
    print(f'conexão finalizada com o cliente {cliente}')
    conexao.close

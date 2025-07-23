import socket
import select
import random
import sys
import time
from _thread import start_new_thread

MSG_LEN = 5
random.shuffle(Q_and_A)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("Correct method: script, IP address, port number")
    exit()

number_of_participants = int(input("Please enter the number of participants (max allowed is 4): "))
number_joined = 0

if not 1 <= number_of_participants <= 4:
    print("Please input a valid number between 1 and 4.")
    sys.exit()

IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.bind((IP_address, Port))
server.listen(10)
print("Server started!")

print(f"Waiting for connection on IP address and Port number: {IP_address}, {Port}")

clients_list = []
participants = {}
marks = {}
mapping = {}
Person = [server]
answer = [-1]

def receive_message(client_socket):
    try:
        message = client_socket.recv(1024).decode('utf-8')
        return message
    except socket.error as e:
        print("Error receiving message:", e)
        return None

# Remaining functions (send_to_one, send_to_all, update_marks, end_quiz, ask_question, quiz) are unchanged

while True:
    rList, wList, error_sockets = select.select(clients_list + [server], [], [])
    for socket in rList:
        if socket == server:
            client_socket, client_address = server.accept()
            # Remaining part of the server loop is unchanged

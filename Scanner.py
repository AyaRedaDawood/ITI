import socket
import time
import threading
import subprocess
import sys,os
from queue import Queue

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = raw_input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)
print('Starting scan on host: ', t_IP)


def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((t_IP, port))
        with print_lock:
            print(port, 'is open')
            nmapR = (os.popen('nmap -sC -sV -p ' + str(port) + " " + t_IP).read()).split("\n")[5]
            print(nmapR)
        con.close()
    except:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


q = Queue()
startTime = time.time()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 500):
    q.put(worker)

q.join()
print('Time taken:', time.time() - startTime)


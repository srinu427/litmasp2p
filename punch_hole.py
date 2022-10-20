import os
import socket
import threading
import time

def init_server(local_rport):
    global server_sock
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('127.0.0.1', local_rport))


def init_sender(local_sport):
    global sender_sock
    sender_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_sock.bind(('127.0.0.1', local_sport))


def process_recv_data(rdata):
    print(rdata)


def start_listening():
    while True:
        print("here")
        server_sock.listen(5)
        cl, addr = server_sock.accept()
        while True:
            print(addr)
            process_recv_data(cl.recv(8))


def send_ping(addr):
    print("sending")
    try:
        sender_sock.send(b"lmaolmao")
        print(sender_sock.recv(8))
    except OSError as sge:
        print(sge)
        sender_sock.connect(addr)
        sender_sock.send(b"lmaolmao")
        print(sender_sock.recv(8))


def punch_hole_to_peer(peer_ip, peer_rport, peer_sport, local_rport, local_sport):
    init_server(local_rport)
    init_sender(local_sport)
    #server_t = threading.Thread(target=start_listening, daemon=True)
    #server_t.start()
    while True:
        try:
            time.sleep(0.5)
            send_ping((peer_ip, peer_sport))
        except Exception as e:
            print(e)
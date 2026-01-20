import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1) # Timeout 1 detik
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        sock.close()
    except socket.error as err:
        print(f"Couldn't connect to server: {err}")

# Contoh penggunaan
target_ip = "192.168.1.1" # Ganti dengan IP target Anda
print(f"Scanning common ports on {target_ip}...")
for port in [21, 22, 23, 80, 443, 8080]:
    scan_port(target_ip, port)
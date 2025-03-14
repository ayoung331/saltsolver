import itertools
import socket

host = "verbal-sleep.picoctf.net"
port = 58075

hex_chars = "0123456789abcdef"

for salt_chars in itertools.product(hex_chars, repeat=2):
    salt = "".join(salt_chars)

    try:
        s = socket.create_connection((host, port))
        data = s.recv(1024).decode()
        s.send(b"g\n")
        data = s.recv(1024).decode()
        s.send(b"squeak\n")
        data = s.recv(1024).decode()
        s.send(salt.encode() + b"\n")
        data = s.recv(1024).decode()
        print(f"Tried salt: {salt}")
        if "picoCTF{" in data:
            print(f"Found it! Salt: {salt}")
            print(data)
            break
        s.close()
    except Exception as e:
        print(f"Error with salt {salt}: {e}")


import itertools
import socket

host = "verbal-sleep.picoctf.net"
port = 58075

hex_chars = "0123456789abcdef"

for salt_chars in itertools.product(hex_chars, repeat=2):
    salt = "".join(salt_chars)

    try:
        s = socket.create_connection((host, port))
        data = b""  # Initialize empty byte string
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break  # Connection closed
            data += chunk
        data = data.decode()
        s.send(b"g\n")
        data2 = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            data2 += chunk
        data2 = data2.decode()
        s.send(b"squeak\n")
        data3 = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            data3 += chunk
        data3 = data3.decode()
        s.send(salt.encode() + b"\n")
        data4 = b""
        while True:
            chunk = s.recv(1024)
            if not chunk:
                break
            data4 += chunk
        data4 = data4.decode()
        print(f"Tried salt: {salt}")
        if "picoCTF{" in data4:
            print(f"Found it! Salt: {salt}")
            print(data4)
            break
        s.close()
    except Exception as e:
        print(f"Error with salt {salt}: {e}")

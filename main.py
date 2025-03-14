import itertools
import socket

host = "verbal-sleep.picoctf.net"
port = 58075

hex_chars = "0123456789abcdef"

for salt_chars in itertools.product(hex_chars, repeat=2):
    salt = "".join(salt_chars)

    try:
        s = socket.create_connection((host, port))
        data = s.recv(1024).decode()  # Receive initial server message
        s.send(b"g\n")  # Send "g" to guess
        data = s.recv(1024).decode()  # Receive next server message
        s.send(b"squeak\n")  # Send the cheese
        data = s.recv(1024).decode()  # Receive prompt for salt
        s.send(salt.encode() + b"\n")  # Send the salt
        data = s.recv(1024).decode()  # Receive the server response
        print(f"Tried salt: {salt}")
        if "picoCTF{" in data:
            print(f"Found it! Salt: {salt}")
            print(data)
            break  # Stop when flag is found
        s.close()

    except Exception as e:
        print(f"Error with salt {salt}: {e}")

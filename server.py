import socket
from datetime import datetime
import pytz


UTC = pytz.utc

timeZ_Kl = pytz.timezone('Asia/Kolkata') 
timeZ_Ny = pytz.timezone('America/New_York')
timeZ_Ma = pytz.timezone('Africa/Maseru')
timeZ_Ce = pytz.timezone('US/Central')
timeZ_At = pytz.timezone('Europe/Athens')

dt_Kl = datetime.now(timeZ_Kl)
dt_Ny = datetime.now(timeZ_Ny)
dt_Ma = datetime.now(timeZ_Ma)
dt_Ce = datetime.now(timeZ_Ce)
dt_At = datetime.now(timeZ_At)

utc_Kl = dt_Kl.astimezone(UTC)
utc_Ny = dt_Ny.astimezone(UTC)
utc_Ma = dt_Ma.astimezone(UTC)
utc_Ce = dt_Ce.astimezone(UTC)
utc_At = dt_At.astimezone(UTC)





HOST="127.0.0.1"
PORT=1234

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as q:
    q.bind((HOST, PORT))
    q.listen()
    conn, addr = q.accept()
    with conn:
            print(f"Connected by {addr}")
            zones="hello Client Choose The Time Zone\n1.Asia/Kolkata\n2.America/New_York\n3.Africa/Maseru\n4.US/Central\n5.Europe/Athens\n"
            conn.send(zones.encode())
            resp=int(conn.recv(1024).decode())
            if(resp==1):
                  conn.send(utc_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==2):
                  conn.send(utc_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==3):
                  conn.send(utc_Ma.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==4):
                  conn.send(utc_Ce.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==5):
                  conn.send(utc_At.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
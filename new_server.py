import socket
from datetime import datetime
import pytz



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

""" 
time_zone = input("Enter the time zone:")
tz = pytz.timezone(time_zone)
curr_time = datetime.now(tz)
print(curr_time)
 """


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
                  conn.send(dt_Kl.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==2):
                  conn.send(dt_Ny.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==3):
                  conn.send(dt_Ma.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==4):
                  conn.send(dt_Ce.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
            elif(resp==5):
                  conn.send(dt_At.strftime('%Y-%m-%d %H:%M:%S %Z %z').encode())
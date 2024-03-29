# !/usr/bin/python3
# simple script to test a syslog-ng input.
import socket

dest_ip = input("Input the IP of the Syslog-ng Server: ")
dest_port = int(input("Input the port for Syslog-ng ingestion: "))
hostname = socket.gethostname()
message = input("Message (Optional): ")

content = f'<14>Test Syslog-ng pipeline over {dest_port} to {dest_ip} from {hostname}. \"message\":\"{message}\" '

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((dest_ip, dest_port))
s.send(content.encode())

s.close()

print("Sent message:", content)


from socket import *
import base64

msg = "\r\n I love Computer Networks"
endmsg = "\r\n.\r\n"

mailserver = ('smtp.gmail.com', 587) #Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

recv = clientSocket.recv(1024).decode()
print("Message after connection request:" + recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')


# Send MAIL FROM command and print server response.
mailFrom = "MAIL FROM: <sachinshah0099@gmail.com> \r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print("After MAIL FROM command: "+recv2)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send RCPT TO command and print server response.
rcptTo = "RCPT TO: <sachinshah0099@gmail.com> \r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024).decode()
print("After RCPT TO command: "+recv3)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send DATA command and print server response.
data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024).decode()
print("After DATA command: "+recv4)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send message data.
subject = "Subject: SMTP mail client testing \r\n\r\n" 
clientSocket.send(subject.encode())
message = msg
clientSocket.send(message.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024).decode()
print("Response after sending message body:"+recv_msg)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send QUIT command and get server response.
clientSocket.send("QUIT\r\n".encode())
message=clientSocket.recv(1024)
print (message)
clientSocket.close()
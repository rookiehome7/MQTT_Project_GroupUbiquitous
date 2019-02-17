from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

addr = ('127.0.0.1', SERV_PORT) # Socket address
s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
s.bind(addr)                    # Bind socket to address
print ('UDP server started ...')

while(1):
  print ('Client> ', end = '')
  txtin,addr = s.recvfrom(MAX_BUF)  # txtin stores receive text
                                    # addr stores client socket address
  print ('%s' %(txtin).decode('utf-8')) # Convert byte to string and print  
  if txtin == b'quit':          # Break if user types 'quit'. 
     print('Terminate server ...')
     break
  else:
     txtout = txtin.upper()     # Change text to upper case
     s.sendto(txtout, addr)     # Send it back to the client
	 

s.close()

from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)     # Server socket address 
s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket

username = input('Enter your name: ') # text for prompt
while(1):
    print('%s> ' %(username), end='') # Print the prompt
    sys.stdout.flush()
    txtout =  sys.stdin.readline().strip() # Take input from user keyboard
    s.sendto(txtout.encode('utf-8'), addr) # Convert to byte type and send
    if txtout == 'quit':                  # Exit if user types quit
      break
    modifiedMsg, srvAddr = s.recvfrom(2048) # Wait for modified text from the server
    print (modifiedMsg.decode('utf-8'))     # Print the modified text.
s.close()

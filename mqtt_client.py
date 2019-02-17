from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

#addr = ('127.0.0.1', SERV_PORT)     # Server socket address 
s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket

print('---------------------------------------------------------')
print('|\t\t\tMQTT Client\t\t\t|')
print('|\t\t     Group Ubiquitous\t\t\t|')
print('|\t   In this program will provide sub/pub\t\t|')
print('|  Subscriber: subscribe broker_ipaddress topicname\t|')
print('|  Publisher: publish broker_ipaddress topicname data\t|')
print('---------------------------------------------------------')

# userInput = input()
# split_userInput = userInput.split()
# if split_userInput[0] == "subscribe":
#     print("subscribe mode")
# elif split_userInput[0] == "publish":
#     print("publish mode")
# else:
#     print("Try again")
txtout = "home"
while(1):
    print('> ',end='') # Print the prompt
    sys.stdout.flush()
    txtout =  sys.stdin.readline().strip() # Take input from user keyboard

    split_txtout = txtout.split()
    if (split_txtout[0] == "subscribe" and len(split_txtout) == 3): # Subscribe Mode 
    	print("Sub")
    	broker_ipaddress = split_txtout[1]  
    	topicname = split_txtout[2] 

    	addr = (broker_ipaddress, SERV_PORT) # IP with port 

    	print('IP:' + broker_ipaddress + ' Topic:' + topicname)
    	data_Send = 'subscribe:' + topicname
    	s.sendto(data_Send.encode('utf-8'), addr)
    
    elif (split_txtout[0] == "publish" and len(split_txtout) == 4): # Publish Mode 
    	broker_ipaddress = split_txtout[1]  
    	topicname = split_txtout[2] 
    	data = split_txtout[3] 

    	addr = (broker_ipaddress, SERV_PORT) # IP with port 

    	print('IP:' + broker_ipaddress + ' Topic:' + topicname + ' Data:' + data)
    	data_Send = 'publish:' + topicname + ':' + data
    	s.sendto(data_Send.encode('utf-8'), addr)	# Convert to byte type and send
    	
    	# modifiedMsg, srvAddr = s.recvfrom(2048)
    	# print(modifiedMsg.decode('utf-8'))
    else:
    	print("Wrong syntax. Please try agian")

    if txtout == 'quit':
        break

s.close()

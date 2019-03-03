from socket import * 
import sys
MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number
print('---------------------------------------------------------')
print('|\t\t\tMQTT Broker\t\t\t|')
print('|\t\t     Group Ubiquitous\t\t\t|')
print('---------------------------------------------------------')
subscribe_lst = [] # Subscribe Array
print ('Please enter Broker IP address:')
sys.stdout.flush()
txt =  sys.stdin.readline().strip() # Take input from user keyboard
txtsplit = txt.split()	
brokerIP = txtsplit[0]
addr = (brokerIP, SERV_PORT) 		# Socket address
s = socket(AF_INET, SOCK_DGRAM) 	# Create UDP socket
s.bind(addr)                   		# Bind socket to address
print ('Broker IP' + brokerIP + '. Start at port:' + str(SERV_PORT))

while(1):
	print ('>', end = '')
	txtin,addr = s.recvfrom(MAX_BUF)  # txtin stores receive text
	ip, port = str(addr[0]), str(addr[1]) 
	split_txtin = txtin.decode('utf-8').split(':')
	# Pubish > constraints  { publih , topic , data }
	if ( split_txtin[0] == "publish" and len(split_txtin) == 3): 
		topic,data = split_txtin[1],split_txtin[2]
		print ('Publish from ' + ip + ':' + port + '\tTopic:' + topic +' Data:' + data)
		# Send message to subscribe client 
		# In each array of subscribe_lst will keep in style
		# >>   127.0.0.1:50000,topicname <<< 
		for x in subscribe_lst:	
			split_x = x.split(',')  						# We need to split IP:Port and topicname
			if split_x[1] == topic: 						# Check each item in list have same topic 
				split_ip_port = split_x[0].split(':') 		# If found split IP and port
				addr_send = (split_ip_port[0], int(split_ip_port[1])) # Write in addr_send 
				print ('   Publish data to ' + split_x[0])
				s.sendto(data.encode('utf-8'), addr_send) 	#Send data to client by using addr_send
	# Subscribe > constraints  { subscribe , topic }
	elif ( split_txtin[0] == "subscribe" and len(split_txtin) == 2): 
		subscribe_lst.append(ip +':'+ port + ',' + split_txtin[1])  # Make array list of subscribe
		print('Subscribe ' + ip +':'+ port + ' to list with topic:' + split_txtin[1])
		print ('\tSubscribe list: ' + str(subscribe_lst))
	# Un-Subscribe > constraints  { unsubscribe , topic }
	elif (split_txtin[0] == "unsubscribe" and len(split_txtin) == 2):
		string = ip + ':' + port + ',' + split_txtin[1]
		subscribe_lst.remove(string) # Remove subscribe client in list 
		print ('Unsubscribe' + ip + ':' + port + ' from list with topic: ' + split_txtin[1])
		print ('\tSubscribe list: ' + str(subscribe_lst))	
	# Error 
	else:
		print("Error : received message error ( Wrong argument or something) ")
s.close()

from threading import Thread
from socket import * 
import sys
import time
import os

MAX_BUF = 2048
SERV_PORT = 50000

def handle_client(s):
  while True:
     txtin = s.recv(2048)
     print ('Message> %s' %(txtin).decode('utf-8')) 
  return

def main():
	#addr = ('127.0.0.1', SERV_PORT)     # Server socket address 
	s = socket(AF_INET, SOCK_DGRAM)  # Create UDP socket
	print('---------------------------------------------------------')
	print('|\t\t\tMQTT Client\t\t\t|')
	print('|\t\t     Group Ubiquitous\t\t\t|')
	print('|\t   In this program will provide sub/pub\t\t|')
	print('|  Subscriber: subscribe broker_ipaddress topicname\t|')
	print('|  Publisher: publish broker_ipaddress topicname data\t|')
	print('---------------------------------------------------------')
	while(1):
		print('> ',end='') # Print the prompt
		sys.stdout.flush()
		txtout =  sys.stdin.readline().strip() # Take input from user keyboard
		split_txtout = txtout.split()

		# Pubish > constraints  { publih , topic , data }			
		if (split_txtout[0] == "publish" and len(split_txtout) == 4): 
			broker_ipaddress,topicname,data = split_txtout[1],split_txtout[2],split_txtout[3]  
			addr = (broker_ipaddress, SERV_PORT) # IP with port 
			print('Publish to IP:' + broker_ipaddress + ' Topic:' + topicname + ' Data:' + data)
			
			# Make string and send to broker 
			data_Send = 'publish:' + topicname + ':' + data
			s.sendto(data_Send.encode('utf-8'), addr)	

		# Subscribe > constraints  { subscribe , topic }
		elif (split_txtout[0] == "subscribe" and len(split_txtout) == 3): # Subscribe Mode
			broker_ipaddress,topicname = split_txtout[1],split_txtout[2] 
			addr = (broker_ipaddress, SERV_PORT) # IP with port 
			print('Subscribe to IP:' + broker_ipaddress + '. Topic:' + topicname)
			
			# Make string and send to broker  
			data_Send = 'subscribe:' + topicname
			s.sendto(data_Send.encode('utf-8'), addr) # Convert to byte type and send

			# Subscribe TOPIC from Broker
			Thread(target=handle_client, args=(s,)).start()
			while True:
				try:
					time.sleep(0.01)
				except KeyboardInterrupt: # When user want to unscribe this topic
					data_Send = 'unsubscribe:' + topicname
					s.sendto(data_Send.encode('utf-8'), addr) # Convert to byte type and send
					print ('Stop subscribe topic:' + topicname)
					Thread(target=handle_client, args=(s,))._stop()
					break
		# Error 
		else:
			print("Wrong syntax. Please try agian")
	s.close()

if __name__ == '__main__':
   try:
     main()
   except KeyboardInterrupt:
     print ('Interrupted ..')
     try:
       sys.exit(0)
     except SystemExit:
       os._exit(0)
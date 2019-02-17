from socket import * 
import sys

MAX_BUF = 2048     # Size of buffer to store received bytes
SERV_PORT = 50000  # Server port number

addr = ('127.0.0.1', SERV_PORT) # Socket address
s = socket(AF_INET, SOCK_DGRAM) # Create UDP socket
s.bind(addr)                    # Bind socket to address


subscribe_lst = []


print ('MQTT Broker started ...(UDP)')

while(1):
  print ('>', end = '')
  txtin,addr = s.recvfrom(MAX_BUF)  # txtin stores receive text
  ip, port = str(addr[0]), str(addr[1]) 
  split_txtin = txtin.decode('utf-8').split(':')

  if ( split_txtin[0] == "publish" and len(split_txtin) == 3): # Pulish | Topic | Data
    topic,data = split_txtin[1],split_txtin[2]
    print ('Publish from ' + ip + ':' + port + '\tTopic:' + topic +' Data:' + data)
   
    # Doing some thing with text
    txtout = txtin.upper()     # Change text to upper case

    # Send back to client we need to keep subscribe client to send 
    s.sendto(txtout, addr)     # Send it back to the client

  
  elif ( split_txtin[0] == "subscribe" and len(split_txtin) == 2): # subscribe | Topic 
    print("SUB")
    subscribe_lst.append(ip +':'+ port + ',' + split_txtin[1]) # Make array list of subscribe with topic
    print(ip +':'+ port + 'add to array list with topic:' + split_txtin[1])

    print ('Subscribe list : ' + str(subscribe_lst))

  else:
    print("Error : received message error ( Wrong argument or something) ")



	
s.close()

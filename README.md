"# MQTT_Project_GroupUbiquitous" 
This project is for CPE314 : Computer Networks (2/2561) Project 1


Software Requirements
1. The subscriber subscribes to a given topic with the command line:

subscribe broker_ip_address 'topic_name'

For example, to subscribe to the topic /room1/light with the broker ip address 202.44.12.85, enter
the command

subscribe 202.44.12.85 '/room1/light'

Once started, the subscriber program stays running to receive published messages and print them
on the screen, and terminates when receiving Ctrl-C key or something similar from the user input.

2. The publisher publishes data to a given topic with the command line:

publish 'broker_ip_address' 'topic_name' 'data to publish'

For example,
publish 202.44.12.85 '/room1/light' 'value=on'
publish 10.0.3.2 '/room2/lcd' 'hello world'

3. The broker prints out a message received from a publisher and sends it to all subscribers for that topic.
The broker must be able to handle multiple publishers and subscribers for different topics at the same
time.

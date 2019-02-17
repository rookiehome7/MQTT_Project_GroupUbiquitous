print('Enter command:')
command = input()
split_command = command.split()
if split_command[0] == "subscribe":
    print("subscribe")
elif split_command[0] == "publish":
    print("publish")
else:
    print("Try again")
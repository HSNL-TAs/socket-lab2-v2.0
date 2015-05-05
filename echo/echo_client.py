import socket

host = socket.gethostname()

port = 5566

# 1. Please write down the code
# Create a TCP socket with IPv4 and TCP
# s =

# 2. Please write down the code
# Using socket instance's method 'connect' to connect host and port
# Hint: The parameter is (host, port)
#


while True:

    # 3. Please write down the code which is getting user input from console
    # msg = ...

    # 4. Please write down the code,
    # if msg string is equal to ":exit" than break the loop
    # if ...
    #     print('Disconnected from server..')
    #

    # 5. Please write down the code,
    # Using socket instance's method 'sendall' to send msg
    #

    # 6. Please write down the code,
    # Using socket instance's method 'recv' to receive data with buffer size 1024


    # Print the data from server sent
    print '[!] Server says: %s' % data

# 7. Please write down the code,
# Don't forget to close the socket
#

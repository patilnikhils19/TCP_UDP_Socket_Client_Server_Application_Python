Execute
Part 1

Execute Command on server from client with specific number of execution count and given delay using TCP

on server side
$python TCPserver.py -p(port number)

on client side

$python TCPclient.py -s(server IP) -p(port number) -c(cmd) -n(execution number) -d(delay)

Part 2

Execute Command on server from client with specific number of execution count and given delay using UDP
Execute
on server side
$python UDPserver.py -p(port number)

on client side

$python UDPclient.py -s(server IP) -p(port number) -c(cmd) -n(execution number) -d(delay)


Part 3

Run Command Like Command Line Interface.

Run part 2 with execution count = 0

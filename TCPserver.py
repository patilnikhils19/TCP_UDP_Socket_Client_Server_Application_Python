import socket
import subprocess
import sys
import os
import time
import argparse
import thread
from thread import *
import datetime

def server():

    #host = socket.gethostname() #Get Host Name
    host = "127.0.0.1"
    port = args.port #Get port name from the arguments

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Define socket
    sock.bind((host,port)) #Bind Socket To Address

    sock.listen(5) #Put server in listening mode 
    print "Server is listening"

    while True:
       connection, address = sock.accept() #Accept connection from the clients
       print "the connection from the IP address" + str(address)
       print "The Date and Time\t"
       print datetime.datetime.now() #Print date and time at the time of connection
       start_new_thread(thread,(connection,)) #Create new threads for connecting clients
    sock.close()

def thread(connection):
       data = connection.recv(4096) #Recieve data from client
       data1 = str(data)
       d = data1.split('^^^')
       cmd = d[0]
       number = d[2]
       delay  = d[1]
       number = int(number)
       delay = float(delay)
       cmd = str(cmd)
       print "\nfrom connected client command is\n" + str(cmd)
       print "\nfrom connected client delay is\n" + str(delay)
       print "\nfrom connected client execution count is\n" + str(number)
       if number == 0: #If execution count is zero run in interactive mode
          endtime = time.time() + delay
          while (time.time() < endtime):  # Run in interactive mode for the specified delay time 
             p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
             if p:
                  out = p.stdout.read()
                  connection.sendall(out)
             cmd = connection.recv(4096)
          print "Interacive mode is closed"
          connection.close() # close the connection after specified time delay
       else : #Run in normal mode if execution count is not zero
        if str(cmd) != 'None' :
       	  while (number):
            time1 = time.time() #set timer for counting execution time
            p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate() #Initiate subprocess to execute the command and take output or error
            time2 = time.time()
            processtime = time2 - time1
            processtime = str(processtime)
            if out:

                        connection.sendall(out) # Send output of the client
                        connection.sendall("\nThe Process Time\t")
                        connection.sendall(processtime) #send the process time to client
            else :
                        connection.send(err)
            time.sleep(delay)
            print "\nDelay in between commands\n", delay
            number = number-1
       print "server is working"
       connection.close()#Close the connection


if __name__ == '__main__':

    parser = argparse.ArgumentParser() #define argument parser
    parser.add_argument("-p","--port",help="Port Number",type=int)
    args = parser.parse_args()
    if not args.port:
           print("Need Port Number")

    else :
           server()

                                           

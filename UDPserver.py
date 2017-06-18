import socket
import subprocess
import sys
import os
import time
import argparse
import datetime
def server():
         # host = socket.gethostbyname(server-2.NSP-Lab03.ch-geni-net.instageni.rnoc.gatech.edu)
         # host = '127.0.0.1'
          host = socket.gethostname()#Get Host Name
          print host
          port = args.port#Get port name from the 

          sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#create socket
          sock.bind((host, port))

          print "server is working"
          while True:
                cmd, address = sock.recvfrom(1024)#receive command from the client
                delay, address = sock.recvfrom(1024)#receive delay from client
                number, address = sock.recvfrom(1024)#recieve number from the client

                print "connection from:\t" + str(address) #print client address
                print "The Date and Time\t"
                print datetime.datetime.now() #Print date and time at the time of connection
                print "\nfrom connected client command is\n" + str(cmd) 
                print "\nfrom connected client delay is\n" + str(delay)
                print "\nfrom connected client execution count is\n" + str(number)
                number = int(number)
                delay = float(delay)
                if cmd != str('None'):
                   while (number):
                        time1 = time.time()
                        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                        out, err = p.communicate()
                        time2 = time.time()
                        processtime = time2 - time1
                        processtime = str(processtime)
                        if out:
                                sock.sendto(out, address)#send output to client
                                sock.sendto(processtime, address)#send process time to client
                        else :
                                sock.sendto(err, address)
                        time.sleep(delay)
                        print "\nDelay in between commands\n", delay
                        number = number-1
                print "server is working"
          sock.close()

if __name__ == '__main__':

          parser = argparse.ArgumentParser()#Define the argument perser
          parser.add_argument("-p","--port",help="Port Number",type=int)
          args = parser.parse_args()
          if not args.port :
                 print("Need Port number")
          else :
                server()#Run server


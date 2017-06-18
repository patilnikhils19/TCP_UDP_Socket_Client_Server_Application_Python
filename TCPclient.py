import os
import argparse
import sys
import socket
import time

def client():

    host = args.serverIP # Get server IP from argument
    port = args.port # Get port number from argument
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Create Socket
    sock.connect((host,port)) #Connect to server
    if not args.command:
       command = str('None')
    else:
       command = (args.command)
    if not args.number:
       args.number = 1
       number = (args.number)
    else :
       number = (args.number)
    if not args.delay:
       args.delay = 0
       delay = (args.delay)
    else :
       delay = (args.delay)
    delay = str(delay)
    number = str(number)
    data =command+'^^^'+delay+'^^^'+number
    data1 = str(data)
    sock.send(data1) # Send data to server

    while True:
            data = sock.recv(4096)# Recieve data from server
            if data :
                 print "\nThe output is\n" + str(data) #print data from server
            else :
                 break
    sock.close()


def interactive():

    host = args.serverIP # Get server IP from argument
    port = args.port # Get port number from argument
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Create Socket
    sock.connect((host,port))#Connect to server
    delay = args.delay
    number = args.number
    print "Interactive mode print command"
    commd = raw_input(">>")
    delay = str(delay)
    number = str(number)
    data =commd+'^^^'+delay+'^^^'+number
    data1 = str(data)
    sock.send(data1) # Send data to server
    number = args.number
    delay = args.delay
    endtime = time.time() + delay
    while (time.time() < endtime):
   # while True:
          output = sock.recv(4096)#Recieve data from server
          print "Execution data from server\n" + output
          commd = raw_input(">>")
          sock.send(commd)
    print "Delay Time is over"
    sock.close()


if __name__ == '__main__':

          parser = argparse.ArgumentParser()
          parser.add_argument("-s","--serverIP",help="Server IP address",type=str)
          parser.add_argument("-p","--port",help="Port Number",type=int)
          parser.add_argument("-c","--command",help="Linux Command")
          parser.add_argument("-d","--delay",help="Delay between two execution", type= float)
          parser.add_argument("-n","--number",help="Command Execution number", type=int)
          args = parser.parse_args()

          if not args.serverIP or  not args.port :
                 print("Need ServerIP and Port number")


         # if args.number:
          elif args.number and (args.number < 0) :

                 print("Please give valid execution count")

         # if args.delay:
          elif args.delay and (args.delay < 0) :
                 print("Please give valid delay time in sec.")
                
          elif args.number == 0 :
                 if  not args.delay or args.delay == 0:
                      print ("Please give time delay for interactive operation")
                 else :
                      interactive()

          else :
                client()


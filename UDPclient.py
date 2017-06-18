import os
import argparse
import sys
import socket


def client():

    host = args.serverIP #Get Host IP from arguments
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#create socket
    sock.bind((host, args.port))
    server = (host,args.port)
    command = str(args.command)# Take command from argument
    print command
    if not args.delay:
       args.delay = 0
       delay = str(args.delay)
    else :
       delay = str(args.delay)
    if not args.number:
       args.number = 1
       number =str(args.number)
    else :
       number =str(args.number)

    sock.sendto(command, server)#Send Command to server
    sock.sendto(delay, server)#Send Delay to server
    sock.sendto(number, server)#send Execution count to server
    number = int(number)
    while(number):
         data, address = sock.recvfrom(1024)#Recieve data from server
         processtime, address = sock.recvfrom(1024)#Recieve process time from server
         print "\nthe output is\n" + str(data)
         print "the Process Time\t" + str(processtime) +"\n\n"
         number = number-1
    sock.close()


if __name__ == '__main__':

          parser = argparse.ArgumentParser()#Define argument parser
          parser.add_argument("-s","--serverIP",help="Server IP address",type=str)
          parser.add_argument("-p","--port",help="Port Number",type=int)
          parser.add_argument("-c","--command",help="Linux Command")
          parser.add_argument("-d","--delay",help="Delay between two execution", type= float)
          parser.add_argument("-n","--number",help="Command Execution number", type=int)
          args = parser.parse_args()

          if not args.serverIP or  not args.port :
                 print("Need ServerIP and Port number")

          elif args.number and (args.number < 0) :
                 print("Please give valid execution count")
          
          elif  (args.number == 0):
                 print("Please give non zero execution count")

          elif args.delay and (args.delay < 0) :
                 print("Please give valid delay time in sec.")

          else :
                client()



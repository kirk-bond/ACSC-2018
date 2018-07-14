#!/usr/bin/env python2

import socket
import sys
import time
from thread import *
from random import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5000 # Arbitrary non-privileged port
FLAG = "acsc18{SameScriptMinorChange}"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Think you are good at math? Answer 100 simple problems in 2 minutes and you get your flag.\n') #send only takes string

    start_time = time.time()

    for i in range (0,100):
      #Deteremine what type of operation this loop will be
      x = randint(1,3)
      # Addition
      if x == 1:
        a = randint(1,10000)
        b = randint(1,10000)
        answer = a + b
        conn.send('  ' + str(a) + '\n+ ' + str(b) + '\n---------\n')
      # Subtraction
      elif x == 2:
        a = randint(10000,100000)
        b = randint(1,9999)
        answer = a - b
        conn.send('  ' + str(a) + '\n- ' + str(b) + '\n---------\n')
      # Multipication
      elif x == 3:
        a = randint(1,1000)
        b = randint(1,1000)
        answer = a * b
        conn.send('  ' + str(a) + '\nx ' + str(b) + '\n---------\n')

      #Get user answer
      userAnswer = conn.recv(1024)

      try:
        if int(userAnswer) == int(answer):
          conn.send("correct\n")
          continue
      except:
        pass

      # On exception or wrong answer
      conn.send("wrong\n")
      conn.close()
      sys.exit()

    end_time = time.time()
    elapsedtime = end_time - start_time

    #Check to see if they were fast enough
    if elapsedtime > 120:
      conn.send("Two Slow\n")
      conn.close()
      sys.exit()

    #Send the flag
    conn.send(FLAG+'\n')

    #came out of loop
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()

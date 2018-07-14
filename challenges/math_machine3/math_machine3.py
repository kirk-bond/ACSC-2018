#!/usr/bin/env python2

import socket
import sys
import time
from thread import *
from random import *

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5100 # Arbitrary non-privileged port
FLAG = "acsc18{WordsMatter}"

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

#Function to convert number to words
def Num2Word(intNumber):
    SINGLE = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', \
             '10':'Ten', '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', \
             '18':'Eighteen', '19':'Nineteen'}
    DOUBLES = {'20':'Twenty', '30':'Thirty', '40':'Forty', '50':'Fifty', '60':'Sixty', '70':'Seventy', '80':'Eighty', '90':'Ninety'}

    OUTPUT = ''
    THOUSANDS = intNumber // 1000
    if THOUSANDS > 0:
        OUTPUT = SINGLE.get(str(THOUSANDS)) + " Thousand"
        intNumber = intNumber - (THOUSANDS * 1000)

    HUNDREDS = intNumber // 100
    if HUNDREDS > 0:
        OUTPUT = OUTPUT + " " + SINGLE.get(str(HUNDREDS)) + " Hundred"
        intNumber = intNumber - (HUNDREDS * 100)

    if intNumber < 20:
        OUTPUT = OUTPUT + " " + SINGLE.get(str(intNumber))
    else:
        TENS = intNumber // 10
        TENS = TENS * 10
        OUTPUT = OUTPUT + " " + DOUBLES.get(str(TENS))
        intNumber = intNumber - (TENS)

        if intNumber > 0:
            OUTPUT = OUTPUT + "-"+SINGLE.get(str(intNumber))

    return OUTPUT

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Same as last time, but with just a little bit of a twist\n') #send only takes string

    start_time = time.time()

    for i in range (0,100):
      #Deteremine what type of operation this loop will be
      x = randint(1,4)
      # Addition
      if x == 1:
        a = randint(1,9999)
        b = randint(1,9999)
        answer = a + b
        conn.send(Num2Word(a) + " Plus " + Num2Word(b) + '\n')
      # Subtraction
      elif x == 2:
        a = randint(5000,9999)
        b = randint(1,4999)
        answer = a - b
        conn.send(Num2Word(a) + " Minus " + Num2Word(b) + '\n')
      # Multipication
      elif x == 3:
        a = randint(1,9999)
        b = randint(1,9999)
        answer = a * b
        conn.send(Num2Word(a) + " Times " + Num2Word(b) + '\n')
      elif x == 4:
        a = randint(1,100)
        b = randint(1,99)
        answer = b
        conn.send(Num2Word(b*a) + " Divided By " + Num2Word(a) + '\n')


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

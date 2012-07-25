#!/bin/env python2.7

###
### Install http://pyserial.sourceforge.net/pyserial.html#installation
###

import re
import sys
import serial
import time
import urllib2
import json

import settings

### SETUP
def setup():
  bestand=open(settings.FONTFILE)
  # Parse chars
  global abc
  abc={}
  for line in bestand.readlines():
    line = line.strip(settings.NEWLINES)
    if line[:5]=='BEGIN':
      xy={}
      letter=line[6:7]
      y=0
    elif line[:3]=='END':
      abc[letter]={'width':len(charline),'xy':xy}
    else:
      # Parse letterline
      xy[y]=line

      charline=line
      y+=1

  bestand.close()
  if settings.DEBUG:
    print 'Known characters:'
    print ''.join(abc.keys())
  global ser
  ser = serial.Serial(settings.TTY,settings.BAUD,timeout=1)
  ser.read(1000)
  time.sleep(2)
  ser.write("SRGBF")

def genOutput(text):
  # Build lines
  totalWidth=0
  lines={0:'',1:'',2:'',3:'',4:'',5:''}
  charNum=0;
  for char in text:
    try:
      lineDict=abc[char.upper()]['xy']
      totalWidth+=abc[char.upper()]['width']
    except KeyError:
      lineDict=abc['*']['xy']
      totalWidth+=abc['*']['width']
      print "Ik ken dit teken niet: "+char

    # Colors for this char:
    try:
      thisColorNum=color[charNum].upper()
      thisColor=settings.COLORS[thisColorNum]
    except:
      thisColor='G'

    for y in range(6):
      lines[y]+= lineDict[y].replace('1',thisColor)

    charNum+=1

  spacer='..........................'
  for y in range(6):
    #lines[y]=lines[y]+spacer
    lines[y]=spacer+lines[y]+spacer
    if settings.DEBUG:
      print lines[y]

  #Steps:
  stepOutLines=[]
  for step in range(1,totalWidth+27):
    curLines={0:'',1:'',2:'',3:'',4:'',5:''}

    # Cut stukje
    for y in range(6):
      curLines[y]+=lines[y][step:step+26]

    stepOutLines.append(curLines)
  return stepOutLines
  
def sendSerial(x):
  if settings.DEBUG:
    print "Sending: " + x
  ser.write(x)

def sendToBanner(text):
  # Send lines
  
  stepOutLines=genOutput(text)

  sendSerial('S')

  for stepOutLine in stepOutLines:
    #Each step
    if(len(stepOutLine[0])<26):
      break

    for y in range(6):
      #Each line
      thisLine=stepOutLine[y].replace('0','.')

      if(y%2==0):
        sendSerial(thisLine)
      else:
        sendSerial(thisLine[::-1])

    sendSerial('F')

    time.sleep(sleepTime)

def looper():
  global text
  global color
  global sleepTime


  try:
    while True:
      #What is the text?
      textfile=urllib2.urlopen(settings.TEXTURL)
      jsonFromFile=json.loads( textfile.read() )
      textfile.close()
      text= jsonFromFile['data']
      color= jsonFromFile['colors']
      sleepTime = jsonFromFile['time']
      if settings.DEBUG:
        print text,color
      #Now we have text, send!
      sendToBanner(text)
  except KeyboardInterrupt:
    print "Bye!"
    ser.close()
    sys.exit()
    
if __name__=="__main__":
  setup()
  while True:
    looper()

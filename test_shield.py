# The following script communicates the values of inputs into the Arduino shield of the 2013 Bulldogs Racing car.
# By Alex Carrillo <alejandro.carrillo@yale.edu>

import serial
import curses
import sys
from datetime import datetime


#ser=serial.Serial('/dev/tty.usbmodem411')
ser=serial.Serial('/dev/tty.usbmodem621')

stdscr=curses.initscr()
stdscr.keypad(1)
stdscr.nodelay(1)
stdscr.leaveok(1)
curses.noecho()
curses.cbreak()

pad = curses.newpad(100, 100)

values= {}

try:
    while 1:
        if stdscr.getch()==ord('q'):
            break
        line=ser.readline()
        items=line.split()
      #  if items[0] in values:
        values[items[0]] = items[1]
      #  else:
      #     raise
        pad.addstr(0,0, "RPM:");pad.addstr(0,20,str(values.get("RPM")))
        pad.addstr(1,0, "Temp:"); pad.addstr(1,20,str(values.get("Temp")))
        pad.addstr(2,0, "Low Battery:");pad.addstr(2,20,str(values.get("BattLow")))
        pad.addstr(3,0, "FuelIn:"); pad.addstr(3,20,str(values.get("FuelIn")))
        pad.addstr(4,0, "Throttle:"); pad.addstr(4,20,str(values.get("ThrottleIn")))
        pad.addstr(5,0, "BMS Fault:"); pad.addstr(5,20,str(values.get("BMS_Fault")))
        pad.addstr(6,0, "Clutch:"); pad.addstr(6,20,str(values.get("Clutch")))
        pad.addstr(7,0, "Assist In:"); pad.addstr(7,20,str(values.get("AssistIn")))
        pad.addstr(8,0, "Brake In:"); pad.addstr(8,20,str(values.get("BrakeIn")))
        stdscr.refresh()
        pad.refresh( 0,0, 5,5, 20,75)
        #print "RPM\t",rpm,"\tTemp\t",temp,"\tLow Battery\t",battlow,"\tFuelIn\t",fuelin,"\tThrottle\t",throttlein,"\tBMS Fault\t",bmsfault,"\tClutch\t",clutch,"\tAssist In\t",assist,"\tBrake In\t",brake

except:
    # Quit!
    curses.nocbreak(); stdscr.keypad(0); curses.echo()
    curses.endwin()
    print "Error\n"
    print sys.exc_info()[0]

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

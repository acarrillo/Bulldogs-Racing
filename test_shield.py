import serial
import curses
from datetime import datetime
stdscr=curses.initscr()
stdscr.keypad(1)
stdscr.nodelay(1)
stdscr.leaveok(1)
curses.noecho()
curses.cbreak()

stdscr=curses.initscr()
stdscr.keypad(1)
stdscr.nodelay(1)
stdscr.leaveok(1)

#ser=serial.Serial('/dev/tty.usbmodem621')
pad = curses.newpad(100, 100)
ser=serial.Serial('/dev/tty.usbmodem411')

rpm = 0
temp = 0
battlow = 0
fuelin = 0
throttlein = 0
bmsfault = 0
clutch = 0
assist = 0
brake = 0


while 1:
    if stdscr.getch()==ord('q'):
        break
    line=ser.readline()
    items=line.split()
    if items[0] == "RPM":
        rpm = items[1]
    elif items[0] == "Temp":
        temp = items[1]
    elif items[0] == "BattLow":
        battlow = items[1]
    elif items[0] == "FuelIn":
        fuelin = items[1]
    elif items[0] == "ThrottleIn":
        throttlein = items[1]
    elif items[0] == "BMS_Fault":
        bmsfault = items[1]
    elif items[0] == "Clutch":
        clutch = items[1]
    elif items[0] == "AssistIn":
        assist = items[1]
    elif items[0] == "BrakeIn":
        brake = items[1]
    pad.addstr(0,0, "RPM:");pad.addstr(0,20,str(rpm))
    pad.addstr(1,0, "Temp:"); pad.addstr(1,20,str(temp))
    pad.addstr(2,0, "Low Battery:\t\t" + str(battlow))
    pad.addstr(3,0, "FuelIn:\t\t" + str(fuelin))
    pad.addstr(4,0, "Throttle:\t\t" + str(throttlein))
    pad.addstr(5,0, "BMS Fault:\t\t" + str(bmsfault))
    pad.addstr(6,0, "Clutch:\t\t" + str(clutch))
    pad.addstr(7,0, "Assist In:\t\t" + str(assist))
    pad.addstr(8,0, "Brake In:\t\t" + str(brake))
    stdscr.refresh()
    pad.refresh( 0,0, 5,5, 20,75)
    #print "RPM\t",rpm,"\tTemp\t",temp,"\tLow Battery\t",battlow,"\tFuelIn\t",fuelin,"\tThrottle\t",throttlein,"\tBMS Fault\t",bmsfault,"\tClutch\t",clutch,"\tAssist In\t",assist,"\tBrake In\t",brake

curses.nocbreak(); stdscr.keypad(0); curses.echo()
curses.endwin()

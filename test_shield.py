import serial
ser=serial.Serial('/dev/tty.usbmodem621')

rpm = 0
temp = 0
battlow = 0
fuelin = 0
throttlein = 0
bmsfault = 0
clutch = 0


while 1:
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
    print "RPM\t",rpm,"\tTemp\t",temp,"\tLow Battery\t",battlow,"\tFuelIn\t",fuelin,"\tThrottle\t",throttlein,"\tBMS Fault\t",bmsfault,"\tClutch\t",clutch

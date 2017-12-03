import fcntl,socket, struct, dweepy, time, platform, random
import time
import grovepi
from grovepi import *

#ports
dht_sensor_port = 7
led = 5
button = 3
potentiometer = 2

pinMode(led,"OUTPUT")
i=0
pinMode(button,"INPUT")


def getTemp():
    [ temp,hum ] = dht(dht_sensor_port,0)
    
    t=temp
    
    
    return t
    
def getHumidity():
    [ temp,hum ] = dht(dht_sensor_port,0)
    
    h=hum
    
    
    return h
    
def getOS():
    return platform.platform()
    
    
def getLed():
        # Read resistance from Potentiometer
        i = grovepi.analogRead(potentiometer)

        # Send PWM signal to LED
        grovepi.analogWrite(led,i//4)
        
        return i
        
def getButton():
    return grovepi.digitalRead(button)

    
       
# from http://stackoverflow.com/questions/159137/getting-mac-address
def getHwAddr(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info = fcntl.ioctl(s.fileno(), 0x8927,  struct.pack('256s', ifname[:15]))
    return ':'.join(['%02x' % ord(char) for char in info[18:24]])

def post(dic):
    thing = 'therapeutic-caption'
    print dweepy.dweet_for(thing, dic)
    
def getReadings():
    dict = {}
    dict["LED"] = getLed();
    dict["temperature"] = getTemp();
    dict["mac-address"] = getHwAddr('eth0')
    dict["humidity"] = getHumidity()
    dict["operating system"] = getOS()
    dict["button"] = getButton()
    return dict

while True:
    dict = getReadings();
    post(dict)
    time.sleep(5)

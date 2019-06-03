import serial
import serial.tools.list_ports
import time
global ser
def open():
    global ser
    ports = list(serial.tools.list_ports.comports())
    ser=serial.Serial(port='COM6')
    """for p in ports:
        print (p[1])
        if "SERIAL" in p[1] or "CH340" in p[1]:
            ser=serial.Serial(port=p[1])
            if ser is not None:
                print(ser)
            else:
                print("serial not connected")
                break
    else:

        print ("No CH340 Device was found connected to the computer")"""
    print(ser)
def close():
    global ser
    ser.close()
    print (ser)
def yaotou():
    open()
    global ser
    #open()
    m0 = bytes.fromhex("ff 01 08 0b 00") #初始化摇头速度100
    m00 = bytes.fromhex("ff 02 08 e8 03") #初始化头的位置90
    ser.write(m0)
    ser.write(m00)
    time.sleep(1)
    i = 0
    for i in range(5):
        m01 = bytes.fromhex("ff 02 08 00 00")#向左摇头0
        ser.write(m01)
        time.sleep(1)
        m02 = bytes.fromhex("ff 02 08 d0 07")#向右摇头180
        ser.write(m02)
        time.sleep(1)
    close()

def shengqi():
    open()
    global ser
    m1 = bytes.fromhex("ff 01 09 14 00") #初始化速度180
    m10 = bytes.fromhex("ff 02 09 00 00")#初始化位置0
    ser.write(m1)
    ser.write(m10)
    time.sleep(1)
    m11 = bytes.fromhex("ff 02 09 e8 03") #向上举手位置180
    ser.write(m11)
    time.sleep(1)
    m12 = bytes.fromhex("ff 02 09 00 00") #放下手 0
    ser.write(m12)
    time.sleep(1)
    close()
def gaoxin():
    open()
    global ser
    m1 = bytes.fromhex("ff 01 09 14 00") #初始化速度180
    m2 = bytes.fromhex("ff 01 0a 14 00") #初始化速度180
    m10 = bytes.fromhex("ff 02 09 00 00")#初始化位置0
    m20 = bytes.fromhex("ff 02 0a 00 00")#初始化位置0
    ser.write(m1)
    ser.write(m10)
    ser.write(m2)
    ser.write(m20)
    time.sleep(1)
    m11 = bytes.fromhex("ff 02 09 e8 03") #向上举手位置180
    m21 = bytes.fromhex("ff 02 0a e8 03") #向上举手位置180
    ser.write(m11)
    ser.write(m21)
    time.sleep(1)
    m12 = bytes.fromhex("ff 02 09 00 00") #放下手 0
    
    m22 = bytes.fromhex("ff 02 0a 00 00") #放下手 0
    ser.write(m12)
    ser.write(m22)
    time.sleep(1)
    close()
def jushou():
    open()
    global ser
    m1 = bytes.fromhex("ff 01 09 14 00") #初始化速度180
    m10 = bytes.fromhex("ff 02 09 00 00")#初始化位置0
    ser.write(m1)
    ser.write(m10)
    time.sleep(1)
    m11 = bytes.fromhex("ff 02 09 e8 03") #向上举手位置180
    ser.write(m11)
    time.sleep(1)
    close()

    

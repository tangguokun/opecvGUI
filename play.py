#!/usr/bin/env python

# -*- coding: gb2312 -*-
import wave
import time
from pyaudio import PyAudio,paInt16
chunk = 2014

def play():
    wf=wave.open("oop.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    n=0
    print(n)

    while True:
        data=wf.readframes(chunk)
        #if data=="":break
        stream.write(data)
        n=n+1
        print("1")
        if n==100:
            print("3")
            n=0
            break
        #time.sleep(10000)
    stream.close()
    print("2")
    p.terminate()
    wf.close()
play()
def play2():
    wf=wave.open("xihuan.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    n=0
    print(n)

    while True:
        data=wf.readframes(chunk)
        #if data=="":break
        stream.write(data)
        n=n+1
        print("1")
        if n==100:
            print("3")
            n=0
            break
        #time.sleep(10000)
    stream.close()
    print("2")
    p.terminate()
    wf.close()
def play3():
    wf=wave.open("seeyou.wav",'rb')
    p=PyAudio()
    stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),channels=
    wf.getnchannels(),rate=wf.getframerate(),output=True)
    n=0
    print(n)

    while True:
        data=wf.readframes(chunk)
        #if data=="":break
        stream.write(data)
        n=n+1
        print("1")
        if n==100:
            print("3")
            n=0
            break
        #time.sleep(10000)
    stream.close()
    print("2")
    p.terminate()
    wf.close()

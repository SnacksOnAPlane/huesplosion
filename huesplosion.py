#!/usr/bin/python

from phue import Bridge
from random import randint
import time

LIGHT_NAMES = ['bloom']
DELAY = 20
BRIDGE_IP = '192.168.1.81'

br = Bridge(BRIDGE_IP)
br.connect()

def changeColor():
  color = randint(1, 65535)
  br.set_light(LIGHT_NAMES, 'hue', color)
  br.set_light(LIGHT_NAMES, 'bri', 254)
  br.set_light(LIGHT_NAMES, 'bri', 0, transitiontime=DELAY)

while(True):
  changeColor()

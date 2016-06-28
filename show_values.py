#!/usr/env python

from pydimitri import *
from time import time

d = Dimitri()

t = time()
while (True):
    d.receiveAngles()
    for index in d.joints:
        if index:
            print index+':'+d.joints[index].currValue, 
        print time() - t
        t = time()


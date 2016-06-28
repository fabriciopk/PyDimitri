#!/usr/bin/env python

from PyDynamixel import Joint, DxlComm
from pysea import Spring, SEA
from math import pi

# Open the sockets
port1 = DxlComm('/dev/ttyS0', 8)
port2 = DxlComm('/dev/ttyS0', 8)

# Create one servo and one spring
j = Joint(14)
s = Spring(103)

# Attach the objects to the socket
# objects for communication
port1.attachJoint(j)
port2.attachJoint(s)

# Create the SEA object
sea = SEA(j,s)

# Set the goal position
sea.setGoalAngle(pi/2)

# Get the spring readings
port2.receiveAngles()

# Update the goal values
# for the servomotors to
# compensate the spring
sea.update()

# Send the message to the
# motors
port1.sendGoalAngles()


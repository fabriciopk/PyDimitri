from PyDynamixel import Joint, DxlComm
from pysea import Spring, SEA
from math import pi

class Dimitri(object):
    def __init__(self):

        '''
        '''

        # Ports
        self.trunk = DxlComm('/dev/ttyS11', 8)
        self.leftLeg = DxlComm('/dev/ttyS4', 8)
        self.rightLeg = DxlComm('/dev/ttyS5', 8)
        self.seas = DxlComm('/dev/ttyS6', 8)
        
        # Feet
        self.left_foot_roll = Joint(11)
        self.right_foot_roll = Joint(12)
        self.left_foot_pitch = Joint(13)
        self.right_foot_pitch = Joint(14)

        # Lower leg
        self.left_lower_leg = Joint(15)
        self.right_lower_leg = Joint(16)
        self.left_lower_spring = Spring(101)
        self.right_lower_spring = Spring(102)
	self.left_lower_leg_sea = SEA(self.left_lower_leg, self.left_lower_spring)
	self.right_lower_leg_sea = SEA(self.right_lower_leg, self.right_lower_spring)	

        # Upper leg
        self.left_upper_leg = Joint(21)
        self.right_upper_leg = Joint(22)
        self.left_upper_spring = Spring(103)
        self.right_upper_spring = Spring(104)
	self.left_upper_leg_sea = SEA(self.left_upper_leg, self.left_upper_spring)
	self.right_upper_leg_sea = SEA(self.right_upper_leg, self.right_upper_spring)

        # Thigh
        self.left_leg_roll = Joint(23)
        self.right_leg_roll = Joint(24)
        self.left_leg_pitch = Joint(25)
        self.right_leg_pitch = Joint(26)
        self.left_leg_yaw = Joint(27)
        self.right_leg_yaw = Joint(28)

        # Arms
        self.left_arm_roll = Joint(31)
        self.right_arm_roll = Joint(32)
        self.left_arm_pitch = Joint(33)
        self.right_arm_pitch = Joint(34)
        self.left_arm_yaw = Joint(35)
        self.right_arm_yaw = Joint(36)
        self.left_elbow = Joint(41)
        self.right_elbow = Joint(42)

        # Waist
        self.waist_roll = Joint(51)
        self.waist_pitch = Joint(52)
        self.waist_yaw = Joint(53)

        # Head
        self.neck_pitch = Joint(61)
        self.neck_yaw = Joint(62)


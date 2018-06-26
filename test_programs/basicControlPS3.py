# Libraries
import RPi.GPIO as GPIO
import time
import pygame, sys
from time import sleep
import numpy as np

# setup the pygame window
pygame.init()
window = pygame.display.set_mode((200, 200), 0, 32)

# how many joysticks connected to computer?
joystick_count = pygame.joystick.get_count()
print("There is " + str(joystick_count) + " joystick/s")

if joystick_count == 0:
    # if no joysticks, quit program safely
    print ("Error, I did not find any joysticks")
    pygame.quit()
    sys.exit()
else:
    # initialise joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

axes = joystick.get_numaxes()
buttons = joystick.get_numbuttons()
hats = joystick.get_numhats()

def getAxis(number):
    # when nothing is moved on an axis, the VALUE IS NOT EXACTLY ZERO
    # so this is used not "if joystick value not zero"
    if joystick.get_axis(number) < -0.1 or joystick.get_axis(number) > 0.1:
      # value between 1.0 and -1.0
      print ("Axis value is %s" %(joystick.get_axis(number)))
      print ("Axis ID is %s" %(number))
 
def getButton(number):
    # returns 1 or 0 - pressed or not
    if joystick.get_button(number):
      # just prints id of button
      print ("Button ID is %s" %(number))

def getHat(number):
    if joystick.get_hat(number) != (0,0):
      # returns tuple with values either 1, 0 or -1
      print ("Hat value is %s, %s" %(joystick.get_hat(number)[0],joystick.get_hat(number)[1]))
      print ("Hat ID is %s" %(number))


# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
# set GPIO Pins
GPIO_Apwm = 6
GPIO_Ain1 = 13
GPIO_Ain2 = 19

GPIO_Bin1 = 16
GPIO_Bin2 = 20
GPIO_Bpwm = 21

# Set GPIO direction (IN / OUT)
GPIO.setup(GPIO_Ain1, GPIO.OUT)
GPIO.setup(GPIO_Ain2, GPIO.OUT)
GPIO.setup(GPIO_Apwm, GPIO.OUT)
GPIO.setup(GPIO_Bin1, GPIO.OUT)
GPIO.setup(GPIO_Bin2, GPIO.OUT)
GPIO.setup(GPIO_Bpwm, GPIO.OUT)

# Both motors are stopped 
GPIO.output(GPIO_Ain1, False)
GPIO.output(GPIO_Ain2, False)
GPIO.output(GPIO_Bin1, False)
GPIO.output(GPIO_Bin2, False)

# Set PWM parameters
pwm_frequency = 50

# Create the PWM instances
pwmA = GPIO.PWM(GPIO_Apwm, pwm_frequency)
pwmB = GPIO.PWM(GPIO_Bpwm, pwm_frequency)

# Set the duty cycle (between 0 and 100)
# The duty cycle determines the speed of the wheels
pwmA.start(100)
pwmB.start(100)

'''
# The PWM pins are set permanently to HIGH
# This sets the motor speed for both to the maximum value
# If we want to change the motor speed, we need to
# attach a PWM signal to these pins
GPIO.output(GPIO_Apwm, True)
GPIO.output(GPIO_Bpwm, True) 
'''


if __name__ == '__main__':
	try:
		
		while True:
			
			
			for event in pygame.event.get():
				# loop through events, if window shut down, quit program
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()

			j1 = joystick.get_axis(1)
			j3 = joystick.get_axis(3)
			print("axis 1: " + str(j1))
			print("axis 3: " + str(j3))
			
			if j1 > 0.1:
				GPIO.output(GPIO_Ain1, True)
				GPIO.output(GPIO_Ain2, False)
			else:
				if j1 < -0.1:
					GPIO.output(GPIO_Ain1, False)
					GPIO.output(GPIO_Ain2, True)
					
				else:
					GPIO.output(GPIO_Ain1, False)
					GPIO.output(GPIO_Ain2, False)
					
			pwmA.ChangeDutyCycle(int(np.abs(j1)*100))

			if j3 > 0.1:
				GPIO.output(GPIO_Bin1, True)
				GPIO.output(GPIO_Bin2, False)
			else:
				if j3 < -0.1:
					GPIO.output(GPIO_Bin1, False)
					GPIO.output(GPIO_Bin2, True)
					
				else:
					GPIO.output(GPIO_Bin1, False)
					GPIO.output(GPIO_Bin2, False)

			pwmB.ChangeDutyCycle(int(np.abs(j3)*100))
			            
        # Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Program stopped by User")
		GPIO.cleanup()
		pygame.quit()
		sys.exit()

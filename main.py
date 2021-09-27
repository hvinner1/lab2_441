import RPi.GPIO as GPIO
from time import sleep # import time.sleep()

GPIO.setmode(GPIO.BCM) # use BCM port numbering
white = 4 # pin number
red = 16
green =12
b1 =17
b2 =21
f = 1 #hertz
dc = 50
Dict = {b1: green, b2: green}


GPIO.setup(white, GPIO.OUT) # assign the pin as output
GPIO.setup(red, GPIO.OUT) # assign the pin as output
GPIO.setup(green, GPIO.OUT) # assign the pin as output
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


try:
  def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)
    if GPIO.input(b1) == GPIO.HIGH:
      pwm = GPIO.PWM(red, 1)
      for dc in range(101):
        pwm.ChangeDutyCycle(dc)
    if GPIO.input(b2) == GPIO.HIGH:
      pwm = GPIO.PWM(green, 1)
      for dc in range(101):
        pwm.ChangeDutyCycle(dc)



  GPIO.add_event_detect(b1, GPIO.RISING, callback=myCallback,
bouncetime=100)
  GPIO.add_event_detect(b2, GPIO.RISING, callback=myCallback,
bouncetime=100)
  while True:
    pwm = GPIO.PWM(white, f) 
    pwm.start (dc)
    



  pwm.start(0) # initiate PWM at 0% duty cycle
  while 1:
    for dc in range(101): # loop duty cycle from 0 to 100
      pwm.ChangeDutyCycle(dc) # set duty cycle
      sleep(0.01) # sleep 10 ms


except KeyboardInterrupt: # stop gracefully on ctrl-C
  print("\nExiting")
except Exception as e: # catch all other errors
  print("\ne")
pwm.stop()
GPIO.cleanup()
#switch 1 pressed


'''
When switch #1 is pressed, LED #1 produces a single cycle of a 1 Hz triangle waveform
(smooth transition from low à high à low).
– When switch #2 is pressed, LED #2 produces a single cycle of a 1 Hz triangle waveform.
– LED #3 continually blinks on/off at 1 Hz, independent other actions.
– Use exception handling to exit elegantly on ctrl-C by cleaning up the GPIO ports.
'''


'''while True: # continuous loop
  if GPIO.input(b1) == GPIO.HIGH:
        print("Button was pushed!")



  GPIO.output(white, 0) # set output to 0V
  sleep(0.5) # wait 0.5 sec
  GPIO.output(white, 1) # set output to 3.3V
  sleep(0.5) # wait 0.5 sec'''
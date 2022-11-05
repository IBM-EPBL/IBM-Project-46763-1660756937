import RPi.GPIO as GPI0
import time


GPIO. setmode(GPIO.BOARD) 
GPIO.setup(7, GPIO.OUT)
 
GPIO.setup(11, GPI0.OUT) 
GPIO.setup(13, GPI0.OUT)

GPI0.setup(15, GPI0.IN, pull_up_down=GPIO.PUD_UP) 
def turn_on (pin, seconds) :
    GPIO.output (pin,GPIO.HIGH) time.sleep(seconds)
def turn_off (pin, seconds) : 
    GPIO.output (pin, GPIO.LOW) time.sleep(seconds)
try :
    while True : 
        button_state=GPIO.input (15) 
        if button_state == True :
            turn_on(13,2) 
            tum_off(13,1) 
            turn_on(7,4) 
            turn_off(7,11) 
            turn_on(11,1) 
            turn_off(11,1)
        else :
            if button_state == False : 
                GPI0.output (7,GPIO.LOW) 
                GPIO.output(11,GPIO.LOW) 
                GPI0.output (13,GPIO.LOW)
                time.sleep(.1) 
except KeyboardInterrupt :
    GPIO.cleanup()
    print("Traffic Light Operation Completed")

from machine import Pin, PWM
import utime

led = Pin(25, Pin.OUT)
spkr = PWM(Pin(0))
spkr.freq(440)
spkr.duty_u16(512)
frequency = 440
duty = 512


col_list = [16]
row_list = [17, 18, 19, 20, 21, 22]
#for x in range(0):
#    row[x] = Pin(row_list[x], Pin.OUT)
#    row[x].value(1)
#for x in range(0, 2):
#    col[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)

col_pins = []
row_pins = []
for i in col_list:
    col_pins.append(Pin(i, Pin.OUT))
for i in row_list:
    row_pins.append(Pin(i, Pin.IN, Pin.PULL_DOWN))


cp0 = Pin(16, Pin.OUT)
cp0.value(1)

rp0 = Pin(17, Pin.IN, Pin.PULL_DOWN)
rp1 = Pin(18, Pin.IN, Pin.PULL_DOWN)
rp2 = Pin(19, Pin.IN, Pin.PULL_DOWN)
rp3 = Pin(20, Pin.IN, Pin.PULL_DOWN)
rp4 = Pin(21, Pin.IN, Pin.PULL_DOWN)
rp5 = Pin(22, Pin.IN, Pin.PULL_DOWN)


def handleButton():
    for pin in row_pins:
        print(str(pin.value()))
    print("\n")
    #we now know what pins are being pressed


#when button pressed

while True:
    duty+=500
    #frequency+=1
    led.toggle()
    utime.sleep(.02)
    if rp0.value() or rp1.value() or rp2.value() or rp3.value() or rp4.value() or rp5.value():
        spkr = PWM(Pin(0))
        spkr.duty_u16(duty)
        handleButton()
    else:
        spkr.deinit()

    '''
    if rp0.value():
        spkr.freq(440)
    elif rp1.value():
        spkr.freq(466)
    elif rp2.value():
        spkr.freq(494)
    elif rp3.value():
        spkr.freq(523)
    elif rp4.value():
        spkr.freq(554)
    elif rp5.value():
        spkr.freq(587)
    '''
    



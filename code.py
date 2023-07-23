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


pitchList = [262, 277, 294, 311, 330, 349]
previousPressed = [0,0,0,0,0,0]
buttonsPressed = [0,0,0,0,0,0]
playingNote = [0,0,0,0,0,0]

#def noteToIndex():


def handleButton():
    global playingNote
    spkr = PWM(Pin(0))
    spkr.duty_u16(duty)
    #del playingNote[:]
    #for button in buttonsPressed:
    #    playingNote.append(0)

    
    #when no other notes playing, play note pressed
    if all(v==0 for v in previousPressed):
        print("first note!")
        playingNote = buttonsPressed
        #expected behaviour:
        # when first note pressed, that note becomes playing note
        # when notes added, playing note changes to most recently
        # pressed note
        #
        # we can do this by checking first case- no notes pressed.
        # if no notes are pressed previously, then just play the note.
        #
        # otherwise, at least one note is already playing- check
        # if a new note has been added or removed. if ADDED, set
        # playing note to most recently pressed key
        #spkr.freq(pitchList[])
    elif previousPressed != buttonsPressed:
        #check if note was added or removed
        if(sum(previousPressed)>sum(buttonsPressed)):
            print("removed")
            #maybe when each new button is pressed, it should just push those indexes to an array 
            # which orders all the buttons pressed, so you can unwind what key is pressed
        else:
            #find new key
            #zip together previousPressed and buttonsPressed
            #grab the difference
            #assume only one new key pressed - go through list of previous pressed.
            #if previous is 0, and current is 1, set playingNote to be that one
            for buttonIndex in range(len(buttonsPressed)):
                if buttonsPressed[buttonIndex] == 1:
                    #check against previousPressed, if previousPressed is zero, set that as new button and.. break?
                    if previousPressed[buttonIndex] == 0:
                        playingNote = [0,0,0,0,0,0]
                        playingNote[buttonIndex] = 1
                        break
                    pass #do something
            print(zip(previousPressed,buttonsPressed))
            print("added")
            #keyReleased
            #need to use
        print("changed note!")
        #spkr.freq()

    #rebuild playingNote and previousPressed
    del previousPressed[:]
    
    for button in buttonsPressed:
        previousPressed.append(button)
    
    #check buttons pressed
    del buttonsPressed[:]
    for pin in row_pins:
        buttonsPressed.append(pin.value())


#when button pressed

while True:
    print("playingNote " + str(playingNote))
    print("buttonsPressed " + str(buttonsPressed))
    print("\n")

    duty+=5000
    #frequency+=1
    led.toggle()
    utime.sleep(.2) #replace with .02 when not debugging
    if rp0.value() or rp1.value() or rp2.value() or rp3.value() or rp4.value() or rp5.value():
        handleButton()
    else:
        spkr.deinit()
        previousPressed = [0,0,0,0,0,0]
        buttonsPressed = [0,0,0,0,0,0]
        playingNote = [0,0,0,0,0,0]


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
    



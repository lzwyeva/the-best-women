def on_button_pressed_a():
    basic.show_string("I love U")
    music.play_melody("C5 A B G A F G E ", 180)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    global num_of_calls
    basic.show_string(receivedString)
    num_of_calls += 1
    basic.show_number(num_of_calls)
radio.on_received_string(on_received_string)

def messages():
    radio.send_string("run away")

def on_button_pressed_b():
    messages()
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play_melody("C C G G A A G F ", 170)
    for index in range(4):
        basic.show_string("!!!!!")
        basic.show_number(88)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_tilt_right():
    for index2 in range(4):
        basic.show_number(88)
        music.play_melody("B A G A G F A C5 ", 200)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def sth():
    for index3 in range(4):
        basic.show_leds("""
            . . # . .
                        . . # . .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . # . .
                        . . . . .
                        . . . . .
        """)
num_of_calls = 0
radio.set_group(200)
num_of_calls = 0
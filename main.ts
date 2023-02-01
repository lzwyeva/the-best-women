input.onButtonPressed(Button.A, function () {
    basic.showString("I love U")
    music.playMelody("C5 A B G A F G E ", 180)
})
radio.onReceivedString(function (receivedString) {
    basic.showString(receivedString)
    num_of_calls += 1
    basic.showNumber(num_of_calls)
    if (num_of_calls >= 3) {
        music.playMelody("C5 F C5 F C5 F C5 F ", 120)
    }
})
function messages () {
    radio.sendString("run away")
}
input.onButtonPressed(Button.B, function () {
    messages()
})
input.onGesture(Gesture.LogoDown, function () {
    music.playMelody("C C G G A A G F ", 170)
})
function sth () {
    for (let index = 0; index < 4; index++) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            `)
    }
}
let num_of_calls = 0
radio.setGroup(218)
num_of_calls = 0

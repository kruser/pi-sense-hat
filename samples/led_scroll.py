from sense_hat import SenseHat
import kruse_hat.led as led

b = [50, 50, 0] # background
f = [0, 255, 0] # foreground

picture = [
    b, b, b, b, b, b, b, b,
    b, b, f, b, b, f, b, b,
    b, b, f, b, b, f, b, b,
    f, b, b, b, b, b, b, f,
    f, b, b, b, b, b, b, f,
    b, f, b, b, b, b, f, b,
    b, b, f, f, f, f, b, b,
    b, b, b, b, b, b, b, b,
]

sense = SenseHat()
sense.rotation = 180
led.scroll_picture(picture, sense=sense, fill=b)

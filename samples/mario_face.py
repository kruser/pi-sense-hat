from sense_hat import SenseHat
import kruse_hat.led as led

hat  = [255, 0, 0]
skin = [232, 219, 104]
hair = [96, 74, 1]
white = [255, 255, 255]

mario = [
    white, hat, hat, hat, hat, hat, white, white,
    hat, hat, hat, hat, hat, hat, hat, hat,
    hair, hair, hair, skin, hair, skin, white, white,
    skin, hair, skin, skin, hair, skin, skin, skin,
    skin, hair, hair, skin, skin, hair, skin, skin,
    hair, skin, skin, skin, hair, hair, hair, hair,
    white, skin, skin, skin, skin, skin, skin, skin,
    hair, hat, hair, hair, hair, white, white, white,
]

sense = SenseHat()
sense.rotation = 180
led.scroll_picture(mario, sense=sense, fill=white)

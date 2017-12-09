from sense_hat import SenseHat
import colors as c

sense = SenseHat()
sense.clear()
sense.set_rotation(180) 

g = c.green

current_x = 4
current_y = 0

sense.set_pixel(current_x, current_y, g)

def move(x_offset, y_offset):
    global current_x
    global current_y
    
    new_x = current_x + x_offset
    if new_x < 0:
        new_x = 0
    elif new_x > 7:
        new_x = 7
    new_y = current_y + y_offset
    if new_y < 0:
        new_y = 0
    elif new_y > 7:
        new_y = 7
    sense.set_pixel(current_x, current_y, c.black)
    sense.set_pixel(new_x, new_y, g)
    current_x = new_x
    current_y = new_y
    
def move_left():
    move(1, 0)
    
def move_right():
    move(-1, 0)
    
def move_up():
    move(0, 1)

def move_down():
    move(0, -1) 

    
sense.stick.direction_left = move_left
sense.stick.direction_right = move_right
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

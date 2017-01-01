from sense_hat import SenseHat
import time

GRID_LENGTH = 8

class ColumnarPicture():
    '''
    turn a list of 64 pixel settings into a two dimensional array padded by two
    empty images on each side
    '''
    columns = [] 

    def __init__(self, picture, fill=[0, 0, 0]):
        '''
        @param {list|tuple} picture - a list of rgb values
        @param {list} fill - in RGB, the fill color used while scrolling. Defaults to black.
        '''

        for index, color in enumerate(picture):
            column_index = index % GRID_LENGTH
            while len(self.columns) <= column_index:
                self.columns.append([])
            self.columns[column_index].append(color)

        fill_column = list(fill for _ in range(GRID_LENGTH))

	# Pad the image on both ends
        for _ in range(GRID_LENGTH):
            self.columns.insert(0, fill_column)
            self.columns.append(fill_column)

    def flatten(self, start_column=0):
        '''
        @param {int} start_column - the column index to start flattening an 8x8 image
        @returns {list}
        '''
        flat_picture = []
        for row in range(GRID_LENGTH):
            for column in range(start_column, start_column + GRID_LENGTH):
                flat_picture.append(self.columns[column][row])

        return flat_picture

def scroll_picture(picture, sense=SenseHat(), fill=[0,0,0]):
    '''
    Scroll a picture across the screen left to right
    @param {list|tuple} picture - a list of rgb values
    @param {SenseHat} sense - optional, a handle on the SenseHat
    @param {list} fill - in RGB, the fill color used while scrolling. Defaults to black.
    '''
    columnar_picture = ColumnarPicture(picture, fill)
    sense.set_pixels(columnar_picture.flatten())

    for column in range(GRID_LENGTH * 2):
        time.sleep(0.25)
        columnar_picture.columns = columnar_picture.columns[1:len(columnar_picture.columns)]
        columnar_picture.columns.append(list(fill for _ in range(GRID_LENGTH)))
        sense.set_pixels(columnar_picture.flatten())


#move_right(): Adds the human's speed to its x position.
#move_left(): Subtracts the human's speed from its x position.
#move_up(): Adds the human's speed to its y position.
#move_down(): Subtracts the human's speed from its y position.
#get_position(): Returns the x position and y position as a tuple.

class Human:
    def __init__(self, pos_x, pos_y, speed):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return (self.__pos_x, self.__pos_y)
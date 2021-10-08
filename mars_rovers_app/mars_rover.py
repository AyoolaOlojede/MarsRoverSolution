
from .direction import Direction

    
class MarsRover:
      
    def __init__(self, x=0, y=0, direction=Direction.N):
        self.x = x
        self.y = y
        self._direction =direction 

    def rotate_left(self):

        if self._direction == Direction.N:
            self._direction = Direction.W
        elif self._direction == Direction.S:
            self._direction = Direction.E
        elif self._direction == Direction.E:
            self._direction = Direction.N
        elif self._direction == Direction.W:
            self._direction = Direction.S


    def rotate_right(self):
        if self._direction == Direction.N:
            self._direction = Direction.E
        elif self._direction == Direction.S:
            self._direction = Direction.W
        elif self._direction == Direction.E:
            self._direction = Direction.S
        elif self._direction == Direction.W:
            self._direction = Direction.N

    def move_in_same_direction(self):
        if self._direction == Direction.N:
            self.y += 1
        elif self._direction == Direction.S:
            self.y-= 1
        elif self._direction == Direction.E:
            self.x += 1
        elif self._direction == Direction.W:
            self.x -= 1

    def move(self, plateau, move):
        if self.x < 0 or self.x > plateau[0] or self.y<0 or self.y > plateau[1]:
            raise Exception('Value not within the plateau range')

        for x in move:
            if x == 'M':
                self.move_in_same_direction()
            elif x == 'L':
                self.rotate_left()
            elif x == 'R':
                self.rotate_right()
            else:
                print('invalid move')


rover1= MarsRover()
rover1.move([5, 5], "LMLMLMLMM")
result ="{} {} {}".format(str(rover1.x),str(rover1.y),rover1._direction.name)
print(result)

# 100 Days of Code: Python
# Snake Game: Snake Class
# Adam Pawlowski (@hypermanganate)

from segment import Segment


class Snake:

    SNAKE_START_SEGMENTS = 4
    SNAKE_SEGMENT_HEIGHT = 20
    SNAKE_SEGMENT_WIDTH = 20
    SNAKE_START_X = 0
    SNAKE_START_Y = 0

    DIR_UP = 1
    DIR_DOWN = 2
    DIR_LEFT = 3
    DIR_RIGHT = 4

    def __init__(self, world_x_length: int, world_y_length: int) -> None:
        super().__init__()
        self.segments = []
        self.world_x_length = world_x_length / 2
        self.world_y_length = world_y_length / 2
        self.food_world_width = self.world_x_length - self.SNAKE_SEGMENT_WIDTH
        self.food_world_height = self.world_y_length - self.SNAKE_SEGMENT_HEIGHT
        self.grow_one = False
        self.reset()

    def add_segment(self, pos_x: int, pos_y: int, color: tuple = None):
        self.segments.append(Segment(pos_x, pos_y, len(self.segments)))

    def set_head(self):
        self.head_segment = self.segments[0]
        self.head_segment.shape("triangle_up")
        self.head_segment.color((0, 255, 255))
        self.head_x = self.segments[0].xcor()
        self.head_y = self.segments[0].ycor()
        self.head_segment.setpos(0 - self.world_x_length, self.world_y_length)
        self.head_segment.pd()
        self.head_segment.goto(self.world_x_length, self.world_y_length)
        self.head_segment.goto(self.world_x_length, 0 - self.world_y_length)
        self.head_segment.goto(0 - self.world_x_length, 0 - self.world_y_length)
        self.head_segment.goto(0 - self.world_x_length, self.world_y_length)
        self.head_segment.pu()
        self.head_segment.setpos(self.head_x, self.head_y)
        self.last_head_x = self.head_x - self.SNAKE_SEGMENT_WIDTH
        self.last_head_y = self.head_y

    def move_head(self, direction: int):

        self.last_head_x = self.head_segment.xcor()
        self.last_head_y = self.head_segment.ycor()

        if direction == self.DIR_RIGHT:
            self.head_segment.shape("triangle_right")
            self.head_segment.setpos(self.last_head_x + self.SNAKE_SEGMENT_WIDTH, self.last_head_y)
        elif direction == self.DIR_LEFT:
            self.head_segment.shape("triangle_left")
            self.head_segment.setpos(self.last_head_x - self.SNAKE_SEGMENT_WIDTH, self.last_head_y)
        elif direction == self.DIR_DOWN:
            self.head_segment.shape("triangle_down")
            self.head_segment.setpos(self.last_head_x, self.last_head_y - self.SNAKE_SEGMENT_HEIGHT)
        else:  # Implied up
            self.head_segment.shape("triangle_up")
            self.head_segment.setpos(self.last_head_x, self.last_head_y + self.SNAKE_SEGMENT_HEIGHT)

        self.head_x = self.head_segment.xcor()
        self.head_y = self.head_segment.ycor()

    def check_collide_snake(self, x_coordinate: int, y_coordinate: int):
        for segment in self.segments:
            if segment.xcor() == x_coordinate and segment.ycor() == y_coordinate:
                return True

        return False

    def check_collide_world(self, x_coordinate: int, y_coordinate: int):
        if self.direction == self.DIR_UP and y_coordinate > self.world_y_length:
            return True
        if self.direction == self.DIR_DOWN and y_coordinate < 0 - self.world_y_length:
            return True
        if self.direction == self.DIR_LEFT and x_coordinate < 0 - self.world_x_length:
            return True
        if self.direction == self.DIR_RIGHT and x_coordinate > self.world_x_length:
            return True

        return False

    def fail_ouroboros(self, x_coordinate: int, y_coordinate: int, direction: int):
        """
        Make sure we don't eat ourself by doubling back.

        I eventually realized I can just make sure I'm not going to land on segment 1,
        but I do not want to re-write this right now.
        """
        if direction >= 3 and x_coordinate == self.last_head_x:
            return True
        elif 0 <= direction <= 2 and y_coordinate == self.last_head_y:
            return True
        else:
            return False

    def get_new_head_pos(self, direction: int):
        """
        Provide new possible coordinates for snake head, for checks.
        """

        if direction == self.DIR_RIGHT:
            return self.head_x + self.SNAKE_SEGMENT_WIDTH, self.head_y
        elif direction == self.DIR_LEFT:
            return self.head_x - self.SNAKE_SEGMENT_WIDTH, self.head_y
        elif direction == self.DIR_DOWN:
            return self.head_x,  self.head_y - self.SNAKE_SEGMENT_HEIGHT
        else:  # Implied up
            return self.head_x,  self.head_y + self.SNAKE_SEGMENT_HEIGHT

    def move_snake(self):

        direction = self.direction

        if self.snake_moving:
            return None

        potential_head_x, potential_head_y = self.get_new_head_pos(direction)

        if self.fail_ouroboros(potential_head_x, potential_head_y, direction):
            return None

        if self.check_collide_snake(potential_head_x, potential_head_y):
            # print("Game Over: Snake has hit itself")
            self.alive = False
            return None

        if self.check_collide_world(potential_head_x, potential_head_y):
            # print("Game Over: Snake has hit the wall.")
            self.alive = False
            return None

        self.snake_moving = True

        self.segments.reverse()

        for segment in self.segments:
            # Starts with the "Tail"

            which_piece = self.segments.index(segment)
            if (self.segments[which_piece] != self.head_segment):
                new_x = self.segments[which_piece + 1].xcor()
                new_y = self.segments[which_piece + 1].ycor()
                segment.next_color()

                segment.setpos(new_x, new_y)

            if which_piece == 0 and self.grow_one:
                self.tail_x_pos = segment.xcor()
                self.tail_y_pos = segment.ycor()

        self.move_head(direction)

        self.segments.reverse()

        if self.grow_one:
            self.add_segment(self.tail_x_pos, self.tail_y_pos)
            self.grow_one = False

        self.draw()

        return True

    def draw(self):
        self.snake_moving = False

    def ate_food(self, food: 'Food'):
        if self.head_segment.distance(food.xcor(), food.ycor()) < 0.8 * self.SNAKE_SEGMENT_WIDTH:
            return True

        return False

    def grow(self):
        self.grow_one = True

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.snake_moving = False
        self.alive = True
        self.direction = 4
        self.segments.clear()

ball = None

def setup():
    global ball
    size(600,600)
    ball = Ball (30, 300, 300, 2)

def draw():
    global ball    
    background(0)
    ball.show()
    ball.move()
    ball.accelerate()

class Ball:
    def __init__(self, raid, x_pos, y_pos, x_vel):
        self.raid = raid
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.x_vel = x_vel
        
    def show (self):
        ellipse (self.x_pos, self.y_pos, self.raid, self.raid)
        
    def move (self):
        self.x_pos = self.x_pos + self.x_vel
        
    def accelerate (self):
        self.x_pos = self.x_pos + 1
from random import randint
apple = Actor("apple")
redball = Actor("red_ball")
score = 0

def draw():
    screen.clear()
    apple.draw()
    redball.draw()
    screen.draw.text("Score: " + str(score), color = "white", topleft = (20,20))

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        score = score + 1
        place_apple()
    else:
        print("You missed!")
        score = 0

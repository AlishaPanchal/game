from random import randint
apple = Actor("apple")
redball = Actor("red_ball")
global score
score = 0

def draw():
    screen.clear()
    screen.fill("light blue")
    apple.draw()
    redball.draw()
    screen.draw.text("Score: " + str(score), color = "white", topleft = (20,20))

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

def place_redball():
    redball.x = randint(10, 800)
    redball.y = randint(10, 600)

place_apple()
place_redball()

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good shot!")
        place_apple()
        place_redball()
    elif redball.collidepoint(pos):
        print("Not a fruit!")
        place_redball()
        place_apple()
    else:
        print("You missed!")

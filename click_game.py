character = Actor('character')
character.topright = 0, 10

WIDTH = 500
HEIGHT = character.height + 20

def draw():
    screen.clear()
    character.draw()

def update():
    character.left = character.left + 2
    if character.left > WIDTH:
        character.right = 0

def on_mouse_down(pos):
    if character.collidepoint(pos):
        set_character_clicked()
    else:
        print("HA........failure.")

def set_character_clicked():
    character.image = "character_clicked"
    sounds.rumble.play()
    print("stop.")
    clock.schedule_unique(set_character_normal, 1.0)

def set_character_normal():
    character.image = "character"

import pgzrun

WIDTH = 1000
HEIGHT = 1000
TITLE = "ask about OOP"
file = "oop.txt"

#boxes
what_is_OOP = Rect(0, 0, 300, 150)
what_can_it_also_be_used_with = Rect(0, 0, 300, 150)
what_is_an_object = Rect(0, 0, 300, 150)
what_does_OOP_stand_for = Rect(0, 0, 300, 150)

#lists n numbers
whats = [what_is_OOP, what_can_it_also_be_used_with, what_is_an_object, what_does_OOP_stand_for]
answers = []
what_count = 0
index_of_file = 0
answer = []
#positions
what_can_it_also_be_used_with.move_ip(20, 270)
what_does_OOP_stand_for.move_ip(370, 270)
what_is_an_object.move_ip(20, 450)
what_is_OOP.move_ip(370, 450)


def draw():
    screen.clear()
    screen.fill("pink")
    for what in whats:
        screen.draw.filled_rect(what, "white")
    indexx = 1
    for what in whats:
        screen.draw.textbox(answer[indexx].strip(), what, color = "pink")
        indexx += 1

def read():
    global what_count

import turtle
import random
def countdown(n) :
    while n > 0:
        print(n)
        n=n-1
        if n ==0:
            print('TIME IS OUT')
            countdown(50)

            
SQUARE_SIZE=20

turtle.penup()


score= 0

#numbers label!
num_label=turtle.Turtle()
num_label.ht()
num_label.penup()
num_label.width('10')
num_label.color('green')
num_label.goto(0,-400)
num_label.write(str (score))

# Now we put different types of trash #

trash_paper= turtle.clone()

trash_plastic= turtle.clone()
trash_glass= turtle.clone()
trash_papercan= turtle.clone()
trash_foodcan= turtle.clone()
trash_plasticcan= turtle.clone()
trash_water = turtle.clone()
trash_plasticcontainer = turtle.clone()
trash_newspaper = turtle.clone()
trash_milk = turtle.clone()
trash_pizza = turtle.clone()
trash_broken_plate = turtle.clone()
trash_banana = turtle.clone()
trash_apple = turtle.clone()
trash_glasscan= turtle.clone()
trash_brokenbottle= turtle.clone()

#trash
turtle.register_shape("paper.gif")
turtle.register_shape("plastic.gif")

turtle.register_shape("water_bottle.gif")
turtle.register_shape("plastic_container.gif")
turtle.register_shape("newspaper.gif")
turtle.register_shape("milk_packag.gif")
turtle.register_shape("pizza.gif")
turtle.register_shape("broken_plate.gif")
turtle.register_shape("broken_bottle.gif")
turtle.register_shape("banana.gif")
turtle.register_shape("apple.gif")

#trash speed
trash_paper.speed(0)

trash_plastic.speed(0)
trash_glass.speed(0)
trash_water.speed(0)
trash_newspaper.speed(0)
trash_milk.speed(0)
trash_pizza.speed(0)
trash_broken_plate.speed(0)
trash_banana.speed(0)
trash_apple.speed(0)
trash_brokenbottle.speed(0)
trash_plasticcontainer.speed(0)

#trash cans
turtle.register_shape("yellow_trash.gif")
turtle.register_shape("blue_trash.gif")
turtle.register_shape("red_trash.gif")
turtle.register_shape("orange_trash.gif")

#final pic
#orange trashcan is for food` yellow trashcan is for plastic` blue trashcan is for glass` red trashcan is for papers
trash_paper.shape("paper.gif")
trash_papercan.shape("red_trash.gif")
trash_plastic.shape("plastic.gif")
trash_plasticcan.shape("yellow_trash.gif")

trash_foodcan.shape("orange_trash.gif")
trash_glasscan.shape("blue_trash.gif")
trash_apple.shape("apple.gif")
trash_banana.shape("banana.gif")
trash_plasticcontainer.shape("plastic_container.gif")
trash_water.shape("water_bottle.gif")
trash_newspaper.shape("newspaper.gif")
trash_milk.shape("milk_packag.gif")
trash_pizza.shape("pizza.gif")
trash_broken_plate.shape("broken_plate.gif")
trash_brokenbottle.shape("broken_bottle.gif")



#drew border
border=turtle.clone()
border.speed(0)
border.ht()
border.color('green')
border.penup()
border.goto(-300,300)
border.pendown()
border.goto(300,300)
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)

#edges
UP_EDGE = 300
DOWN_EDGE=-300
RIGHT_EDGE=300
LEFT_EDGE=-300

#label
label_game=turtle.Turtle()
label_game.ht()
label_game.penup()
label_game.color('green')
label_game.width('12')
label_game.goto(-200,355)
label_game.write('~GREEN TRASH~',font=('serif',30,'normal'))

#notes label
notes_label=turtle.clone()
notes_label.ht()
notes_label.penup()
notes_label.color('black')
notes_label.width('9')
notes_label.goto(-300,-500)
notes_label.write('orange trashcan is for food`    yellow trashcan is for plastic`    blue trashcan is for glass`    red trashcan is for papers` ',font=('arial',15,'normal'))

#pensup
trash_paper.penup()
trash_plastic.penup()
trash_papercan.penup()
trash_foodcan.penup()
trash_plasticcan.penup()

#Trash cans outside
trash_papercan.speed(0)
trash_foodcan.speed(0)
trash_plasticcan.speed(0)
trash_glasscan.speed(0)
trash_papercan.goto(-400,-75)
trash_foodcan.goto(-400,200)
trash_plasticcan.goto(-400,-200)
trash_glasscan.goto(-400,75)
turtle.hideturtle()

cans= [trash_glasscan, trash_papercan, trash_foodcan, trash_plasticcan]


#pop up food randomly
trash_paper.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))

trash_milk.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_apple.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_banana.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_broken_plate.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_plasticcontainer.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_pizza.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_newspaper.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_plastic.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_water.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
trash_brokenbottle.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))

def is_in_range(p, l, u):
    return p >= l and p <= u
m_done=False

n_done=False
pa_done=False
a_done = False
b_done = False
p_done = False
plc_done = False
w_done= False
pl_done=False
bp_done=False
bb_done=False
def banana_go(x, y):

    global b_done
    trash_banana.goto(x, y)
    bx, by = trash_banana.pos()
    fx, fy = trash_foodcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not b_done:
        b_done = True
        trash_banana.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_banana,trash_foodcan)
    




    

def apple_go(x, y):
    global a_done
    trash_apple.goto(x, y)
    bx, by = trash_apple.pos()
    fx, fy = trash_foodcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not a_done:
        a_done = True
        trash_apple.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_apple,trash_foodcan)
        
    
def pizza_go(x, y):
    global p_done
    trash_pizza.goto(x, y)
    bx, by = trash_pizza.pos()
    fx, fy = trash_foodcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not p_done:
        p_done = True
        trash_pizza.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_pizza,trash_foodcan)
        
        
def plasticcontainer_go(x, y):
    global plc_done
    trash_plasticcontainer.goto(x, y)
    bx, by = trash_plasticcontainer.pos()
    fx, fy = trash_plasticcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not plc_done:
        plc_done = True
        trash_plasticcontainer.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_plasticcontainer,trash_plasticcan)
        

def water_go(x, y):
    global w_done
    trash_water.goto(x, y)
    bx, by = trash_water.pos()
    fx, fy = trash_plasticcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not w_done:
        w_done = True
        trash_water.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_water,trash_plasticcan)
        
        
def plastic_go(x, y):
    global pl_done
    trash_plastic.goto(x, y)
    bx, by = trash_plastic.pos()
    fx, fy = trash_plasticcan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not pl_done:
        pl_done = True
        trash_plastic.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_plastic,trash_plasticcan)
        
        
def broken_plate_go(x, y):
    global bp_done
    trash_broken_plate.goto(x, y)
    bx, by = trash_broken_plate.pos()
    fx, fy = trash_glasscan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not bp_done:
        bp_done = True
        trash_broken_plate.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_broken_plate,trash_glasscan)

        
def brokenbottle_go(x, y):
    global bb_done
    trash_brokenbottle.goto(x, y)
    bx, by = trash_brokenbottle.pos()
    fx, fy = trash_glasscan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not bb_done:
        bb_done = True
        trash_brokenbottle.hideturtle()
        score = score +2
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_brokenbottle,trash_glasscan)
        
        
def paper_go(x, y):
    global pa_done
    trash_paper.goto(x, y)
    bx, by = trash_paper.pos()
    fx, fy = trash_papercan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not pa_done:
        pa_done = True
        trash_paper.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_paper,trash_papercan)
    
        
def trash_newspaper_go(x, y):
    global n_done
    trash_newspaper.goto(x, y)
    bx, by = trash_newspaper.pos()
    fx, fy = trash_papercan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not n_done:
        n_done = True
        trash_newspaper.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_newspaper,trash_papercan)
    
        
def trash_milk_go(x, y):
    global m_done
    trash_milk.goto(x, y)
    bx, by = trash_milk.pos()
    fx, fy = trash_papercan.pos()
    global score, num_label
    if is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15) and not m_done:
        m_done = True
        trash_milk.hideturtle()
        score = score +2
        num_label.clear()
        num_label.write(str (score),font=('Arial',40,'normal'))
    else:
        check_right_trash(trash_milk,trash_papercan)
    
    

def check_right_trash(trash, can):
    global cans , score
    for stuff_can in cans:
        bx, by= trash.pos()
        fx, fy = stuff_can.pos()
        if stuff_can != can and is_in_range(bx, fx-15, fx+15) and is_in_range(by, fy-15, fy+15):
            score= score-1
            num_label.clear()
            num_label.write(str(score),font=('Arial',40,'normal'))
            trash.goto(random.randint(LEFT_EDGE,RIGHT_EDGE),random.randint(DOWN_EDGE,UP_EDGE))
           
            

    
##dragging

trash_paper.onrelease(paper_go)
trash_milk.onrelease(trash_milk_go)
trash_apple.onrelease(apple_go)
trash_banana.onrelease(banana_go)
trash_broken_plate.onrelease(broken_plate_go)
trash_plasticcontainer.onrelease(plasticcontainer_go)
trash_pizza.onrelease(pizza_go)
trash_newspaper.onrelease(trash_newspaper_go)
trash_plastic.onrelease(plastic_go)
trash_water.onrelease(water_go)
trash_brokenbottle.onrelease(brokenbottle_go)


#Trash Lists
foodcan= [trash_banana , trash_apple , trash_pizza]
plasticcan= [trash_water, trash_plastic, trash_plasticcontainer]
glasscan = [trash_brokenbottle , trash_broken_plate]
papercan= [trash_newspaper, trash_paper]

#make the trashcans accept the correct trash
##if trash_banana.pos() == trash_foodcan.pos():
##    hideturtle.hide(trash_banana)
#  Now we make the same things but with "or"'s and if statements #
     


turtle.mainloop()








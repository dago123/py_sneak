from tkinter import *
from random import randint

# Origin for this funciton https://www.python-course.eu/tkinter_canvas.php
# checkered draw pattern on canvas
def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


#  GLOBAL Variables
x = 0       # coordinate variable head of snake
y = 0       # coordinate variable of head of snake
r = 10      # variable radious oval of snake
rx = (2*r)    # variable with information about movement direction at X axis/default left
ry = 0*r      # variable with information about movement direction at X axis
offset = r  # offset for x,y coordinate (taking account for radious take some space)
snake_feed = [] # postion oval feed of snake (x0,y0,x1,y1), when head of snake cover this point then snake will grow up
feed_id = []    # ID of snake_feed oval needed during deleting operation
result = ""     # this label story inforamtion about game status
canvas_width = 200  # canvas X
canvas_height = 200 # canvas Y
score = 0



# feed_snake_generator() generate x,y comlete even coordination in range <0,18>
def feed_snake_generator():

    xy=[]

    for i in range(2):
        temp = randint(0, 18)
        if temp % 2 == 0:   #if even check
            temp = temp * 10
        else:
            temp = (temp - 1) * 10
        #print(":", temp)
        xy.append(temp)
    return xy

# move_oval_cords() provide logic for snake game move,feed,end game etc
def move_oval_cords(circle, owal_position, body):
    def next_step():
        global x
        global y
        global rx
        global ry
        global snake_feed
        temp_feed = []
        global feed_id
        global score
        snake_feedxy = []

        # left/right movement
        if x == 180 and rx== 20:
            x = 0
        elif x == 0 and rx == -20:
            x = 180
        else:
            x += rx

        #up down movement
        if y == 180 and ry == 20:
            y = 0
        elif y == 0 and ry == -20:
            y = 180
        else:
            y += ry

        if not snake_feed:  #check is feed for snake exist on a canvas?
            temp = feed_snake_generator()     #if not exist generate new xy coordinate
            snake_feed.append([temp[0] - r+ offset, temp[1] - r+ offset, temp[0] + r+ offset , temp[1] + r + offset])   # transform into oval coordinate
            #print(temp_feed)   #for debbug process
            feed_id = body.create_oval(snake_feed[0], width=0, fill='yellow')   # draw oval in xy coordinate

        next_head_xy = [x - r + offset, y - r + offset, x + r + offset, y + r + offset] #head posstion in next step

        for temp_owal, temp_position in zip(circle, owal_position):
            if temp_position == next_head_xy:   #if head meet tail then game is over
                print("END OVER")
                result.set("GAME OVER Result: %d" %score)
                rx = 0  # stop snake
                ry = 0  # stop snake
                body.itemconfig(temp_owal, fill = "RED")    #show where collsion take place
                return

        if next_head_xy == snake_feed[0]:   #enlargement of the snake
            print("grow UP!")
            owal_position.append(snake_feed[0])
            circle.append(body.create_oval(temp_list, width=0, fill='green'))
            score +=1
            result.set("Result: %d" %score)
            body.delete(feed_id)    #delete feed oval
            snake_feed.pop()        #delete feed cooridnate



        owal_position.pop(0)            #movement of oval, remove first tail coordinate
        owal_position.append(next_head_xy)  #movement of oval, add next step coordinate

        for temp_owal, temp_position in zip(circle, owal_position):
            body.coords(temp_owal, temp_position)   #redraw snake with new coordinates for next step

        body.after(200,next_step)   #loop to next_step after 200ms

    next_step()

# canvas control event functions
def leftKey(event):
    global rx,    ry

    print ("left")
    rx = -20
    ry = 0

def rightKey(event):
    global rx, ry
    print("right")
    rx = 20
    ry = 0

def upKey(event):
    global rx, ry
    print("up")
    rx = 0
    ry = -20

def downKey(event):
    global rx, ry
    print("down")
    rx = 0
    ry = 20

master = Tk()
master.title("pySnake v1.0")


body = Canvas(master,width=canvas_width,height=canvas_height)
body.grid(row=21, column=0, padx=10, pady=2)

body.bind('<Left>', leftKey)
body.bind('<Right>', rightKey)
body.bind('<Up>', upKey)
body.bind('<Down>', downKey)
body.focus_set()

circle = []
owal_position = []
result = StringVar()
result.set("Result: %d" %score)

checkered(body,20)

temp_list = [x - r + offset, y - r + offset, x + r + offset, y + r + offset]
owal_position.append(temp_list)
circle.append(body.create_oval(temp_list, width=0, fill='green'))

move_oval_cords(circle,owal_position, body)

upper_frame = Canvas(master,width= canvas_width,height=canvas_height/10)
upper_frame.grid(row=0, column=0, padx=10, pady=2)

Label(upper_frame,text = "Sneak v1.0").grid(row=0, column=0, padx=10, pady=2)
Label(upper_frame,textvariable = result).grid(row=1, column=0, padx=10, pady=2)




mainloop()
from tkinter import *

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" pixel
   for x in range(line_distance,canvas_width,line_distance):
      canvas.create_line(x, 0, x, canvas_height, fill="#476042")
   # horizontal lines at an interval of "line_distance" pixel
   for y in range(line_distance,canvas_height,line_distance):
      canvas.create_line(0, y, canvas_width, y, fill="#476042")


x = 0
y = 0
rx = -20
ry = 0
r = 10
offset = 10


coordinate = [0,0,20,20] #x0,y0, x1,y1


def move_oval_cords(circle, owal_position, body):
    def next_step():
        global x
        global y
        global rx
        global ry


        if x == 180 and rx== 20:
            x = 0
        elif x == 0 and rx == -20:
            x = 180
        else:
            x += rx


        #up down
        if y == 180 and ry == 20:
            y = 0
        elif y == 0 and ry == -20:
            y = 180
        else:
            y += ry


        #for temporary in range(len(owal_position)-1):
        #    owal_position[temporary+1] = owal_position[temporary].copy()
        temp = [x - r + offset, y - r + offset, x + r + offset, y + r + offset]

        for temp_owal, temp_position in zip(circle, owal_position):
            if temp_position == temp:
                print("END OVER")
                rx=0
                ry=0
                body.itemconfig(temp_owal, fill = "RED")
                return

        owal_position.pop(0)
        owal_position.append(temp)

        for temp_owal, temp_position in zip(circle,owal_position):
            body.coords(temp_owal, temp_position)

        #body.move(circle, rx, ry)
    #    body.coords(circle, owal_position)

        #body.after(1000,next_step())
        body.after(200,next_step)

    next_step()


def leftKey(event):
    global rx,    ry

    print ("lewo")
    rx = -20
    ry = 0

def rightKey(event):
    global rx, ry
    print("prawo")
    rx = 20
    ry = 0

def upKey(event):
    global rx, ry
    print("góra")
    ry = -20
    rx = 0
def downKey(event):
    global rx, ry
    print("dół")
    ry = 20
    rx = 0

master = Tk()
canvas_width = 200
canvas_height = 200

body = Canvas(master,width=canvas_width,height=canvas_height)
body.grid(row=21, column=0, padx=10, pady=2)

body.bind('<Left>', leftKey)
body.bind('<Right>', rightKey)
body.bind('<Up>', upKey)
body.bind('<Down>', downKey)
body.focus_set()

#rect = Canvas(master, width=20, height=20, bg='green').grid(row=21, column=0, padx=10, pady=2)
circle = []
owal_position = []

for temp in range(160, 0, -20):
    temp_list = [x - r + offset+temp, y - r + offset, x + r + offset+temp, y + r + offset]
    owal_position.append(temp_list)
    circle.append(body.create_oval(temp_list, width=0, fill='green'))

move_oval_cords(circle,owal_position, body)

upper_frame = Canvas(master,width= canvas_width,height=canvas_height/10)
upper_frame.grid(row=0, column=0, padx=10, pady=2)

Label(upper_frame,text = "Sneak v0.0").grid(row=0, column=0, padx=10, pady=2)



checkered(body,20)

mainloop()
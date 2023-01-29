import tkinter
import time
import random
import array
import logging
import threading

PYTHONUNBUFFERED="yes"

TK_SILENCE_DEPRECATION=1

Window_Width=700
Window_Height=500
line_width = Window_Width - 20



rect_min_movement = 5
Refresh_Sec = .00001
Refresh_Sec2 =.001
rectx1 = 10

rectx2 = rectx1 + 10

basey = 470


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("tk")
    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


 

def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="white")
    canvas.pack(fill="both", expand=True)
    canvas.create_line(8,basey,Window_Width - 10,470) 
                    
    return canvas
 
def animate_rect(Window, canvas,xmove):
    
   
    #creating an empty array list 
    yval = []
    despos = []
    #implemented a incremental counter, while Inc_bar is less than Max_bar columns will continue to generate
    Inc_bar = 0
    # Change Max_bar to change the max number of columns being made
    Max_bar = 100
    
    
    colnum = 97
    #colwidth = 5
    colwidth = round(((Window_Width - 18) / colnum)-2)
    colbetween = colwidth + 2
    
    x1pos = 10
    despos.append(x1pos)
    xstart = 10
    for i in range(0,colnum):
        
        color = "#%03x" % random.randint(0, 0xFFF)
        x2pos= x1pos + colwidth
        y2pos = random.randint(10,450)
        rect = canvas.create_rectangle(xstart-(colbetween * 3),basey,xstart-(colbetween * 3)+colwidth, y2pos, fill = color, outline = "")
        x1pos += colbetween
        val = basey - y2pos
        yval.append(val)
        despos.append(x1pos)
        print (len(yval), len(despos))
        if i == 0:
            Inc_bar = 10
        else:
            Inc_bar += colbetween
        while True:
            canvas.move(rect,1,0)
            Window.update()
            time.sleep(Refresh_Sec)
            rect_pos = canvas.coords(rect)
            # unpack array to variables
            x1,y1,x2,y2 = rect_pos
            z = x1 + 1
            
            if x1 >= z:
                rect = canvas.create_rectangle(x1,y1,x2, y2, fill = color)
                canvas.coords(rect, x1,basey,x2, y2pos)
                canvas.update()
                v +=1 
            elif z == Inc_bar:
                l = tkinter.Label(canvas, text = val, font =("Courier", 8))
                l.place(x = x1, y = y1)
                xstart += colbetween 
                break
                
        
    print(yval)
    
        
    time.sleep(5)
Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_rect(Animation_Window,Animation_canvas, rect_min_movement)

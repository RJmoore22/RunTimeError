import tkinter
import time
import random
import array
import logging
import threading
import sys

PYTHONUNBUFFERED="yes"

TK_SILENCE_DEPRECATION=1

Window_Width=830
Window_Height=670
line_width = Window_Width - 20
rect_min_movement = 5
Refresh_Sec = .000001
Refresh_Sec2 =.000001
rectx1 = 10
rectx2 = rectx1 + 10
basey = 590

#creating an empty array list 
yval = []
despos = []
names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ]
errorCounter = 0
objects = []

colnum = 102

colwidth = round(((Window_Width - 18) / colnum)-2)
colbetween = colwidth + 2
def animate_rect():
    
    objects.clear()
    yval.clear()
    canvas.delete('all')
    canvas.create_line(8,basey,Window_Width - 10,basey,fill = "white") 
    #implemented a incremental counter, while Inc_bar is less than Max_bar columns will continue to generate
    Inc_bar = 0
    # Change Max_bar to change the max number of columns being made
    Max_bar = 100
    x1pos = 10
    despos.append(x1pos)
    xstart = 10
    
    for i in range(0,colnum):
        delay = 1
        color = "#%03x" % random.randint(0, 0xFFF)
        color2 = "#386e6b"
        #x2pos= x1pos + colwidth
        y2pos = random.randint(10,570)
        rect = canvas.create_rectangle(xstart-(colbetween * delay),basey,xstart-(colbetween * delay)+colwidth, y2pos, fill = color2, outline = "")
        objects.append(rect)
        
        x1pos += colbetween
        val = basey - y2pos
        yval.append(val)
        
        #print (len(yval), len(despos))
        if i == 0:
            Inc_bar = 10
        else:
            Inc_bar += colbetween
        while True:
            
            canvas.move(rect,1,0)
            canvas.update()
            time.sleep(Refresh_Sec)
            rect_pos = canvas.coords(rect)
            
            # unpack array to variables
            x1,y1,x2,y2 = rect_pos
            despos.append(x1)
            z = x1 
            if z == Inc_bar:
                xstart += colbetween 
                
                break
        
    canvas.config(min(str(objects)),fill = 'red')
    canvas.config(max(str(objects)),fill = 'red')
    print (objects)
    print (len(objects))
    print (yval)
    print (len(yval))
                    
    #print(yval)
    #print(objects)
    #print(despos)

     
def bubbleSort(yval): 
    tic = time.perf_counter()   
    n = len(yval)  
    
    # Traverse through all array elements
    for i in range(0,n-1):
 
        # Last i elements are already in place
        for j in range(n-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if yval[j] > yval[j + 1]:
                yval[j], yval[j+1] = yval[j+1], yval[j]
                while True:
                    canvas.move(objects[j],colbetween, 0)
                    canvas.move(objects[j+1],-colbetween, 0)
                    canvas.update()
                    objects[j], objects[j+1] = objects[j+1], objects[j]
                    break
    toc = time.perf_counter()

    canvas.create_text(Window_Width / 2, 20, text=f"{toc-tic:0.3f} seconds ", fill = "white")




Window = tkinter.Tk()
Window.title("tk")
#Window.geometry(f'{Window_Width}x{Window_Height}')
Window.lift()
Window.attributes("-topmost", True)



    
UI_frame = tkinter.Frame(Window, background = 'black')
UI_frame.grid(row=0, column=0)

#animation canvas config
canvas = tkinter.Canvas(UI_frame)
canvas.configure(bg="black",width=Window_Width, height=600)
canvas.pack(fill="both", expand=True)


btn = tkinter.Button(UI_frame, text = 'Create', bd = '5',
                          command = animate_rect)
btn.pack(side = 'left')

btn = tkinter.Button(UI_frame, text = 'Sort', bd = '5',
                          command =lambda: bubbleSort(yval))

btn.pack(side = 'right')



Window.mainloop()



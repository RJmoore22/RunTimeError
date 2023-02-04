import tkinter
import time
import random
import array
import logging
import threading
import sys

PYTHONUNBUFFERED="yes"

TK_SILENCE_DEPRECATION=1

Window_Width=770
Window_Height=600
line_width = Window_Width - 20



rect_min_movement = 5
Refresh_Sec = .000001
Refresh_Sec2 =.000001
rectx1 = 10

rectx2 = rectx1 + 10

basey = 470

#creating an empty array list 
yval = []
despos = []
names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ]
                    

 
def animate_rect():
    canvas.delete('all')
    canvas.create_line(8,basey,Window_Width - 10,470) 
   
    
    #implemented a incremental counter, while Inc_bar is less than Max_bar columns will continue to generate
    Inc_bar = 0
    # Change Max_bar to change the max number of columns being made
    Max_bar = 100
    
    
    colnum = 10

    #colwidth = 5
    colwidth = round(((Window_Width - 18) / colnum)-2)
    colbetween = colwidth + 2
    
    x1pos = 10
    despos.append(x1pos)
    xstart = 10

                

    for i in range(0,colnum):
        v = 0
        delay = 4
        color = "#%03x" % random.randint(0, 0xFFF)
        color2 = "#386e6b"
        x2pos= x1pos + colwidth
        y2pos = random.randint(10,450)
        rect = canvas.create_rectangle(xstart-(colbetween * delay),basey,xstart-(colbetween * delay)+colwidth, y2pos, fill = color2, outline = "")
        x1pos += colbetween
        val = basey - y2pos
        yval.append(val)
        despos.append(x1pos)
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
            z = x1 + 1
            
            if x1 >= z:
                names[i]  = canvas.create_rectangle(x1,y1,x2, y2, fill = color)
                
                v += 1 
                canvas.coords(rect, x1,basey,x2, y2pos)
                canvas.update()
                 
                
            elif z == Inc_bar:
                canvas.create_text((x1 + 4, y1 - 4), text=val,font = "MSGothic 6 bold")
                
                xstart += colbetween 
                
                break
                  
    print(yval)
    #print(despos)

     
def bubbleSort(yval):
    n = len(yval)
 
    # Traverse through all array elements
    for i in range(n-1):
 
        # Last i elements are already in place
        for j in range(i+1, n):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if yval[i] > yval[j]:
                yval[i], yval[j] = yval[j], yval[i]    

    print(yval)

Window = tkinter.Tk()
Window.title("tk")
Window.geometry(f'{Window_Width}x{Window_Height}')
    
UI_frame = tkinter.Frame(Window, width= 3000, height=500)
UI_frame.grid(row=0, column=0, padx=0)

    
canvas = tkinter.Canvas(UI_frame)
canvas.configure(bg="white",width=Window_Width, height=500)
canvas.pack(fill="both", expand=True)
#canvas.create_line(8,basey,Window_Width - 10,470) 

btn = tkinter.Button(UI_frame, text = 'Create', bd = '5',
                          command = animate_rect)

btn.pack(side= 'left' )

btn = tkinter.Button(UI_frame, text = 'Sort', bd = '5',
                          command =lambda: bubbleSort(yval))

btn.pack(side= 'right' )


Window.mainloop()



import tkinter
import time
import random
import array



TK_SILENCE_DEPRECATION=1

Window_Width=1000
Window_Height=500
rect_min_movement = 5
Refresh_Sec = 0.005
rectx1 = Window_Width/2
recty1 = 355
rectx2 = rectx1 + 10
recty2 = random.randint(10,330)


def create_animation_window():
    Window = tkinter.Tk()
    Window.title("tk")
    Window.geometry(f'{Window_Width}x{Window_Height}')
    return Window


 

def create_animation_canvas(Window):
    canvas = tkinter.Canvas(Window)
    canvas.configure(bg="white")
    canvas.pack(fill="both", expand=True)
    canvas.create_line(10,355,1000,355) 
                    
    return canvas
 
def animate_rect(Window, canvas,xmove):
    rect = canvas.create_rectangle(rectx1,recty1,rectx2, recty2, fill = 'blue', outline = 'black')
   
    #creating an empty array list 
    arr = []
   
    #implemented a incremental counter, while Inc_bar is less than Max_bar columns will continue to generate
    Inc_bar = 0
    # Change Max_bar to change the max number of columns being made
    Max_bar = 5
    while Inc_bar < Max_bar:
        canvas.move(rect,xmove,0)
        Window.update()
        time.sleep(Refresh_Sec)
        rect_pos = canvas.coords(rect)
        # unpack array to variables
        x1,y1,x2,y2 = rect_pos
        
        
        if x1 < abs(xmove) or  x2 > Window_Width-abs(xmove):
            #Inc_bar will increment by 1 when column touches the window edge
            Inc_bar += 1
            xmove = -xmove 
            var = random.randint(10,350)
            
            #appends the random number being generated with var and append them to the empty array list arr
            arr.append(var)
            canvas.coords(rect, Window_Width / 2, 355, (Window_Width / 2) +10, var)
           
            l = tkinter.Label(canvas, text = var, font =("Courier", 10))
            l.pack()
            
            canvas.update()

        
#print array list after program runs
    print(arr)        


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_rect(Animation_Window,Animation_canvas, rect_min_movement)

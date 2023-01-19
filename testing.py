import tkinter
import time
import random
TK_SILENCE_DEPRECATION=1

Window_Width=600
Window_Height=400
rect_min_movement = 5
Refresh_Sec = 0.001
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
    canvas.create_line(10,355,590,355) 
                    
    return canvas
 
def animate_rect(Window, canvas,xmove):
    rect = canvas.create_rectangle(rectx1,recty1,rectx2, recty2, fill = 'blue', outline = 'black')
    while True:
        canvas.move(rect,xmove,0)
        Window.update()
        time.sleep(Refresh_Sec)
        rect_pos = canvas.coords(rect)
        # unpack array to variables
        x1,y1,x2,y2 = rect_pos
        
        if x1 < abs(xmove) or  x2 > Window_Width-abs(xmove):
            
            xmove = -xmove 
            var = random.randint(10,350)
            canvas.coords(rect, Window_Width / 2, 355, (Window_Width / 2) +10, var)
           
            l = tkinter.Label(canvas, text = var, font =("Courier", 10))
            l.pack()
            
            canvas.update()
        
        


Animation_Window = create_animation_window()
Animation_canvas = create_animation_canvas(Animation_Window)
animate_rect(Animation_Window,Animation_canvas, rect_min_movement)


 
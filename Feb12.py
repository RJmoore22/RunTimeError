import tkinter
import time
import random
import tracemalloc
PYTHONUNBUFFERED="yes"

TK_SILENCE_DEPRECATION=1

Window_Width=1600
Window_Height=800
line_width = Window_Width - 20
rect_min_movement = 5
Refresh_Sec = .000001
Refresh_Sec2 =.000001
rectx1 = 10
rectx2 = rectx1 + 10
basey = Window_Height - 10

#creating an empty array list 
yval = []
despos = []
names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ]
errorCounter = 0
objects = []

colnum = 500

colwidth = round(((Window_Width - 18) / colnum)-2)
colbetween = colwidth + 2

#timex = 0 for fast or 1 for slow 

def fast():
    global timex
    timex = 0
    bubbleSort(yval)

def cool():
    global timex
    timex = 1
    bubbleSort(yval)

color2 = "#386e6b"
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
        y2pos = random.randint(10,basey - 10)
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
            #canvas.config(objects[i], fill = 'red')
            canvas.move(rect,colbetween,0)
            #canvas.update()
            #time.sleep(Refresh_Sec)
            rect_pos = canvas.coords(rect)
            # unpack array to variables
            x1,y1,x2,y2 = rect_pos
            despos.append(x1)
            z = x1 
            if z == Inc_bar:
                xstart += colbetween 
                break
    lowest = yval.index(min(yval))
    highest = yval.index(max(yval))
    canvas.itemconfig(objects[lowest],fill = 'red')
    canvas.itemconfig(objects[highest],fill = 'red')
    canvas.update()

     
def bubbleSort(yval): 
    tracemalloc.start()
    tic = time.perf_counter()   
    n = len(yval)  
    
    # Traverse through all array elements
    for i in range(0,n-1):
        if timex == 1:
            canvas.update()
        # Last i elements are already in place
        for j in range(n-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if yval[j] > yval[j + 1]:
                yval[j], yval[j+1] = yval[j+1], yval[j]
                
                    
                canvas.move(objects[j],colbetween, 0)
                canvas.move(objects[j+1],-colbetween, 0)
                objects[j], objects[j+1] = objects[j+1], objects[j]
                    

    toc = time.perf_counter()
    canvas.create_text(Window_Width / 2, 40, text=f"Traced Memory (Current, Peak): {tracemalloc.get_traced_memory()} bytes ", fill = "white")
    canvas.create_text(Window_Width / 2, 20, text=f"{toc-tic:0.3f} seconds ", fill = "white")
    tracemalloc.stop()

def insertionSort(yval):
    tracemalloc.start()
    st = time.perf_counter()
    n = len(yval)

    for i in range(1, n):
        k = yval[i]
        j = i - 1
        canvas.update()
        while j >= 0 and k < yval[j]:
            yval[j + 1] = yval[j]
            canvas.move(objects[j],colbetween, 0)
            canvas.move(objects[j+1],-colbetween, 0)
            objects[j], objects[j+1] = objects[j+1], objects[j]
            j -= 1
        yval[j + 1] = k
        
    #print(yval)
    et = time.perf_counter()
    canvas.create_text(Window_Width / 2, 40, text=f"Traced Memory (Current, Peak): {tracemalloc.get_traced_memory()} bytes ", fill = "white")
    canvas.create_text(Window_Width / 2, 20, text=f"{et-st:0.3f} seconds ", fill = "white")
    tracemalloc.stop()

def mergeSort(yval):
    if len(yval) > 1:
 
         # Finding the mid of the array
        mid = len(yval)//2
 
        # Dividing the array elements
        L = yval[:mid]
 
        # into 2 halves
        R = yval[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                yval[k] = L[i]
                i += 1
            else:
                yval[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            yval[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            yval[k] = R[j]
            j += 1
            k += 1
    print(yval)

Window = tkinter.Tk()
Window.title("tk")
#Window.geometry(f'{Window_Width}x{Window_Height}')
Window.lift()
Window.attributes("-topmost", True)



    
UI_frame = tkinter.Frame(Window, background = 'black', border = 30)
UI_frame.grid(row=0, column=0, padx = 0, pady = 0)

#animation canvas config
canvas = tkinter.Canvas(UI_frame)
canvas.configure(bg="black",width=Window_Width, height=Window_Height)
canvas.pack(fill="both", expand=True)


# btn = tkinter.Button(UI_frame, text = 'Create',bd = 5,command = animate_rect)
# btn.pack(side = 'left')

# btn = tkinter.Button(UI_frame, text = 'Cool Sort',bd = 5,command =lambda: cool())
# btn.pack(side = 'right')

# btn = tkinter.Button(UI_frame, text = 'Fast Sort',bd = 5,command =lambda: fast())
# btn.pack(side = 'right')

# btn = tkinter.Button(UI_frame, text = 'IN Sort',bd = 5,command =lambda: insertionSort(yval))
# btn.pack(side = 'right')

# btn = tkinter.Button(UI_frame, text = 'M Sort',bd = 5,command =lambda: mergeSort(yval))
# btn.pack(side = 'right')

def selected ():
    if clicked.get() == 'Create':
        animate_rect()
    if clicked.get() == 'Cool':
        cool()
    if clicked.get() == 'Fast':
        fast()
    if clicked.get() == 'Insertion':
        insertionSort(yval)

options = [
    "Create" , 
    "Cool" , 
    "Fast", 
    "Insertion", 
    "Merge",
]

clicked  = tkinter.StringVar()
clicked.set(options[0])

btn = tkinter.OptionMenu(UI_frame, clicked ,*options)
btn.pack(side='left')

btn = tkinter.Button(UI_frame, text = 'Selected',bd = 5,command = selected)
btn.pack(side = 'left')

Window.mainloop()


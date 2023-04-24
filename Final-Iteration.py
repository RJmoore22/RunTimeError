import tkinter
import time
import random
import tracemalloc
import csv
from tkinter import simpledialog


PYTHONUNBUFFERED="yes"

TK_SILENCE_DEPRECATION=1

root=tkinter.Tk()
 
# setting the windows size
root.geometry("600x400")
  
# declaring string variable
# for storing name and password
name_var=simpledialog.askinteger("Input", "Column Number")
 
# performing an infinite loop
# for the window to display


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

totalTIME = 0
colnum = name_var

colwidth = round(((Window_Width - 18) / colnum)-2)
colbetween = colwidth + 2
color2 = "#386e6b"

def shuff_col():
    
    objects.clear()
    yval.clear()
    canvas.delete('all')
    despos.clear()
    canvas.create_line(8,basey,Window_Width - 10,basey,fill = "white") 
    #implemented a incremental counter, while Inc_bar is less than Max_bar columns will continue to generate
    Inc_bar = 0
    # Change Max_bar to change the max number of columns being made
    Max_bar = 100
    x1pos = 10
    xstart = 10
    
    for i in range(0,colnum):
        delay = 1
        color = "#%03x" % random.randint(0, 0xFFF)
        color2 = "#386e6b"
        y2pos = random.randint(10,basey - 10)
        rect = canvas.create_rectangle(xstart-(colbetween * delay),basey,xstart-(colbetween * delay)+colwidth, y2pos, fill = color2, outline = "")
        objects.append(rect)
        
        x1pos += colbetween
        val = basey - y2pos
        yval.append(val)
        

        if i == 0:
            Inc_bar = 10
        else:
            Inc_bar += colbetween
        while True:
            canvas.move(rect,colbetween,0)
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

#timex = 0 for fast or 1 for slow 
def fast():
    global timex
    timex = 0
    bubbleSort(yval)

def Bubble():
    global timex
    timex = 1
    bubbleSort(yval)

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
    canvas.create_text(Window_Width / 2, 40, text=f"Traced Memory (Current, Peak): {tracemalloc.get_traced_memory()} bytes ", fill = "black")
    canvas.create_text(Window_Width / 2, 20, text=f"{toc-tic:0.3f} seconds ", fill = "black")
    tracemalloc.stop()
    export("Bubble Sort",toc-tic,colnum)




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
    canvas.create_text(Window_Width / 2, 40, text=f"Traced Memory (Current, Peak): {tracemalloc.get_traced_memory()} bytes ", fill = "black")
    canvas.create_text(Window_Width / 2, 20, text=f"{et-st:0.3f} seconds ", fill = "black")
    tracemalloc.stop()
    export("Insertion Sort",et-st,colnum)
total = []


def mergeSort(yval,despos,objects):
    
    #tic = time.perf_counter()   
    #start_time = time.time()
    if len(yval) > 1:
         # Finding the mid of the array
        mid = len(yval)//2
        # Dividing the array elements
        L = yval[:mid]
        L2 = despos[:mid]
        L3 = objects[:mid]
        # into 2 halves
        R = yval[mid:]
        R2 = despos[mid:]
        R3 = objects[mid:]
        # Sorting the first half
        mergeSort(L,L2,L3)
        # Sorting the second half
        mergeSort(R,R2,R3)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] >= R[j]: 
                yval[k] = L[i]
                objects[k] = L3[i]
                canvas.delete(objects[k])    
                objects[k] = canvas.create_rectangle(despos[k],basey,despos[k] + colwidth, yval[k], fill = color2, outline = "")
                
                i += 1
            else:
                yval[k] = R[j]
                objects[k] = R3[j]
                canvas.delete(objects[k])
                objects[k] = canvas.create_rectangle(despos[k],basey,despos[k] + colwidth, yval[k], fill = color2, outline = "")
                
                j += 1
            k += 1
            canvas.update()
        # Checking if any element was left
        while i < len(L):
            yval[k] = L[i]
            objects[k] = L3[i]
            canvas.delete(objects[k])
            objects[k] = canvas.create_rectangle(despos[k],basey,despos[k] + colwidth, yval[k], fill = color2, outline = "")
            
            i += 1
            k += 1
 
        while j < len(R):
            yval[k] = R[j]
            objects[k] = R3[j]
            canvas.delete(objects[k])    
            objects[k] = canvas.create_rectangle(despos[k],basey,despos[k] + colwidth, yval[k], fill = color2, outline = "")
            j += 1
            k += 1

    
    
      

def partition(yval, start, end):
  
    pivot = yval[end]
    canvas.itemconfig(objects[end], fill = "green")
    
    i = start -1

    for j in range(start, end):
        if yval[j] <= pivot:
            
            i = i + 1
            yval[i], yval[j] = yval[j], yval[i]
            
            canvas.move(objects[i],colbetween * (j - i), 0)
            canvas.move(objects[j],-colbetween * (j - i), 0)
            objects[i], objects[j] = objects[j], objects[i]
            canvas.update()
            
    
    canvas.itemconfig(objects[end], fill = color2)
    
    yval[i + 1], yval[end] = yval[end], yval[i + 1]
    canvas.move(objects[i+1],colbetween * (end - (i+1)), 0)
    canvas.move(objects[end],-colbetween * (end - (i+1)), 0)
    objects[i+1], objects[end] = objects[end], objects[i+1]
    canvas.update()
    return i + 1
    
    

def quickSort(yval, start, end):
    
    if start < end:

        pi = partition(yval, start, end)

        quickSort(yval, start, pi - 1)
    
        quickSort(yval, pi + 1, end)
    
       

def timesort():
    stime = time.perf_counter()
    quickSort(yval, 0, len(yval) - 1)
    etime = time.perf_counter()
    export("Quick Sort",etime-stime,colnum)
    canvas.create_text(Window_Width / 2, 20, text=f"{etime-stime:0.3f} seconds ", fill = "black")


def cocktailSort(yval):
    starttime = time.perf_counter()
    n = len(yval)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):
 
        # reset the swapped flag on entering the loop,
        # because it might be true from a previous
        # iteration.
        swapped = False
 
        # loop from left to right same as the bubble
        # sort
        for i in range (start, end):
            if (yval[i] > yval[i+1]) :
                yval[i], yval[i+1]= yval[i+1], yval[i]
                canvas.move(objects[i],colbetween, 0)
                canvas.move(objects[i+1],-colbetween, 0)
                objects[i], objects[i+1] = objects[i+1], objects[i]
                swapped=True
        canvas.update()
 
        # if nothing moved, then array is sorted.
        if (swapped==False):
            break
 
        # otherwise, reset the swapped flag so that it
        # can be used in the next stage
        swapped = False
 
        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end-1
 
        # from right to left, doing the same
        # comparison as in the previous stage
        for i in range(end-1, start-1,-1):
            if (yval[i] > yval[i+1]):
                yval[i], yval[i+1] = yval[i+1], yval[i]
                canvas.move(objects[i],colbetween, 0)
                canvas.move(objects[i+1],-colbetween, 0)
                objects[i], objects[i+1] = objects[i+1], objects[i]
                swapped = True
        canvas.update()
 
        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        start = start+1
    endtime = time.perf_counter()
    export("Cocktail Sort",endtime-starttime,colnum)
    canvas.create_text(Window_Width / 2, 20, text=f"{endtime-starttime:0.3f} seconds ", fill = "black")
        


def shellSort(yval):
 
    # Start with a big gap, then reduce the gap
    n = float(len(yval))
    gap = float(n/2)
 
    # Do a gapped insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gapped
    # order keep adding one more element until the entire array
    # is gap sorted
    while gap > 0:
 
        for i in range(int(gap),int(n)):
 
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = yval[i]
            temp2 = objects[i]
 
            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while  j >= gap and yval[int(j)-int(gap)] >temp:
                yval[int(j)], yval[int(j)-int(gap)] = yval[int(j)-int(gap)], yval[int(j)]
                canvas.move(objects[int(j)],colbetween * (-gap), 0)
                canvas.move(objects[int(j)-int(gap)],colbetween * gap, 0)
                objects[int(j)], objects[int(j)-int(gap)]= objects[int(j)-int(gap)], objects[int(j)]
                canvas.update()
                j -= gap
 
            # put temp (the original a[i]) in its correct location
            yval[int(j)] = temp
            objects[int(j)] = temp2
            #canvas.move(objects[int(j)-int(gap)],colbetween, 0)
            #canvas.update()
        gap /= 2


def timefunc():
    stime = time.perf_counter()
    mergeSort(yval,despos,objects)
    etime = time.perf_counter()
    export("Merge Sort",etime-stime,colnum)
    canvas.create_text(Window_Width / 2, 20, text=f"{etime-stime:0.3f} seconds ", fill = "black")

def export(sort_name, time_of_sort, colnum):
    from csv import DictWriter
 
    # list of column names
    field_names = ['Sorting Alg', 'Time', 'Num of Col']
    
    # Dictionary that we want to add as a new row
    dict = {'Sorting Alg': sort_name, 'Time': time_of_sort ,'Num of Col': colnum}
    
    # Open CSV file in append mode
    # Create a file object for this file
    with open(r'sorting_data.csv', 'a') as f_object:
    
        # Pass the file object and a list
        # of column names to DictWriter()
        # You will get a object of DictWriter
        dictwriter_object = DictWriter(f_object, fieldnames=field_names)
    
        # Pass the dictionary as an argument to the Writerow()
        dictwriter_object.writerow(dict)
    
        # Close the file object
        f_object.close()


Window = tkinter.Tk()
Window.title("tk")
#Window.geometry(f'{Window_Width}x{Window_Height}')
Window.lift()
Window.attributes("-topmost", True)



    
UI_frame = tkinter.Frame(Window, background = 'white', border = 30)
UI_frame.grid(row=0, column=0, padx = 0, pady = 0)

#animation canvas config
canvas = tkinter.Canvas(UI_frame)
canvas.configure(bg="white",width=Window_Width, height=Window_Height)
canvas.pack(fill="both", expand=True)


btn = tkinter.Button(UI_frame, text = 'Shuffle',bd = 5,command = lambda: [shuff_col(), shuff_col(),shuff_col(), shuff_col(),shuff_col(), shuff_col()])
btn.pack(side = 'left')

btn = tkinter.Button(UI_frame, text = 'Bubble',bd = 5,command = lambda: Bubble())
btn.pack(side = 'right')

btn = tkinter.Button(UI_frame, text = 'Insertion',bd = 5,command = lambda: insertionSort(yval))
btn.pack(side = 'right')

btn = tkinter.Button(UI_frame, text = 'Merge',bd = 5,command = lambda: timefunc())
btn.pack(side = 'right')

btn = tkinter.Button(UI_frame, text = 'Quick',bd = 5,command = lambda: timesort())
btn.pack(side = 'right')

btn = tkinter.Button(UI_frame, text = 'cocktail',bd = 5,command = lambda: cocktailSort(yval))
btn.pack(side = 'right')

btn = tkinter.Button(UI_frame, text = 'Shell',bd = 5,command = lambda: shellSort(yval))
btn.pack(side = 'right')

root.mainloop()
Window.mainloop()
import tkinter as Tkinter
from datetime import datetime

counter = 500000
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 500000:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
            label['text'] = display
            label.after(1000, count)
            counter += 1
    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

def Reset(label):
    global counter
    counter = 1000
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'
root = Tkinter.Tk()
root.title("Stopwatch by JC")
root.minsize(width=400, height=200)
label = Tkinter.Label(root, text="Welcome!", fg="blue", font="Brutalism 33 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', bg="black", fg="white", height=2, width=10, command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', bg="black", fg="white", height=2, width=10, state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', bg="black", fg="white", height=2, width=10, state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=50)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop()
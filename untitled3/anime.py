from tkinter import *
press = True
energy = 100
day = 0
c=5
ind=1

def start(event):
    global press
    if press == False:
        pass
    else:
        startLabel.config(text="")
        updateHeart()
        updateDay()
        updateDisplay()
        press = False


def updateDisplay():
    global energy
    global day
    if energy <= 50:
        p=1
        #himage.config(image=h2)
    else:
        p=1
        #himage.config(image=h2)
    bombLabel.config(text="Fitil:"+str(energy))
    dayLabel.config(text="Day:"+str(day))


def updateHeart():
    global energy
    global ind
    global c
    energy-=1
    if isAlive():
        bombLabel.after(500,updateHeart)
        k= int(ind %c)
        print(k)
        ind+=1


def updateDay():
    global day
    day+=1
    if isAlive():
        dayLabel.after(5000,updateDay)

def stop():
    global energy
    if isAlive():
        if energy<=68:
            energy+=20
        else:
            energy-=20
def isAlive():
    global energy
    if energy<=0:
        startLabel.config(text="KILL KILL ME")
        return False
    else:
        return True

def update(ind,frames,label,c):
   # ind=max(ind,1)
    frame = frames[ind]
    ind += 1
    ind%=c
    label.configure(image=frame)
    root.after(c, update, ind,frames,label,6)


root = Tk()

root.title("Heart")
root.geometry("1280x720")

startLabel = Label(root, text="tab enter button")
bombLabel = Label(root, text="Fitil:"+str(energy))
dayLabel = Label(root, text="Day:"+str(day))
startLabel.pack()
bombLabel.pack()
dayLabel.pack()
print("kill")

frames1=[PhotoImage(file="heartnorm.gif",format="gif -index %i" %(i)) for i in range(c)]


def update(ind,frames,label,c):
   # ind=max(ind,1)
    frame = frames[ind]
    ind += 1
    ind%=c
    label.configure(image=frame)
    root.after(c, update, ind,frames,label,c)


label1 = Label(root,width=500,height=500)
label1.pack()
root.after(0, update, 0,frames1,label1,c)
heart_out = Button(root, text="Click on me!!!",command=stop)
heart_out.pack()

root.bind('<Return>', start)

root.mainloop()
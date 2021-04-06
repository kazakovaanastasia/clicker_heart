from tkinter import *

press = True
energy = 200
day = 10
c=5
ind=1

def start(event):
    label0.pack_forget()
    label1.pack()

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
        bombLabel.config(text="Energy left: IM ENDING NO" + str(energy))

    else:
        p=35
    bombLabel.config(text="Energy left:"+str(energy))
    dayLabel.config(text="levels_left:"+str(day))
    label1.after(500, updateDisplay)


def updateHeart():
    global energy
    global ind
    global c
    energy-=15
    if isAlive():
        bombLabel.after(1200,updateHeart)
        k= int(ind %c)
        ind+=1


def updateDay():
    global day
    day-=1
    if day<=0:
        startLabel.config(text="В мире чувства есть лишь один закон – составить счастье того, кого любишь.")
        bombLabel.config(text="Energy left,WINNER" + str(energy))
        dayLabel.config(text="levels_left,WINNER" + str(day))
    else:
        if isAlive():
            dayLabel.after(9000,updateDay)

def click():
    global energy
    if isAlive():
        if ((energy>=29) and (energy<=89)) or ((energy>=120) and (energy<=180)):
            energy+=10
        else:
            energy-=20

def isAlive():
    global energy
    if energy<=0:
        startLabel.config(text="Тот, кого разлюбили, обычно сам виноват, что вовремя этого не заметил.")
        global c
        c=20
        frames1 = [PhotoImage(file="broken.gif", format="gif -index %i" % (i)) for i in range(c)]
        global label1
        label1.pack_forget()
        label1 = Label(root, width=500, height=500)

        label1.pack()
        root.after(0, update, 0, frames1, label1, c)
        root.mainloop()

        return False
    else:
        return True


root = Tk()

root.title("Heart")
root.geometry("1280x720")

startLabel = Label(root, text="tab enter button")
bombLabel = Label(root, text="ENERGY LEVEL:"+str(energy))
dayLabel = Label(root, text="levels_NUMBER:"+str(day))
startLabel.pack()
bombLabel.pack()
dayLabel.pack()

frames1=[PhotoImage(file="heartnorm.gif",format="gif -index %i" %(i)) for i in range(c)]
frames2=PhotoImage(file="hs.png")


def update(ind,frames,label,c):
   # ind=max(ind,1)
    frame = frames[ind]
    ind += 1
    ind%=c
    label.configure(image=frame)
    root.after(c, update, ind,frames,label,c)

label0=Label(root,image=frames2)
label1 = Label(root,width=500,height=500)
label0.pack()

root.after(0, update, 0,frames1,label1,c)
heart_out = Button(root, text="Click on me!!!",command=click)

root.bind('<Return>', start)

heart_out.pack()

root.mainloop()
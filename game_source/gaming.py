from tkinter import Tk, Label, PhotoImage, Button

press = True
time_day = 10000
auto_clicker = 0
health_support = 0
energy = 200
day = 16
c = 5
ind = 1


def zero(event):
    label0.pack_forget()
    label1.pack()

    global press
    if press == False:
        pass
    else:
        zeroLabel.config(text=":3")
        newHeart()
        newDay()
        newFrame()
        press = False


def newFrame():
    global energy
    global day
    if energy <= 50:
        bombLabel.config(text="Energy left: IM ENDING NO" + str(energy))

    else:
        p = 35
    bombLabel.config(text="Energy left:" + str(energy))
    dayLabel.config(text="levels_left:" + str(day))
    label1.after(500, newFrame)


def newHeart():
    global energy
    global ind
    global c
    energy -= 15
    if isAlive():
        bombLabel.after(1200, newHeart)
        k = int(ind % c)
        ind += 1


def newDay():
    global day
    day -= 1
    if (day % 3 == 0):
        global energy
        energy += health_support
        zeroLabel.config(text="Какое улучшение вы выберите?Ускорение дней или восстановлкение энергии?")
        global heart_1
        global heart_2
        heart_1.config(text="С каждой новой минутой начинается для нас новая жизнь.", command=reduce_day)
        heart_2.config(text="Не держись за злость, боль или страдание: они крадут твою энергию и препятствуют любви.",
                       command=add_health)

    if day <= 0:
        zeroLabel.config(text="В мире чувства есть лишь один закон – составить счастье того, кого любишь.")
        bombLabel.config(text="Energy left,WINNER" + str(energy))
        dayLabel.config(text="levels_left,WINNER" + str(day))
    else:
        if isAlive():
            dayLabel.after(time_day, newDay)


def reduce_day():
    global time_day
    time_day = int(0.95 * time_day)
    global heart_1
    zeroLabel.config(text="Важно отпустить того, кто так и не полюбил тебя.")
    heart_1.config(text="С каждым днем я тихонько схожу с ума", command=nothing)
    heart_2.config(text="От переизбытка боли и недостатка тебя.",
                   command=nothing)


def add_health():
    global health_support
    health_support += 5
    global heart_2
    zeroLabel.config(text="Важно отпустить того, кто так и не полюбил тебя.")
    heart_1.config(text="Ведь разлюбить не сможешь ты,", command=nothing)
    heart_2.config(text="Как полюбить ты не сумела…",
                   command=nothing)


def nothing():
    global energy
    if (energy < 10):
        energy -= 1


def click():
    global energy
    if isAlive():
        if ((energy >= 29) and (energy <= 89)) or ((energy >= 120) and (energy <= 180)):
            energy += 10
        else:
            energy -= 20


def isAlive():
    global energy
    if energy <= 0:
        zeroLabel.config(text="Тот, кого разлюбили, обычно сам виноват, что вовремя этого не заметил.")
        global c
        c = 20
        frames1 = [PhotoImage(file="pictures/broken.gif", format="gif -index %i" % (i)) for i in range(c)]
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
root["bg"] = "pink2"
# root.configure(background="pictures/heartnorm.gif")

root.title("Heart")
root.geometry("600x600")

zeroLabel = Label(root, bg='red', fg='yellow', text="tab enter button")
bombLabel = Label(root, text="ENERGY LEVEL:" + str(energy))
dayLabel = Label(root, text="levels_NUMBER:" + str(day))
zeroLabel.pack()
bombLabel.pack()
dayLabel.pack()

frames1 = [PhotoImage(file="pictures/heartnorm.gif", format="gif -index %i" % (i)) for i in range(c)]
frames2 = PhotoImage(file="pictures/startone.png")


def update(ind, frames, label, c):
    # ind=max(ind,1)
    frame = frames[ind]
    ind += 1
    ind %= c
    label.configure(image=frame)
    root.after(c, update, ind, frames, label, c)


label0 = Label(root, image=frames2)
label1 = Label(root, width=5000, height=5000)
label0.pack()

root.after(0, update, 0, frames1, label1, c)
heart_out = Button(root, text="Click on me!!!", command=click)
heart_1 = Button(root, bg="red", fg='yellow', text="сюрприз")
heart_2 = Button(root, bg="red", fg='yellow', text="не смотри!")
heart_1.pack()

heart_2.pack()

root.bind('<Return>', zero)

heart_out.pack()

root.mainloop()

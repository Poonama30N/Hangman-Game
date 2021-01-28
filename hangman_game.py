from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox


top=Tk()
#top.configure(background='plum1')
e1=StringVar()
e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
top.geometry("900x600")
chances=0
correct=0
pic_arr=['dog.png','jam.png','cat.png','bat.png','pan.png','van.png','book.png','kite.png','room.png','java.png','BOMB.png']
img = Image.open(pic_arr[chances])
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(top, image = img)
panel.grid(column=0, row=0)


def next():
    check2()
    global chances
    global guess
    chances=chances+1
    guess=3
    if chances>=6:
        reset2()
    else:
        reset()
    img = Image.open(pic_arr[chances])
    img = img.resize((200, 200), Image.ANTIALIAS)
    imgnew= ImageTk.PhotoImage(img)
    panel.configure(image=imgnew)
    panel.image=imgnew

def reset():
    global count
    count=1
    e4.set(guess)
    b1=Button(top,textvariable=e1,width=5,height=3,bg="white").grid(row=1,column=2)
    e1.set(" ")
    b2=Button(top,textvariable=e2,width=5,height=3,bg="white").grid(row=1,column=3)
    e2.set(" ")
    b3=Button(top,textvariable=e3,width=5,height=3,bg="white").grid(row=1,column=4)
    e3.set(" ")

def reset2():
    global count
    count=1
    e4.set(guess)
    b1=Button(top,textvariable=e1,width=5,height=3,bg="white").grid(row=1,column=2)
    e1.set(" ")
    b2=Button(top,textvariable=e2,width=5,height=3,bg="white").grid(row=1,column=3)
    e2.set(" ")
    b3=Button(top,textvariable=e3,width=5,height=3,bg="white").grid(row=1,column=4)
    e3.set(" ")
    b4=Button(top,textvariable=e5,width=5,height=3,bg="white").grid(row=1,column=5)
    e5.set(" ")
    
    
count=1
global a1,a2,a3,a4
def click(alphabet):
    global count
    global st
    global a1,a2,a3,a4
    if count==1:
        e1.set(alphabet)
        a1=alphabet
    elif count==2:
        e2.set(alphabet)
        a2=alphabet
    elif count==3:
        e3.set(alphabet)
        a3=alphabet
    elif count==4:
        e5.set(alphabet)
        a4=alphabet
    count=count+1    

guess=3     
def check():
    global chances,correct
    global a1,a2,a3,a4
    global guess
    import sqlite3
    conn=sqlite3.connect('pic.db')
    c=conn.cursor()
    
        
    if chances<6:
        for row in c.execute("SELECT * FROM pics"):
            if chances+1==row[0]:
                if a1+a2+a3 == row[1]:
                    txt='right answer!!'
                    messagebox.showinfo('congrats',txt)
                    correct=correct+1
                    next()
                    break
                else:
                    guess=guess-1
                    txt='wrong answer!!\n Try again\nNumber of chances left : ' +str(guess)
                    messagebox.showinfo('Oops',txt)
                    if guess==0:
                        txt="You Lost the game.Hanged!!!!"
                        messagebox.showinfo('Oops',txt)
                        top.destroy()
        
                    reset()


    else:
        for row in c.execute("SELECT * FROM pics"):
            if chances+1==row[0]:
                if a1+a2+a3+a4 == row[1]:
                    txt='right answer!!'
                    messagebox.showinfo('congrats',txt)
                    correct=correct+1
                    next()
                    break
                else:
                    guess=guess-1
                    txt='wrong answer!!\n Try again\nNumber of chances left : ' +str(guess)
                    messagebox.showinfo('Oops',txt)
                    if guess==0:
                        txt="You Lost the game.Hanged!!!!"
                        messagebox.showinfo('Oops',txt)
                        top.destroy()
                    reset2()
        
         

def hint():
    global chances
    import sqlite3
    conn=sqlite3.connect('pic.db')
    c=conn.cursor()
    for row in c.execute('select * from pics'):
        if row[0]==chances+1:
            messagebox.showinfo("HINT",row[2])
    
def check2():
    global correct
    if correct==11:
        messagebox.showinfo(" ","Congratulations!!!\nYou have won the game")
        top.destroy()
        

ck=Button(top,text='check',bg='lightblue',width=20,command=check,anchor=S).grid(row=0,column=2)

nextB=Button(top,text='next',bg='lightblue',width=20,command=next,anchor=N)
nextB.grid(row=0,column=4)
reset()

w=Label(top,height=3).grid(row=2)


a=Button(top,text='A',bg='aquamarine',width=10,command=lambda:click('A')).grid(row=3,column=0)
b=Button(top,text='B',bg='aquamarine',width=10,command=lambda:click('B')).grid(row=3,column=1)
c=Button(top,text='C',bg='aquamarine',width=10,command=lambda:click('C')).grid(row=3,column=2)
d=Button(top,text='D',bg='aquamarine',width=10,command=lambda:click('D')).grid(row=3,column=3)
e=Button(top,text='E',bg='aquamarine',width=10,command=lambda:click('E')).grid(row=3,column=4)
f=Button(top,text='F',bg='aquamarine',width=10,command=lambda:click('F')).grid(row=3,column=5)
g=Button(top,text='G',bg='aquamarine',width=10,command=lambda:click('G')).grid(row=4,column=0)
h=Button(top,text='H',bg='aquamarine',width=10,command=lambda:click('H')).grid(row=4,column=1)
i=Button(top,text='I',bg='aquamarine',width=10,command=lambda:click('I')).grid(row=4,column=2)
j=Button(top,text='J',bg='aquamarine',width=10,command=lambda:click('J')).grid(row=4,column=3)
k=Button(top,text='K',bg='aquamarine',width=10,command=lambda:click('K')).grid(row=4,column=4)
l=Button(top,text='L',bg='aquamarine',width=10,command=lambda:click('L')).grid(row=4,column=5)
m=Button(top,text='M',bg='aquamarine',width=10,command=lambda:click('M')).grid(row=5,column=0)
n=Button(top,text='N',bg='aquamarine',width=10,command=lambda:click('N')).grid(row=5,column=1)
o=Button(top,text='O',bg='aquamarine',width=10,command=lambda:click('O')).grid(row=5,column=2)
p=Button(top,text='P',bg='aquamarine',width=10,command=lambda:click('P')).grid(row=5,column=3)
q=Button(top,text='Q',bg='aquamarine',width=10,command=lambda:click('Q')).grid(row=5,column=4)
r=Button(top,text='R',bg='aquamarine',width=10,command=lambda:click('R')).grid(row=5,column=5)
s=Button(top,text='S',bg='aquamarine',width=10,command=lambda:click('S')).grid(row=6,column=0)
t=Button(top,text='T',bg='aquamarine',width=10,command=lambda:click('T')).grid(row=6,column=1)
u=Button(top,text='U',bg='aquamarine',width=10,command=lambda:click('U')).grid(row=6,column=2)
v=Button(top,text='V',bg='aquamarine',width=10,command=lambda:click('V')).grid(row=6,column=3)
w=Button(top,text='W',bg='aquamarine',width=10,command=lambda:click('W')).grid(row=6,column=4)
x=Button(top,text='X',bg='aquamarine',width=10,command=lambda:click('X')).grid(row=6,column=5)
y=Button(top,text='Y',bg='aquamarine',width=10,command=lambda:click('Y')).grid(row=7,column=2)
z=Button(top,text='Z',bg='aquamarine',width=10,command=lambda:click('Z')).grid(row=7,column=3)
w1=Label(top,height=3).grid(row=8)
last=Label(top,text="Guesses left : ").grid(row=9,column=2)
gs=Button(top,textvariable=e4,width=6,bg="white").grid(row=9,column=3)
w2=Label(top,height=3).grid(row=9)
hint=Button(top,text="Hint",bg='orange',width=20,command=hint).grid(row=10,column=3)

top.mainloop()



'''import sqlite3
conn=sqlite3.connect('pic.db')
c=conn.cursor()
c.execute("alter table pics add hints text")
c.execute("update pics set hints='explosive weapon' where id=11")
c.execute("create table pics(id number,value text)")
c.execute("insert into pics values('11','BOMB',' ')")
conn.commit()
conn.close()
for row in c.execute("select * from pics"):
    print(row)
'''































#! /usr/env python3

from tkinter import *
from  math import *
import math


from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    time_display.config(text=string)
    time_display.after(1000, time)

win = Tk()
win.geometry("400x500")
win.title("SCIENTIFIC CALCULATOR")
win.resizable(0,0)
win.configure(background="royal blue")
#win.iconbitmap("dist\\bit.ico")
time_frame = Frame(win ,width=3,height=2,bg="royal blue")
time_frame.pack(expand=YES,fill=X,pady=10, padx=10)

time_display = Label(time_frame,font=(('DS-DIGI'),15),background = "black",fg="red")
time_display.pack(side=RIGHT,fill=X)
time()
lb = Label(time_frame, text="Time: ",font=('arial',20,'bold'),bg="royal blue")
lb.pack(side=RIGHT,fill=X)

first_frame = Frame(win, width=10, height=40)
first_frame.pack(expand=NO, fill=X, pady=10, padx=10)

display = Entry(first_frame, borderwidth=5,justify="left",font=("DS-DIGIB",20), bg=("black"), fg="red")
display.pack(fill=BOTH,expand=YES)
se_display = Entry(first_frame, borderwidth=5,justify="right",font=("DS-DIGIT",25), bg=("black"), fg="red")
se_display.pack(fill="both",expand="yes")

fu_frame = Frame(win,width=10,bg="royal blue")
fu_frame.pack(anchor=W)

#functions
def put_seven():
    t = display.insert(END, 7)
    
    
def put_eight():
    t = display.insert(END, 8)
    
    
    
def put_nine():
    t = display.insert(END, 9)
    
    
def put_four():
    t = display.insert(END, 4)
    
    
def put_five():
    t = display.insert(END, 5)
    
    
def put_six():
    t = display.insert(END, 6)
    
    
def put_one():
    t = display.insert(END, 1)
    
    
def put_two():
    t = display.insert(END, 2)
    
    
def put_three():
    t = display.insert(END, 3)
    
    
def put_zero():
    t = display.insert(END, 0)
    
    
def add_val():
    y = display.get()
    display.delete(0,END)
    ui = ("+")
    display.insert(END,y + ui)
    
    
def evaluate():
    y = display.get()
    u=eval(y)
    se_display.delete(0,END)
    se_display.insert(END, u)
    print(u)
    
    
def sub():
    i = display.get()
    display.delete(0,END)
    sign =("-")
    display.insert(END,i + sign)
    
    
def divid():
    t=display.get()
    display.delete(0,END)
    sign=('/')
    display.insert(END,t + sign)
    
    
def clear():
    display.delete(0,1000)
    se_display.delete(0,100)
    
    
def Ac():
    current=display.get()
    leng=len(current)-1
    display.delete(leng,END)
    
    
def multiply():
    r=display.get()
    display.delete(0,END)
    sign=('*')
    display.insert(END,r+sign)
    
    
def SIN():
    y= float(se_display.get())
    u = math.sin(y)
    se_display.delete(0, END)
    se_display.insert(END,f'{u}')
    
    
def COS():
    y= float(display.get())
    p = math.cos(y)
    se_display.delete(0,1000)
    se_display.insert(END,p)
    
    
def TAN():
    t= float(display.get())
    y = math.tan(t)
    se_display.delete(0,END)
    se_display.insert(END,y)
    
    
def LOG():
    U = float(display.get())
    t = math.log10(U)
    se_display.delete(0,10)
    se_display.insert(0,t)
    

def LN():
    t = float(display.get())
    p = math.log(t)
    se_display.delete(0,END)
    se_display.insert(END,p)
    
    
def EXP():
    y = float(display.get())
    p = math.exp(y)
    se_display.delete(0,END)
    se_display.insert(END,p)
    
    
def SQR():
    i = float(display.get())
    o = str(math.sqrt(i))
    se_display.delete(0,10)
    ty = (("√")+str(i))+(("=")+o)
    se_display.insert(0, ty)
    
    
def put_par():
    ty= display.get()
    display.insert(len(ty)+1,'(')
def put_par_close():
    u = display.get()
    I = (')')
    display.insert(len(u)+1,I)
    
    
def FACT():
    r = int(display.get())
    w = math.factorial(r)
    se_display.delete(0,100)
    jk = (str(r)+("!")+("=")+str(w))
    se_display.insert(0,jk)
    
    
#def PWR():
#    y = display.get()
#    i = math.pow
def root():
    e = int(display.get())
    g = (e**(2))
    display.delete(0,10)
    display.insert(0, g)
    
    
def cube_root():
    r = display.get()
    y = int(r)
    k = (1/3)
    u = (y**k)
    w= str(u)
    display.delete(0,10)
    display.insert(0,w)
    
    
def put_pi():
    o = math.pi
    display.insert(END, o)
    
    
def cubed():
    y= display.get()
    root= int(y)
    display.delete(0,10)
    op= root**3
    p = str(op)
    display.insert(0,p)
    
    
def inverse():
    y = display.get()
    display.delete(END,0)
    se_display.insert(0,1/(int(y)))
    
    
def ROOT():
    display.insert(END,".")
    
    
def Comb():
    what = float(display.get())
    se_display.delete(0,1000)
    display.delete(0,1000)
    se_display.insert(0,str(what)+("C "))
    fg = float(display.get())
    amo = math.comb(round(what), round(fg))
    display.insert(0,fg)
    se_display.delete(0,100)
    se_display.insert(0, amo)
def Perm():
    pass
def mod():
    pass
def cube_root_of():
    pass
def ROOTed():
    pass
def convert_deg():
    t = float(display.get())
    y= math.degrees(t)
    se_display.delete(0,END)
    se_display.insert(END, y)



rad1 = Button(fu_frame,text="Convert to Degrees",command=convert_deg,fg="brown",bg="green")
rad1.pack(padx=10)
#rad2 = Radiobutton(fu_frame,text="Radians",value=0,)
#rad2.pack(anchor=E)

second_frame = Frame(win, width=18, height=60 )
second_frame.pack(fill = X,padx=10)

#buttons for first frame
sin_bt = Button(second_frame, bg="brown", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Sin", command=SIN)
sin_bt.pack(fill="both", side=LEFT,expand=YES)

cos_bt = Button(second_frame,bg="brown", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Cos",command=COS)
cos_bt.bind("<Button-1>")
cos_bt.pack(fill="both", side=LEFT,expand=YES)

tan_bt = Button(second_frame, bg="brown", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Tan", command=TAN)
tan_bt.pack(fill="both", side=LEFT,expand=YES)

log_bt = Button(second_frame, bg="brown", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Log",command=LOG)
log_bt.pack(fill="both", side=LEFT,expand=YES)

ln_bt = Button(second_frame, bg="brown", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="ln",command=LN)
ln_bt.pack(fill="both", side=LEFT,expand=YES)

th_frame = Frame(win, width=18, height=60 )
th_frame.pack(fill = X,padx=10)
#buttons
exp_bt = Button(th_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Exp",command=EXP)
exp_bt.pack(fill="both", side=LEFT,expand=YES)

hyp_bt = Button(th_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="√",command=SQR)
hyp_bt.pack(fill="both", side=LEFT,expand=YES)

open_bracket_bt = Button(th_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="(",command=put_par)
open_bracket_bt.pack(fill="both", side=LEFT,expand=YES)

close_bracket_bt = Button(th_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text=")",command=put_par_close)
close_bracket_bt.pack(fill="both", side=LEFT,expand=YES)

factorial_bt = Button(th_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="❕",command=FACT)
factorial_bt.pack(fill="both", side=LEFT,expand=YES)

fourth_frame = Frame(win, width=18, height=60 )
fourth_frame.pack(fill = X,padx=10)

#buttons
comb_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="nCr", command= Comb)
comb_bt.pack(fill="both", side=LEFT,expand=YES)

PERM_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Perm", command=Perm)
PERM_bt.pack(fill="both", side=LEFT,expand=YES)

mod_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="Mod",command=mod)
mod_bt.pack(fill="both", side=LEFT,expand=YES)

PWO_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="X^y",command=cube_root_of)
PWO_bt.pack(fill="both", side=LEFT,expand=YES)

perm_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="x√",command=ROOTed)
perm_bt.pack(fill="both", side=LEFT,expand=YES)


fourth_frame = Frame(win, width=18, height=60 )
fourth_frame.pack(fill = X,padx=10)

#buttons
sin_inverse_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="X³", command= cubed)
sin_inverse_bt.pack(fill="both", side=LEFT,expand=YES)

cos_inverse_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="X²", command=root)
cos_inverse_bt.pack(fill="both", side=LEFT,expand=YES)

tan_inverse_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="1/X",command=inverse)
tan_inverse_bt.pack(fill="both", side=LEFT,expand=YES)

cube_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="³√",command=cube_root)
cube_bt.pack(fill="both", side=LEFT,expand=YES)

point_bt = Button(fourth_frame, bg="grey", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text=".",command=ROOT)
point_bt.pack(fill="both", side=LEFT,expand=YES)


fifth_frame = Frame(win, width=18, height=60 )
fifth_frame.pack(fill = X,padx=10)
#buttons
seven_bt = Button(fifth_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="7", command=put_seven)
seven_bt.pack(fill="both", side=LEFT,expand=YES)

eight_bt = Button(fifth_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="8",command=put_eight)
eight_bt.pack(fill="both", side=LEFT,expand=YES)

nine_bt = Button(fifth_frame, bg="black", fg="white",font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="9",command=put_nine)
nine_bt.pack(fill="both", side=LEFT,expand=YES)

clear_bt = Button(fifth_frame, bg="yellow", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="AC",command=clear)
clear_bt.pack(fill="both", side=LEFT,expand=YES)

delete_bt = Button(fifth_frame, bg="yellow", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="DEL",command=Ac)
delete_bt.pack(fill="both", side=LEFT,expand=YES)

sixth_frame = Frame(win, width=18, height=60 )
sixth_frame.pack(fill = X,padx=10)

#buttons

four_bt = Button(sixth_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="4",command=put_four)
four_bt.pack(fill="both", side=LEFT,expand=YES)

five_bt = Button(sixth_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="5",command=put_five)
five_bt.pack(fill="both", side=LEFT,expand=YES)

six_bt = Button(sixth_frame, bg="black", fg="white",font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="6",command=put_six)
six_bt.pack(fill="both", side=LEFT,expand=YES)

multiplication_bt = Button(sixth_frame, bg="cyan", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="❌",command=multiply)
multiplication_bt.pack(fill="both", side=LEFT,expand=YES)

division_bt = Button(sixth_frame, bg="cyan", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="➗",command=divid)
division_bt.pack(fill="both", side=LEFT,expand=YES)

seventh_frame = Frame(win, width=18, height=60 )
seventh_frame.pack(fill = X,padx=10)

#buttons

one_bt = Button(seventh_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="1",command=put_one)
one_bt.pack(fill="both", side=LEFT,expand=YES)

two_bt = Button(seventh_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="2",command=put_two)
two_bt.pack(fill="both", side=LEFT,expand=YES)

three_bt = Button(seventh_frame, bg="black",fg="white", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="3",command=put_three)
three_bt.pack(fill="both", side=LEFT,expand=YES)

add_bt = Button(seventh_frame, bg="cyan", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="➕", command=add_val)
add_bt.pack(fill="both", side=LEFT,expand=YES)

sub_bt = Button(seventh_frame, bg="cyan", font=("DS-DIGIT",8), borderwidth=1,height=2,width=8,text="➖", command=sub)
sub_bt.pack(fill="both", side=LEFT,expand=YES)

last_frame =Frame(win, width=18, height=60 )
last_frame.pack(fill = X,padx=10)

equl_bt =Button(last_frame,  bg="blue", font=("DS-DIGIT",8), borderwidth=1,height=2,width=12,text="=", command=evaluate)
equl_bt.bind('<Button-2>')
equl_bt.pack(side=RIGHT,fill="both", expand=YES)

zero_bt = Button(last_frame,  bg="black",fg="white", font=("DS-DIGIT",8,"bold"), borderwidth=1,height=2,width=12,text="0",command=put_zero)
zero_bt.pack(side=RIGHT,fill="both", expand=YES)

#pi_image = PhotoImage(file="C:\\Users\\clive\\Documents\\python projects\\pi.png")
pi_bt = Button(last_frame, text='π', borderwidth=1,width=12,height=2,bg="grey",command=put_pi)
pi_bt.pack(side=RIGHT,fill=BOTH,expand=YES)




win.mainloop()

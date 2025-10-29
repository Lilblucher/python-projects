#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 12:38:04 2023

@author: clive
"""
import pyperclip as ppr
import hashlib
from tkinter import *
import random
from tkinter import ttk
from tkinter import messagebox

def main():
    g_ops = str(options.get())
    
    if g_ops == "md5":
        v1  = str(ep.get())
        con = hashlib.md5()
        v2 = con.update(v1.encode())
        v3 = con.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)



    if g_ops == "sha1":
        v1 = str(ep.get())
        conv = hashlib.sha1()
        v2 = conv.update(v1.encode())
        v3  = conv.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)
    
    if g_ops == "sha224":
        v1 = str(ep.get())
        con = hashlib.sha224()
        v2 = con.update(v1.encode())
        v3 = con.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)
        
    if g_ops == "sha256":
        v1  = str(ep.get())
        con = hashlib.sha256()
        v2 = con.update(v1.encode())
        v3 = con.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)
        
        
    if g_ops == 'sha384':
        v1 = str(ep.get())
        con = hashlib.sha384()
        v2  = con.update(v1.encode())
        v3 = con.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)
        
    if g_ops == "sha512":
        v1 = ep.get()
        con = hashlib.sha512()
        v2 = con.update(v1.encode())
        v3 = con.hexdigest()
        out_put.delete(END,0)
        out_put.insert(END,v3)
    

     
    
def copy_txt():
    sd = out_put.get(ACTIVE)
    cp = ppr.copy(sd)
    
    ms = messagebox.showinfo("info","Hash copied to clipboard")     
    
    

    
win = Tk()
win.geometry("550x370")
win.title("Hash converter")

Wel_lb = Label(win, text="HASH CONVERTER",font=("terminal",16,'bold'))
Wel_lb.place(x=120,y=10)


ep_lb = Label(win, text="Enter text to be convertered:", font=("arial",12),)
ep_lb.place(x=10,y=50)

ep = StringVar()
enter_password = Entry(win, textvariable=ep, width=45)
enter_password.place(x=220,y=50)

op_ls = ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']
options = ttk.Combobox(win, value=op_ls)
options.current(random.randint(0,5))
options.place(x=130,y=90)

gen_bt = Button(win, text="Generate Hash", command=main)
gen_bt.place(x=430,y=90)

out_lb = Label(win, text="Generated Hash:", font="corbel")
out_lb.place(x=110,y=130) 




out_put = Listbox(win, width=77)
out_put.place(x=5,y=150)


cp_bt = Button(win, text="copy", command=copy_txt)
cp_bt.place(x=4, y=340)




win.mainloop()



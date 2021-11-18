import tkinter as tk
from tkinter import*
import random
from tkinter import messagebox
main=tk.Tk()
#*****body*******
main.title("PAIRS")
main.geometry("340x280")
main.configure(bg="#C9DFEC")
main.resizable(0,0)

#matches
match=[99,99,100,100,50,50,44,44,66,66,77,77]
#shuffling
random.shuffle(match)


#frame******
frame_=Frame(main)
frame_.pack(pady=10,padx=10,)
#********win_logic***************
winn=0
def win():
        global stepp
        s="NO OF STEP:"
        z=str(stepp)
        step.configure(text=s+z)
        dis.configure(text="Congulation You Win!",font="bold")

#********main_logic***************
count=0
ans_list=[]
ans_dict={}
stepp=0
def whenclick(b,index):
    global count,ans_list,ans_dict,winn,stepp

    stepp+=1

    if b["text"]== " " and count<2:
        b["text"]=match[index]
        
        ans_list.append(index)
        ans_dict[b]=match[index]
        count+=1
      
    #correct or not
    if len(ans_list) == 2:
        if match[ans_list[0]] == match[ans_list[1]]:
            for key in ans_dict:
               key["state"]="disabled"
            count=0   
            ans_list=[]
            ans_dict={}
            winn+=1
            if winn==6:
                win()
            
        else:
            count=0
            ans_list=[]
            messagebox.showinfo("Error!","Incorrect!")
            
            #reset the button
            for key in ans_dict:
                key["text"]=" "
            ans_dict={}
    
#button of row 1
b0=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b0,0),relief="groove")
b0.grid(row=0,column=0,)

b1=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b1,1),relief="groove")
b1.grid(row=0,column=1,)

b2=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b2,2),relief="groove")
b2.grid(row=0,column=2,)

b3=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b3,3),relief="groove")
b3.grid(row=0,column=3,)

#button of row 2
b4=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b4,4),relief="groove")
b4.grid(row=1,column=0,)

b5=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b5,5),relief="groove")
b5.grid(row=1,column=1,)

b6=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b6,6),relief="groove")
b6.grid(row=1,column=2,)

b7=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b7,7),relief="groove")
b7.grid(row=1,column=3,)

#button of row 3
b8=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b8,8),relief="groove")
b8.grid(row=2,column=0,)

b9=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b9,9),relief="groove")
b9.grid(row=2,column=1,)

b10=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b10,10),relief="groove")
b10.grid(row=2,column=2,)

b11=Button(frame_,text=" ",width=10,height=4,command=lambda:whenclick(b11,11),relief="groove")
b11.grid(row=2,column=3)

#displaying msg
dis=Label(main,text="PAIRS_GAME",bg="#C9DFEC",font="bold")
dis.pack()
step=Label(main,text=" ",bg="#C9DFEC")
step.pack()

mainloop()

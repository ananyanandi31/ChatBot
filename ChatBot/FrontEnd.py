# -*- coding: utf-8 -*-


import tkinter as tk
from PIL import ImageTk, Image
import bot

master = tk.Tk()
def conversation():
    query=textF.get()
    chat=bot.Chat(bot.pairs, bot.reflections)
    answer=chat.respond(query)
    msg.insert(tk.END, "You : " +query)
    msg.insert(tk.END, "ChatBot : " + answer)
    textF.delete(0,tk.END)
    
def userText(event):
    textF.delete(0,tk.END)
    
    
master.title("ChatBot")
master.geometry("500x900")
img=ImageTk.PhotoImage(Image.open(r"C:\Users\Student\Desktop\chatbot.jpeg"))
photo=tk.Label(master, image=img,width=220,height=180)
photo.grid(column=1,row=1)
photo.pack(pady=10)
master.configure(bg='#76D7C4')
frame=tk.Frame(master)
sc=tk.Scrollbar(frame)
msg=tk.Listbox(frame, width=80, height=25,fg='white')
msg.configure(bg='black')
sc.pack(side=tk.RIGHT, fill=tk.Y)
msg.pack(side=tk.LEFT, fill=tk.BOTH, pady=10)
frame.pack()
textF=tk.Entry(master, font=("Times New Roman", 12),fg='#0B5345',bg="#D1F2EB",width=25)
textF.insert(1,"Start conversation here")
textF.bind("<Button>",userText)
textF.pack(pady=20)
button =tk.Button(master,
                   text="Submit",
                   font="Arial",
                   fg="white",
                   bg="black",
                   command=conversation)
button.pack()
master.mainloop()

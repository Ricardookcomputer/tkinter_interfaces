import tkinter as tk

ventana=tk.Tk()# La sefunda t va en mayuscula
ventana.title("Mi primer ventana")
ventana.geometry("600x400+0+0")
ventana.minsize(400,200)
ventana.maxsize(800,600)
ventana.iconbitmap("albert_einstein.ico")
ventana.configure(bg="DodgerBlue2")
ventana.resizable(False,True)#Horizontal y vertical
ventana.attributes("-alpha",0.1)
ventana.mainloop()
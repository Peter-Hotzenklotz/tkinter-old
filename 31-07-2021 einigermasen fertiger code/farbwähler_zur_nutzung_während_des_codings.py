# This Python file uses the following encoding: utf-8


from tkinter import *
from tkinter.colorchooser import *

__all__ = ['farbwähler_zur_nutzung_während_des_codings']


def example():
    def getColor():
        color= askcolor()
        aa.set(color)
        try:
            print(str(color[1]))
            button["bg"]=str(color[1])
        except:
            print("unknown")

    def setColor():
        color= button2.cget("bg")
        aa.set(color)
        button["bg"]=str(color)


    master=Tk()
    master.geometry("1000x500")
    aa=StringVar()

    lbl1=Entry(master, textvariable=aa,font=('Times', '-40'))
    lbl1.pack(fill="both",side="top",expand=True)

    button=Button(text="Select Color", command=getColor,font=('Times', '-40'))
    button.pack(fill="both",side="bottom",expand=True)

    button2=Button(text="own collor", command=setColor,font=('Times', '-40'))
    button2.pack(fill="both",side="bottom")

    master.mainloop()


if __name__ == "__main__":
    example()
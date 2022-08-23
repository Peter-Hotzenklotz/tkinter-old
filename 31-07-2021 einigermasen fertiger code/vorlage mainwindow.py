# This Python file uses the following encoding: utf-8

from tkinter import *

__all__ = ['window 0.py']

def main(font):

    def zurück():
        pass

    def weiter():
        pass



    canvas_1_scrollregion_height=0
    def fenstergröße_event(event):
        nonlocal canvas_1_scrollregion_height
        print("größenänderung")
        canvas_1.itemconfigure(id, width=canvas_1.winfo_width())

        try:
            canvas_1_scrollregion_height=0
            #for objekt in (canvas_1.Frame.grid_slaves()):
            for objekt in (canvas_1.Frame.pack_slaves()):
                canvas_1_scrollregion_height += objekt.winfo_height()
        except:
            print("ein error")
        print(canvas_1_scrollregion_height)

        canvas_1["scrollregion"]=(0,0,0,canvas_1_scrollregion_height)


    master=Tk()

    botFr = Frame(master,takefocus=0,width=0,height=0)
    botFr.pack(fill="x",side="bottom",anchor="s",expand=False)

    topFr=Frame(master,width=0,height=0)
    botFr.pack(fill="both",side="top",anchor="n",expand=True)


    botFr.pack(fill="x",side="bottom",anchor="n",expand=False)
    topFr.pack(fill="both",side="top",anchor="n",expand=True)


    #botFr
    zurück_button = Button(botFr, text="zurück",command=zurück,height="1",font=('Times', '-20'),takefocus=0)
    weiter_button = Button(botFr, text="weiter",command=weiter,height="1",font=('Times', '-20'),takefocus=0)

    zurück_button.pack(side="left",fill="x",expand=True)
    weiter_button.pack(side="right",fill="x",expand=True)

    #topFr
    scrollbar1=Scrollbar(topFr,width=19)
    canvas_1= Canvas(topFr,scrollregion=(0,0,0,0),bg="yellow")

    scrollbar1.pack(anchor="ne",side="right",fill="y")
    canvas_1.pack(anchor="ne",fill="both",expand=True,side="right")

    scrollbar1.config(command=canvas_1.yview)
    canvas_1.config(yscrollcommand=scrollbar1.set)

    canvas_1.Frame = Frame(topFr,bg="orange")


    #canvas_1.Frame

    id=canvas_1.create_window(0,0,anchor="nw",width=0,height=0,window=canvas_1.Frame)



    master.bind('<Configure>',fenstergröße_event)

    LF1=LabelFrame(canvas_1.Frame,text="suchort")
    LF2=LabelFrame(canvas_1.Frame,text="suchmethode")
    LF3=LabelFrame(canvas_1.Frame,text="suchergebnissbehandlung")

    #canvas_1.Frame.columnconfigure(0,weight=1)
    #canvas_1.Frame.columnconfigure(1, weight=1)

    #LF1.grid(row=0,column=0,sticky=NSEW)
    #LF2.grid(row=1,column=0,sticky=NSEW)
    #LF3.grid(row=2,column=0,sticky=NSEW)

    LF1.pack(fill="x",expand=True,side="bottom",anchor=S)
    LF2.pack(fill="x",expand=True,side="bottom",anchor=S)
    LF3.pack(fill="both",expand=True,side="bottom",anchor=S)



    #LF1
    B1=Button(LF1,text="erster",font=font)
    B2=Button(LF2,text="erster",font=font)
    B3=Button(LF3,text="erster",font=font)


    B1.pack(side="top",anchor="w")
    B2.pack(side="left")
    B3.pack(side="left")




    mainloop()


if __name__ == "__main__":
    main(font=('Times', '-20'))
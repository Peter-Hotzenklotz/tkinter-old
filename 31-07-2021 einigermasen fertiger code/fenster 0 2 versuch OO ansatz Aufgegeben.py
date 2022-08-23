# This Python file uses the following encoding: utf-8

import tkinter as tk


__all__ = ['Vorlage tkinter.py']


class Application(tk.Frame):
    def __init__(self, master=None,font=('Times', '-20')):
        tk.Frame.__init__(self, master)
        self.pack(fill="both",expand=True)
        self.create_Widgets(font=font)

        start=True
        def config_handler(event,self=self,start=start):
            return self.__fenstergröße_event(event,start)
        self.bind('<Configure>',config_handler)






    def __fenstergröße_event(self,event,start):
        print("funkt")
        #nonlocal scrollregion_height
        #nonlocal scroll_height
        print(self.Canvas_topFr.winfo_width())
        #self.Canvas_topFr.itemconfigure(id,width=self.Fr1.winfo_width())
        self.Canvas_topFr.itemconfigure(id,width=0)

        try:
            scrollregion_height=0
            for element in (self.Canvas_topFr.grid_slaves()):
                scrollregion_height+=element.winfo_height()
        except:
            print("fail")




    def create_Widgets(self,font):

        self.botFr = tk.Frame(self)
        self.topFr = tk.Frame(self)

        self.botFr.pack(fill="x",side="bottom")
        self.topFr.pack(fill="both",expand=True)

        self.create_Widgets_topFr(font=font)
        self.create_Widgets_botFr(font=font)

        # botFr



        # Canvas_topFr

        #CanvasFr_topFr = tk.Frame(Canvas_topFr)

        #CanvasFr_topFr
        #Canvas_LF1=tk.LabelFrame(CanvasFr_topFr,text="Suchgebiet (wo wollen sie suchen)")
        #Canvas_LF2=tk.LabelFrame(CanvasFr_topFr,text="Suchkriterien (wie wollen sie suchen)")
        #Canvas_LF3=tk.LabelFrame(CanvasFr_topFr,text="Ergebnissverarbeitung(was wollen sie suchen)")

        #Canvas_LF1.pack(fill="both",expand=True)
        #Canvas_LF2.pack(fill="both",expand=True)
        #Canvas_LF3.pack(fill="both",expand=True)
        # Canvas_LF1

    def create_Widgets_botFr(self,font):
        print("hollas die waldfee")

        botFr_zurück = tk.Button(self.botFr,text="zurück",font=font)
        botFr_weiter = tk.Button(self.botFr,text="weiter",font=font)
        botFr_zurück.pack(side="left",fill="x",expand=True)
        botFr_weiter.pack(side="right",fill="x",expand=True)

    def create_Widgets_topFr(self,font):
        print("startet")
        self.Scrollbar_topFr = tk.Scrollbar(self.topFr,width=17)   #die scrollbar übernimmt die länge vom arbeitsfenster
        self.Canvas_topFr= tk.Canvas(self.topFr,scrollregion=(0,0,0,0))

        self.Scrollbar_topFr.pack(anchor="se",side="right",fill="y")
        self.Canvas_topFr.pack(anchor="ne",fill="both",expand=True,side="right")

        self.Canvas_topFr.config(yscrollcommand=self.Scrollbar_topFr.set)
        self.Scrollbar_topFr.config(command=self.Canvas_topFr.yview)
        print("endet")
        self.create_Widgets_topFr_Canvas(font)

    def create_Widgets_topFr_Canvas(self,font):

        self.Fr1 = tk.Frame(self.Canvas_topFr)
        id=self.Canvas_topFr.create_window(0,0,anchor="nw",height=0,width=0,window=self.Fr1)
        Canvas_LF1=tk.LabelFrame(self.Fr1,height=0,text="Suchgebiet (wo wollen sie suchen)")
        Canvas_LF2=tk.LabelFrame(self.Fr1,text="Suchgebiet (wo wollen sie suchen)")
        Canvas_LF3=tk.LabelFrame(self.Fr1,text="Suchgebiet (wo wollen sie suchen)")
        Canvas_LF1.pack(fill="both",expand=True)
        Canvas_LF2.pack(fill="both",expand=True)
        Canvas_LF3.pack(fill="both",expand=True)
        print("buxdehude")
        print(Canvas_LF1.winfo_height())

        b1=tk.Button(Canvas_LF1,text="Hallloooo")
        b1.pack()
        print(Canvas_LF1.winfo_height())

        b1=tk.Button(Canvas_LF2,text="Hallloooo")
        b1.pack()
        print(Canvas_LF1.winfo_height())

        b1=tk.Button(Canvas_LF3,text="Hallloooo")
        b1.pack()
        print(Canvas_LF1.winfo_height())


    # Canvas_LF2



        # Canvas_LF3



        #id=Canvas_topFr.create_window(0,0,anchor="nw",width=0,height=0,window=CanvasFr_topFr)

        start=True

        def config_handler(event,self=self,start=start):
            return self.__fenstergröße_event(event,start)

        #self.bind('<Configure>',config_handler)



def example():
    app = Application(font=('Times', '-20'))
    app.master.title('Sample application')
    app.mainloop()

if __name__ == "__main__":
    example()
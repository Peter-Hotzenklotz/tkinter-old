# This Python file uses the following encoding: utf-8

"""@HG Datei genutzt um nochmal einen überblick über die richtigenutzun von
Klassen und Events in tkinter zu bekommen."""


import tkinter as tk


__all__ = ['multi argument trick testing.py']


class Application(tk.Frame):
    def __init__(self, master=None,liste=[]):
        self.liste=liste

        tk.Frame.__init__(self, master)
        self.pack(fill="both",expand=True)
        self.__createWidgets(liste=self.liste)

    def __createWidgets(self,liste):
        self.cbList = [] # Create the checkbutton list

        i=0
        for wort in liste:
            cb_variable= tk.StringVar()
            cb = tk.Entry(self,textvariable=cb_variable)
            cb_variable.set(wort)

            self.cbList.append(cb)
            cb.pack(fill="both",expand=True)
            bg_state=cb.cget("bg")

            def handler(event, self=self, i=i,bg_state=bg_state):
                event.a=tk.StringVar()
                print(event)
                (self.cbList[i])["textvariable"]=event.a
                #return self.__cbHandler(event, i,bg_state)

            def handler_2(event,self=self,i=i):
                return self.__event_2(event,cbNumber=i)



            cb.bind('<FocusIn>', handler)
            cb.bind("<FocusOut>",handler_2)
            i+=1
        self.quitButton = tk.Button(self, text='infos',
                                    command=self.infos)
        self.quitButton.pack(fill="x")

    def __event_2(self,event,cbNumber):
        print(event)
        c=(self.cbList[cbNumber]).get()
        print("c=",c)

    def __cbHandler(self, event, cbNumber,bg_state):
        print(cbNumber)
        #(self.cbList[cbNumber])["text"]=self.liste[cbNumber]
        print(bg_state)

        #c=(self.cbList[cbNumber]).get()
        #print("c=",c)

        a=(self.cbList[cbNumber])["bg"]

        print(a)
        if a != "red":
            (self.cbList[cbNumber])["bg"]="red"
        else:
            (self.cbList[cbNumber])["bg"]=bg_state


    def infos(self):
        print("funkt")
        print(str(self.cbList[0]))
        (self.cbList[0])["text"]="oppps"
        (self.cbList[1])["bg"]="red"



def example(liste=[]):
    app = Application(liste=liste)
    app.master.title('Sample application')
    app.mainloop()

if __name__ == "__main__":
    example(liste= [".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben",
                    "Faust.","ostern.","J.R.R.Martin","essen","Fussall"])

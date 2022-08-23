# This Python file uses the following encoding: utf-8

import tkinter as tk

# leider kommt man hiermiet auch nicht um das jeweilige definieren von mehreren etrys drum herum. Schade.

__all__ = ['Vorlage tkinter_the_extra_argument_trick_angepasst.py']

liste=["Haus","klaus","raus"]

class Application(tk.Frame):
    def __init__(self, master=None,liste=liste):
        tk.Frame.__init__(self, master)
        self.grid(sticky=tk.N+tk.S+tk.W+tk.E)
        #self.createWidgets()
        self.__createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()


    def __createWidgets(self):
        self.cbList = [] # Create the checkbutton list
        i=0
        for wort in liste:
            cb_var=tk.StringVar()
            cb = tk.Entry(self,textvariable=cb_var)
            cb_var.set(wort)

            self.cbList.append(cb)
            cb.grid( row=i, column=0,sticky=tk.N+tk.S+tk.W+tk.E)
            def handler(event, self=self, i=i):
                #cb_var.set(str(i))
                return self.__cbHandler(event, i)
            cb.bind('<Button-1>', handler)
            i+=1

    def __cbHandler(self, event, cbNumber):
        print(event)
        print(cbNumber)
        #print(str(cb_var))
        #print("d=",d)
        #e= self.focus_get()
        #print("e=",str(e))
        #e["textvariable"]="etextetext"

def example():
    app = Application(liste=liste)
    app.master.title('Sample application')
    app.mainloop()

if __name__ == "__main__":
    example()
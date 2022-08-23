# This Python file uses the following encoding: utf-8

import tkinter as tk


__all__ = ['Vorlage tkinter_the_extra_argument_trick.py']


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        #self.createWidgets()
        self.__createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()


    def __createWidgets(self):
        self.cbList = [] # Create the checkbutton list
        for i in range(10):
            cb = tk.Checkbutton(self)
            self.cbList.append(cb)
            cb.grid( row=1, column=i)
            def handler(event, self=self, i=i):
                return self.__cbHandler(event, i)
            cb.bind('<Button-1>', handler)

    def __cbHandler(self, event, cbNumber):
        print(event)
        print(cbNumber)


def example():
    app = Application()
    app.master.title('Sample application')
    app.mainloop()

if __name__ == "__main__":
    example()
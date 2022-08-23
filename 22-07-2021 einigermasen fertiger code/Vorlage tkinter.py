# This Python file uses the following encoding: utf-8

import tkinter as tk


__all__ = ['Vorlage tkinter.py']


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',
                                    command=self.quit)
        self.quitButton.grid()



def example():
    app = Application()
    app.master.title('Sample application')
    app.mainloop()

if __name__ == "__main__":
    example()
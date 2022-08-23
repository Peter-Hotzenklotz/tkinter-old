# This Python file uses the following encoding: utf-8

import tkinter as tk

#aus irgendeinem Grund kann ich diesen Code nicht starten bzw er führt nichs aus.
__all__ = ['Sortierlisten_erstellen.py']


class Application(tk.Frame):
    def __init__(self, master=None,liste=[],parameterliste=[],beschreibung=""):
        #import schreibe_buttons5eventhandling
        self.liste = liste
        self.parameterliste = parameterliste
        self.ursprung_parameterliste = parameterliste

        self.beschreibung = beschreibung

        self.scrollregion_height=0

        for element in parameterliste:
            self.ursprung_parameterliste.append(element)

        tk.Frame.__init__(self, master)
        self.pack(fill="both",expand=True)


        #self.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
        #self.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)


        self.__createWidgets(liste=self.liste)


    def __createWidgets(self,liste):

        #self.Top_Frame = tk.Frame(self,height=0,width=0,takefocus=0)
        #self.Top_Frame.pack(side="top",anchor="n",expand=False,fill="both")

        #self.Arbeits_Fenster = tk.Frame(self,width=0,height=0)
        #self.Arbeits_Fenster.pack(fill="both",side="top",anchor="n",expand=True)

        #self.Arbeits_Menu = tk.Frame(self,takefocus=0,width=0,height=0)
        #self.Arbeits_Menu.pack(fill="x",side="bottom",anchor="s",expand=False)

        # Arbeis_Menu

        #self.Arbeits_Menu.Bot_Frame=tk.Frame(self.Arbeits_Menu)
        #self.Arbeits_Menu.Bot_Frame.pack(side="bottom",anchor="n",expand=True,fill="x")



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


    #def infos(self):
    #    pass
    #    """print("funkt")
    #    print(str(self.cbList[0]))
    #    (self.cbList[0])["text"]="oppps"
    #    (self.cbList[1])["bg"]="red"""

    #def fenster_größen_anpassen():
    #    pass
    #    """scrollregion_height2=parameterliste_label.winfo_height()
    #    #scrollbar_top_Frame["scrollregion"]=(0,0,0,parameterliste_label.winfo_height())
    #    canvas_top_frame["scrollregion"]=(0,0,0,scrollregion_height2)"""



def example(liste=[],parameterliste=[],beschreibung=""):
    app = Application(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)
    app.master.title('Sample application')

    print("startet")
    app.mainloop()

if __name__ == "__main__":
    liste= [".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben",
            "Faust.","ostern.","J.R.R.Martin","essen","Fussall"]

    parameterliste=["Nomen","verben","adjektive","Orte","adverben",
                    "buxdehude","Politik","Fenster","Poster"]

    beschreibung= """das ist ein Auswahlmenü zum erstellen der Sortierlisten. Jedes der Liste angehängte Wort ist, ist wie eine Überschrift. Nutze diese Überschrift. Später wird für jede Überschrift eine Liste erstellt. bis jetzt vorhandene listen siehe Parameterliste"""


    example(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)


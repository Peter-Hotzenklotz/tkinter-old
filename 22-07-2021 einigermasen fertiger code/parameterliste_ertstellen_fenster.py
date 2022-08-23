# This Python file uses the following encoding: utf-8

from tkinter import*


__all__ = ['parameterliste_erstellen_fenster.py']


liste= [".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben",
        "Faust.","ostern.","J.R.R.Martin","essen","Fussall"]

parameterliste=["Nomen","verben","adjektive","Orte","adverben",
                    "buxdehude","Politik","Fenster","Poster"]


beschreibung= """das ist ein Auswahlmenü zum erstellen der Sortierlisten. Jedes der Liste angehängte Wort ist, ist wie eine Überschrift. Nutze diese Überschrift. Später wird für jede Überschrift eine Liste erstellt. bis jetzt vorhandene listen siehe Parameterliste"""


def code_der_in_datei_geschrieben_wird(liste=[],parameterliste=[],beschreibung=beschreibung,minwidth=1000,minhight=500):

    import schreibe_buttons5eventhandling

    ursprüngliche_parameterliste=[]

    for element in parameterliste:
        ursprüngliche_parameterliste.append(element)
    print("ursprüngliche_parameterliste= ",str(ursprüngliche_parameterliste))

    def liste_hinzufuegen_0():   #_0 wird später hochgezählt _h bzw _0 _1 _2 _3 ... korrektur unten entfernt da bereits
                                 # durch das Event gelöst stattdessen dem jeweiligen Button liste_zurücksetzten hinzugefügt.
        a= entry_0.get()
        print(a)
        parameterliste[0]=a
        print(parameterliste)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)

    def liste_hinzufuegen_0_event(event):
        try:
            a= entry_0.get()
            print(a)
            parameterliste[0]=a
            print(parameterliste)
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        except:
            print("fehler, sind sie sicher sie haben den Listeneintrag nicht entfernt")

    def liste_zurücksetzen_0():
        try:
            print("ursprüngliche_parameterliste= " ,str(ursprüngliche_parameterliste))
            variable_0.set(ursprüngliche_parameterliste[0])
            a= entry_0.get()
            print(a)
            parameterliste[0]=a
            print(parameterliste)
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        except:
            print("stellen sie sicher den Listeneintrag nicht komplett entfernt zu haben, wenn dem so ist erneuern sie " \
                  "die gesammte liste")

    def listen_erzeugen():
        pass

    def weiter():
        root.destroy()
        print('parameterliste= ',parameterliste)
        schreibe_buttons5eventhandling.alles(liste=liste, parameterliste=parameterliste)

    def parameterliste_pop():
        nonlocal parameterliste
        try:
            parameterliste.pop()
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        except:
            print("alle Einträge entfernt")
            parameterliste=[]

    def Alt_L_komplette_liste_zurucksetzen(event):
        nonlocal parameterliste
        parameterliste=[]
        for element in ursprüngliche_parameterliste:
            parameterliste.append(element)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)
    # bei dieser funktion gibt es einen mehr oder wniger Bug. Den ich aber nicht finden kann. Wenn man die liste komplett mit
    # del leert und dann erneut und dann wieder komplett lert muss man erst eine andere aktion durchführen um die liste wieder
    # zu leeren.


    def KeyPress_Delete_parameterliste_pop(event):
        nonlocal parameterliste
        try:
            parameterliste.pop()
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
            parameterliste=parameterliste
        except:
            print("alle Einträge entfernt")
            parameterliste=[]



    def parameterliste_append(event):
        b=entry_appending.get()
        parameterliste.append(b)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        variable_appending.set("")

    def fenstergröße():
        a=root.winfo_geometry()
        print("geometry= ",str(a))

        b=root.winfo_width()
        print("width= ",str(b))
        beschreibung_label["wraplength"]=int(b)

    def fenstergröße_event(event):
        #a=root.winfo_geometry()
        #print("geometry= ",str(a))
        b=root.winfo_width()
        #print("width= ",str(b))
        beschreibung_label["wraplength"]=int(b)-20
        parameterliste_label["wraplength"]=int(b)-20
    h=0
    master=Tk()


    master.geometry(str(minwidth)+"x"+str(minhight))
    master.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    master.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)
    master.bind('<Configure>',fenstergröße_event)
    master.title('parameterliste_erstellen_fenster')


    arbeits_fenster=Frame(master)
    arbeits_fenster.pack(fill="both",expand=True)

    arbeits_menü=Frame(master,takefocus=0)
    arbeits_menü.pack(anchor="s",side="bottom",fill="x")

    #arbeits_menü
    zurück_button= Button(arbeits_menü, text="zurück",command=weiter,height="2",font=('Times', '-20'),takefocus=0)
    zurück_button.pack(side="left",fill="x",expand=True)
    weiter_button= Button(arbeits_menü, text="weiter",command=weiter,height="2",font=('Times', '-20'),takefocus=0)
    weiter_button.pack(side="right",fill="x",expand=True)

    #arbeits_fenster
    root=Frame(arbeits_fenster)
    root.pack(anchor="nw",side="left",fill="x",expand=True)

    scrollbar1=Scrollbar(arbeits_fenster)
    scrollbar1.pack(anchor="nw",side="right",fill="y")

    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)



    beschreibung_variable = StringVar()
    beschreibung_variable.set(beschreibung)

    beschreibung_label = Label(root,text="",anchor="w",justify="left",textvariable=beschreibung_variable,wraplength=minwidth,
                               font=('Times', '-20'),pady="20",fg="black")
    beschreibung_label.grid(column=0,row=0,columnspan=2,sticky=N+S+E+W)


    parameterliste_label=Label(root,text="parameterliste= "+str(parameterliste),anchor="w",justify="left",
                               wraplength=minwidth,font=('Times', '-20'),pady="20",fg="black",bg="white")
    parameterliste_label.grid(column=0,row=1,columnspan=2,sticky=N+S+E+W)


    variable_0 = StringVar()
    variable_0.set("klasse")
    entry_0 = Entry(root,textvariable=variable_0,font=('Times', '-20'))
    entry_0.grid(column=0, row=2,sticky=N+S+E+W)
    entry_0.bind('<FocusOut>',liste_hinzufuegen_0_event)



    button_0 = Button(root,text="listeneintrag 1 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_0.grid(column=1, row=2,sticky=N+S+E+W)


    variable_appending = StringVar()
    entry_appending = Entry(root,textvariable=variable_appending,font=('Times', '-20'))
    entry_appending.grid(column=0, row=3,sticky=N+S+E+W)
    entry_appending.bind('<Return>',parameterliste_append)


    button_entf = Button(root,text="entferne letzten listeneintrag (del)",font=('Times', '-20'),command=parameterliste_pop,takefocus=0)
    button_entf.grid(column=1, row=3,sticky=N+S+E+W)

    button_entf = Button(root,text="gibt fenstergröße zurück",font=('Times', '-20'),command=fenstergröße,takefocus=0)
    button_entf.grid(columnspan=2,sticky=N+S+E+W)




    mainloop()

def parameterliste_erstellen(liste=[],parameterliste=[],dateiname="parameterliste_ertstellen.py",beschreibung=beschreibung,minwidth=1000,minhight=500):


    ursprüngliche_parameterliste=[]

    for element in parameterliste:
        ursprüngliche_parameterliste.append(element)

    datei=open(dateiname,"w",encoding="utf-8")
    datei.write(

"""from tkinter import*
import schreibe_buttons5eventhandling

def parameterliste_fenster(liste= """+str(liste)+""", parameterliste="""+str(parameterliste)+",beschreibung='"+str(beschreibung)+"',minwidth ="+str(minwidth)+",minhight ="+str(minhight)+"):")
    h=0


    datei.write('\n\n    ursprüngliche_parameterliste= '+str(ursprüngliche_parameterliste))

    for element in parameterliste:
        datei.write(
    """


    def liste_zurucksetzen_"""+str(h)+"""():
        try:
            variable_"""+str(h)+""".set(ursprüngliche_parameterliste["""+str(h)+"""])
            a= entry_"""+str(h)+""".get()
            # print(a)
            parameterliste["""+str(h)+"""]=a
            # print(parameterliste)
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        except:
            print('fehler: bitte füllen sie die liste wieder mit einträgen oder setzen sie diese mit alt komplett zurück')
        
    def liste_hinzufuegen_"""+str(h)+"""_event(event):
        a= entry_"""+str(h)+""".get()
        # print(a)
        parameterliste["""+str(h)+"""]=a
        # print(parameterliste)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)""")

        h+=1

    datei.write(
    """
    def listen_erzeugen():
        pass

    def weiter():
        root.destroy()
        print('parameterliste= ',parameterliste)
        schreibe_buttons5eventhandling.alles(liste=liste,parameterliste=parameterliste)
        
    def parameterliste_pop():
        nonlocal parameterliste
        try:
            parameterliste.pop()
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        except:
            print("alle Einträge entfernt")
            parameterliste=[]

    def Alt_L_komplette_liste_zurucksetzen(event):
        nonlocal parameterliste
        parameterliste=[]
        for element in ursprüngliche_parameterliste:
            parameterliste.append(element)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)
    # bei dieser funktion gibt es einen mehr oder wniger Bug. Den ich aber nicht finden kann. Wenn man die liste komplett mit
    # del leert und dann erneut und dann wieder komplett lert muss man erst eine andere aktion durchführen um die liste wieder
    # zu leeren.


    def KeyPress_Delete_parameterliste_pop(event):
        nonlocal parameterliste
        try:
            parameterliste.pop()
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)
            parameterliste=parameterliste
        except:
            print("alle Einträge entfernt")
            parameterliste=[]



    def parameterliste_append(event):
        b=entry_appending.get()
        parameterliste.append(b)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)
        variable_appending.set("")

    root=Tk()
    root.title('parameterliste_erstellen_fenster')

    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)
    root.minsize(width=minwidth,height=minhight)
    root.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    root.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)


    beschreibung_label = Label(root,text=beschreibung,anchor="w",justify="left",wraplength=minwidth,
                               font=('Times', '-20'),pady="20",fg="black")
    beschreibung_label.grid(column=0,row=0,columnspan=2,sticky=N+S+E+W)

    parameterliste_label=Label(root,text="parameterliste= "+str(parameterliste),anchor="w",justify="left",
                               wraplength=minwidth,font=('Times', '-20'),pady="20",fg="black",bg="white")
    parameterliste_label.grid(column=0,row=1,columnspan=2,sticky=N+S+E+W)""")

    h=0
    i=0
    for element in parameterliste:
        datei.write(
    """
    variable_"""+str(h)+""" = StringVar()
    variable_"""+str(h)+""".set('"""+str(element)+"""')

    entry_"""+str(h)+""" = Entry(root,textvariable=variable_"""+str(h)+""",font=('Times', '-20'))

    entry_"""+str(h)+""".grid(column=0, row="""+str(i+2)+""",sticky=N+S+E+W)
    entry_"""+str(h)+""".bind('<FocusOut>',liste_hinzufuegen_"""+str(h)+"""_event)


    button_"""+str(h)+""" = Button(root,text='Listeneintrag """+str(h+1)+""" zurücksetzen',font=('Times', '-20'),command=liste_zurucksetzen_"""+str(h)+""",takefocus=0)
    button_"""+str(h)+""".grid(column=1, row="""+str(i+2)+""",sticky=N+S+E+W)""")
        i+=1
        h+=1

    datei.write(
    """
    variable_appending = StringVar()
    entry_appending = Entry(root,textvariable=variable_appending,font=('Times', '-20'))
    entry_appending.grid(column=0, row="""+str(i+2)+""",sticky=N+S+E+W)
    entry_appending.bind('<Return>',parameterliste_append)
    
    button_entf = Button(root,text="entferne letzten listeneintrag (del)",font=('Times', '-20'),command=parameterliste_pop,takefocus=0)
    button_entf.grid(column=1, row="""+str(i+2)+""",sticky=N+S+E+W)
    
    weiter= Button(root, text="weiter",command=weiter,height="3",font=('Times', '-20'),takefocus=0)
    weiter.grid(columnspan=2,sticky=S+E+W)

    mainloop()""")
    datei.close




def example(liste=[],parameterliste=["test"],beschreibung=""):

    parameterliste_erstellen(liste=liste,parameterliste=parameterliste,dateiname="parameterliste_ertstellen.py")
    import parameterliste_ertstellen
    parameterliste_ertstellen.parameterliste_fenster(parameterliste=parameterliste,beschreibung=beschreibung)

if __name__ == "__main__":

    beschreibung="Die Einträge der Parameterliste bilden die Sortierkriterien. Jeder Eintrag ist später eine eigene" \
                 " Liste in die Begriffe einsortiert werden. Um den jeweiligen Listeneintrag der Parameterliste zu ändern, ändern sie das Wort in dem Jeweiligen Eingabefeld." \
                 " Dann verändern sie den Focus bsp. indem sie Tab drücken oder einen Button oder eingabefeld anklicken" \
                 " Um den jeweiligen Listeneintrag zurückzusetzten drücken sie den entprechenden Button." \
                 " Um die komplette liste zurückzusetzen drücken sie Alt." \
                 " Um den letzten eintrag zu entfernen drücken sie die entf taste oder den Button unten rechts" \
                 " Um ein neues Wort der Liste hinzuzufügen schreiben sie diesen in das letzte Eingabefeld (neben den entfernen Button)" \
                 " und drücken sie Enter" \
                 " wichtiger Hinweis: wenn kürzlich die gesamte Liste gelert wurde kann es vorkommen das" \
                 " Befehle nicht beim ersten mal angenommen werden sollte dies der Fall sein drücken sie eine beliebiege" \
                 " Buchstabentaste oder klicken sie auf einen beliebiegen Button/Eingabefeld ."

    parameterliste=["Nomen","verben","adjektive","Orte","adverben","Haus","mmmmmmmmmmmmmmmmmmmmm","nnnnnnnnnnnnnnnnnn",
                    "ooooooooooooooooooooooo","ppppppppppppppppppppppppp","qqqqqqqqqqqqqqqqqqqqqqqq"]


    code_der_in_datei_geschrieben_wird(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung,minwidth=1000,minhight=700)

    #example(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)

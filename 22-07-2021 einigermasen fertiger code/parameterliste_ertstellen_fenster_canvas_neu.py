# This Python file uses the following encoding: utf-8

from tkinter import*


__all__ = ['parameterliste_erstellen_fenster.py']


liste= [".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben",
        "Faust.","ostern.","J.R.R.Martin","essen","Fussall"]

parameterliste=["Nomen","verben","adjektive","Orte","adverben",
                    "buxdehude","Politik","Fenster","Poster"]


beschreibung= """das ist ein Auswahlmenü zum erstellen der Sortierlisten. Jedes der Liste angehängte Wort ist, ist wie eine Überschrift. Nutze diese Überschrift. Später wird für jede Überschrift eine Liste erstellt. bis jetzt vorhandene listen siehe Parameterliste"""


def code_der_in_datei_geschrieben_wird(liste=[],parameterliste=[],beschreibung=beschreibung,minwidth=int,minhight=int):

    import schreibe_buttons5eventhandling

    ursprüngliche_parameterliste=[]
    scrollregion_height=0
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

    def FocusOut_event_0(event,scroll_height):
        # Achtung in die spätere datei wird nicht exakt der selbe code geschrieben dort wird folgender code geschrieben.
        # 1. die bind funktion wird an den jeweiligen button gekoppelt, bedeutet des if scrollbar position[1]<1 entfällt
        # und der code in der if schleife, für alle buttons auser dem letzten verwendet wird.
        # beim letzten wiederrum wird der else: code verwendet.
        # so wird auch der doppel Tab beim letzten Button vermieden.
        """     #try:
        a= entry_0.get()
        print(a)
        parameterliste[0]=a
        print(parameterliste)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)

        button_höhe= button_0.winfo_height()
        canvas_höhe= canvas_test.winfo_height()

        parameterliste_label_höhe= parameterliste_label.winfo_height()
        beschreibung_label_höhe= beschreibung_label.winfo_height()

        aaa=(canvas_höhe-parameterliste_label_höhe-beschreibung_label_höhe)/anzahl_buttons

        frame_höhe=root.winfo_height()

        print("frame_höhe",frame_höhe)

        print("button_höhe=",button_höhe)
        print("aaa=",aaa)

        scrollbar_position=scrollbar1.get()
        xx=scrollbar_position[0]
        z= xx+scroll_height
        print("z=",z)
        print("xx=",xx)
        canvas_test.yview_moveto(z)
        scrollbar_position=scrollbar1.get()
        print("scrollbar_position=", scrollbar_position)"""

        scrollbar_position=scrollbar1.get()

        tab_scroll=scrollbar_position[0]+button_0.winfo_height()/scrollregion_height
        print("tab_scroll=",tab_scroll)

        if scrollbar_position[1] <1:
            canvas_test.yview_moveto(tab_scroll)
            scrollbar_position=scrollbar1.get()
            print("scrollbar_position=", scrollbar1.get())
        else:
            Button_0_y_position = button_0.winfo_pointery()
            print("else")
            print("scrollregion_height=",scrollregion_height)
            #print("Button_0_y_position=",Button_0_y_position)
            #print("Button_0_y_position/scrollregion_height=",Button_0_y_position/scrollregion_height)

            neue_position_höhe=parameterliste_label.winfo_height() + beschreibung_label.winfo_height()

            neue_scrollpunkt=neue_position_höhe/scrollregion_height

            print("neu_scrollpunkt=",neue_scrollpunkt)
            canvas_test.yview_moveto(neue_scrollpunkt)  # in dem write programm ist diese position an den button selbst gekoppelt so das
            # der sprung an der richtigen stelle landet und nicht erst noch der minimale rest gefüllt werden muss.

            print("scrollbar_position=", scrollbar1.get())

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


    def zurück():
        scrollbar_position=scrollbar1.get()
        print("scrollbar_position=", scrollbar_position)
        print("scroll_height=",scroll_height)
        #print("entry_0.winfo_pixels() =",entry_0.winfo_pixels(number)
        print("fraktion=(y=entry_0.winfo_y())",scrollbar1.fraction(x=0,y=entry_0.winfo_y()))
        print("entry_0.winfo_pointery()=",entry_0.winfo_pointery())
        print("fraktion=,scrollbar1.fraction(x=0,y=",entry_0.winfo_pointery(),"))",scrollbar1.fraction(x=0,y=entry_0.winfo_pointery()))
        print("entry_0.winfo_y()=",entry_0.winfo_y())

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
        a=master.winfo_geometry()
        print("geometry= ",str(a))

        b=master.winfo_width()
        print("width= ",str(b))
        beschreibung_label["wraplength"]=int(b)

    def fenstergröße_event(event,fenster_construiert3):
        #a=root.winfo_geometry()
        #print("geometry= ",str(a))
        #b=arbeits_fenster.winfo_width()
        #print("width= ",str(b))
        nonlocal scroll_height
        nonlocal fenster_construiert
        nonlocal scrollregion_height
        fenster_construiert2=fenster_construiert3
        c=canvas_test.winfo_width()
        d=master.winfo_height()
        e=root.winfo_geometry()

        beschreibung_label["wraplength"]=c
        parameterliste_label["wraplength"]=c

        #if start is True:
            #canvas_test.itemconfigure(id,width=c)

        f=beschreibung_label.winfo_height()

        g=button_0.winfo_height()
        # h=entry_0.winfo_height()

        # i=button_1.winfo_height()
        # j=entry_1.winfo_height()
        k=parameterliste_label.winfo_height()

        #print("canvas_width=",c)
        #print("master_height=",d)
        #print("root geometry=",e)

        #print("beschreibung_label=",f)
        #print("button_0=",g)
        # print("entry_0=",h)
        # print("button_1=",i)
        # print("entry_1=",j)
        #print("parameterliste_label=",k)

        #print("anzahl_buttons= ",anzahl_buttons)

        scrollregion_height= beschreibung_label.winfo_height() + anzahl_buttons * button_0.winfo_height() + parameterliste_label.winfo_height()
        #scrollregion_height2=anzahl_buttons*int(g)

        #print("scrollregion_height2= ", scrollregion_height2)
        #print("scrollregion_height= ", scrollregion_height)


        canvas_test["scrollregion"]=(0,0,0,scrollregion_height)


        if fenster_construiert2 is True:
            g=button_0.winfo_height()
            z=g/canvas_test.winfo_height()
            scroll_height=z
            fenster_construiert2=False
            #print("fenster construiert if bedigung durchlaufen")
            #print("c=",canvas_test.winfo_height())

        def test_ob_global_richtig():
            print("scroll_height=",scroll_height)
        #test_ob_global_richtig()
        print("scrollregion_height=",str(scrollregion_height))


    info_event_liste=[]

    def info_event(event):
        scrollbar_position=scrollbar1.get()
        scrollbar_geometry=scrollbar1.winfo_geometry()  # 17x639+983+0   bzw.  17,  y-koordinate, x-koordinate

        master_geometry=master.winfo_geometry()
        arbeits_fenster_geometry=arbeits_fenster.winfo_geometry()
        arbeits_menü_geometry=arbeits_menü.winfo_geometry()
        root_geometry=root.winfo_geometry()

        print("scrollregion_height=",str(scrollregion_height))

        print("master_geometry=",master.winfo_geometry())
        print("...")
        print("arbeits_fenster_geometry=",arbeits_fenster.winfo_geometry()) # wisth x height + x + y
        print("...")

        print("arbeits_menü_geometry=",arbeits_menü.winfo_geometry())   #
        print("...")

        print("root_geometry=",root.winfo_geometry())
        print("...")

        print("scrollbar_position=", scrollbar_position)
        print("...")

        print("scrollbar_geometry=",scrollbar_geometry)
        print("scrollbar1.winfo_children()=",scrollbar1.winfo_children())
        print("...")

        print("button_0.winfo_geometry()=",button_0.winfo_geometry())


        zzz= button_0.winfo_height()/scrollregion_height
        print("zzz=",zzz)

        scrollbar_position=scrollbar1.get()

        tab_scroll=scrollbar_position[0]+button_0.winfo_height()/scrollregion_height
        print("tab_scroll=",tab_scroll)

        if scrollbar_position[1] <1:
            canvas_test.yview_moveto(tab_scroll)
            scrollbar_position=scrollbar1.get()
            print("scrollbar_position=", scrollbar1.get())
        else:
            Button_0_y_position = button_0.winfo_pointery()
            print("else")
            print("scrollregion_height=",scrollregion_height)
            #print("Button_0_y_position=",Button_0_y_position)
            #print("Button_0_y_position/scrollregion_height=",Button_0_y_position/scrollregion_height)

            neue_position_höhe=parameterliste_label.winfo_height() + beschreibung_label.winfo_height()

            neue_scrollpunkt=neue_position_höhe/scrollregion_height

            print("neu_scrollpunkt=",neue_scrollpunkt)
            canvas_test.yview_moveto(neue_scrollpunkt)  # in dem write programm ist diese position an den button selbst gekoppelt so das
            # der sprung an der richtigen stelle landet und nicht erst noch der minimale rest gefüllt werden muss.

            print("scrollbar_position=", scrollbar1.get())


        # print("scroll_height=",scroll_height)
        # print("entry_0.winfo_pixels() =",entry_0.winfo_pixels(number)
        # print("fraktion=(y=entry_0.winfo_y())",scrollbar1.fraction(x=0,y=entry_0.winfo_y()))
        # print("entry_0.winfo_pointery()=",entry_0.winfo_pointery())
        # print("fraktion=,scrollbar1.fraction(x=0,y=",entry_0.winfo_pointery(),"))",scrollbar1.fraction(x=0,y=entry_0.winfo_pointery()))
        # print("entry_0.winfo_y()=",entry_0.winfo_y())


    fenster_construiert=False
    scroll_height=0
    h=0
    master=Tk()


    master.geometry(str(minwidth)+"x"+str(minhight))
    master.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    master.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)
    master.bind('<KeyPress-i>',info_event)

    def multi_argument_trick_fenstergröße_event(event):
        nonlocal fenster_construiert
        fenster_construiert3=fenster_construiert
        #print("fenster_construiert3",fenster_construiert3)
        return fenstergröße_event(event,fenster_construiert3)


    master.bind('<Configure>',multi_argument_trick_fenstergröße_event)
    master.title('parameterliste_erstellen_fenster')
    master.minsize(width=520,height=330)    # bei einer kleineren größe bugt die GUI buttons verschwinden

    arbeits_fenster=Frame(master)
    arbeits_fenster.pack(fill="both",expand=True,side="top",anchor="nw")

    arbeits_menü = Frame(master,takefocus=0)
    arbeits_menü.pack(fill="x",side="bottom",anchor="nw")

    #arbeits_menü
    zurück_button = Button(arbeits_menü, text="zurück",command=zurück,height="2",font=('Times', '-20'),takefocus=0)
    zurück_button.pack(side="left",fill="x",expand=True)
    weiter_button = Button(arbeits_menü, text="weiter",command=weiter,height="2",font=('Times', '-20'),takefocus=0)
    weiter_button.pack(side="right",fill="x",expand=True)

    i=10
    #arbeits_fenster
    canvas_test= Canvas(arbeits_fenster,scrollregion=(0,0,0,0))
    canvas_test.pack(anchor="nw",fill="both",expand=True,side="left")

    scrollbar1=Scrollbar(arbeits_fenster)   #die scrollbar übernimmt die länge vom arbeitsfenster
    scrollbar1.pack(anchor="ne",side="right",fill="y")

    canvas_test.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=canvas_test.yview)


    root=Frame(arbeits_fenster)
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


    anzahl_buttons=0


    def multi_argument_trick_FocusOut(event):
        print("scroll_height=", scroll_height)
        return FocusOut_event_0(event,scroll_height)

    variable_0 = StringVar()
    variable_0.set("klasse")
    entry_0 = Entry(root,textvariable=variable_0,font=('Times', '-20'))
    entry_0.grid(column=0, row=2,sticky=N+S+E+W)
    entry_0.bind('<FocusOut>',multi_argument_trick_FocusOut)

    button_0 = Button(root,text="listeneintrag 1 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_0.grid(column=1, row=2,sticky=N+S+E+W)

    anzahl_buttons+=1

    entry_1=Entry(root,font=('Times', '-20'))
    entry_1.grid(column=0,row=3,sticky=N+S+E+W)

    button_1 = Button(root,text="listeneintrag 2 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_1.grid(column=1, row=3,sticky=N+S+E+W)

    anzahl_buttons+=1

    entry_2=Entry(root,font=('Times', '-20'))
    entry_2.grid(column=0,row=4,sticky=N+S+E+W)

    button_2 = Button(root,text="listeneintrag 3 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_2.grid(column=1, row=4,sticky=N+S+E+W)

    anzahl_buttons+=1


    entry_3=Entry(root,font=('Times', '-20'))
    entry_3.grid(column=0,row=5,sticky=N+S+E+W)

    button_3 = Button(root,text="listeneintrag 4 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_3.grid(column=1, row=5,sticky=N+S+E+W)

    anzahl_buttons+=1


    entry_4=Entry(root,font=('Times', '-20'))
    entry_4.grid(column=0,row=6,sticky=N+S+E+W)

    button_4 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_4.grid(column=1, row=6,sticky=N+S+E+W)

    anzahl_buttons+=1

    i=7

    entry_4=Entry(root,font=('Times', '-20'))
    entry_4.grid(column=0,row=i,sticky=N+S+E+W)

    button_4 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_4.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1

    i+=1

    entry_6=Entry(root,font=('Times', '-20'))
    entry_6.grid(column=0,row=i,sticky=N+S+E+W)

    button_6 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_6.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1

    i+=1

    entry_4=Entry(root,font=('Times', '-20'))
    entry_4.grid(column=0,row=i,sticky=N+S+E+W)

    button_4 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_4.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1

    i+=1

    entry_4=Entry(root,font=('Times', '-20'))
    entry_4.grid(column=0,row=i,sticky=N+S+E+W)

    button_4 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_4.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1

    i+=1

    entry_4=Entry(root,font=('Times', '-20'))
    entry_4.grid(column=0,row=i,sticky=N+S+E+W)

    button_4 = Button(root,text="listeneintrag 5 zurücksetzen",font=('Times', '-20'),command=liste_zurücksetzen_0,takefocus=0)
    button_4.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1

    i+=1




    variable_appending = StringVar()
    entry_appending = Entry(root,textvariable=variable_appending,font=('Times', '-20'))
    entry_appending.grid(column=0, row=i,sticky=N+S+E+W)
    entry_appending.bind('<Return>',parameterliste_append)

    button_entf = Button(root,text="entferne letzten listeneintrag (del)",font=('Times', '-20'),command=parameterliste_pop,takefocus=0)
    button_entf.grid(column=1, row=i,sticky=N+S+E+W)

    anzahl_buttons+=1



    # scrollregion_height=anzahl_buttons

    id=canvas_test.create_window(0,0,anchor="nw",width=0,height=0,window=root)


    print("button_0 "+str(button_0.winfo_height()))
    start=True
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
    def back():
        pass


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


    #code_der_in_datei_geschrieben_wird(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung,minwidth=1000,minhight=700)

    example(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)

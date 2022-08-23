# This Python file uses the following encoding: utf-8

from tkinter import*


__all__ = ['parameterliste_ertstellen_fenster_canvas_neu_neu_2.py']


liste= [".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben",
        "Faust.","ostern.","J.R.R.Martin","essen","Fussall"]

parameterliste=["Nomen","verben","adjektive","Orte","adverben",
                    "buxdehude","Politik","Fenster","Poster"]


beschreibung= """das ist ein Auswahlmenü zum erstellen der Sortierlisten. Jedes der Liste angehängte Wort ist, ist wie eine Überschrift. Nutze diese Überschrift. Später wird für jede Überschrift eine Liste erstellt. bis jetzt vorhandene listen siehe Parameterliste"""


def code_der_in_datei_geschrieben_wird(liste=[],parameterliste=[],beschreibung=beschreibung,minwidth=int,minhight=int,
                                       elemente_welche_bei_Tab_scrolling_übersprungen_werden=["Label"],
                                       elemente_welche_bei_berechnung_der_scrollhöhe_übersprungen_werden=["Button"],
                                       as_textfeld=False):

    import schreibe_buttons5eventhandling

    ursprüngliche_parameterliste=[]
    scrollregion_height=0
    for element in parameterliste:
        ursprüngliche_parameterliste.append(element)
    print("ursprüngliche_parameterliste= ",str(ursprüngliche_parameterliste))


    def Tab_event(event,scroll_height):
        scrollbar_position=scrollbar1.get()

        tab_scroll=scrollbar_position[0]+button.winfo_height()/scrollregion_height
        print("tab_scroll=",tab_scroll)
        canvas_test.yview_moveto(tab_scroll)
        print("scrollbar_position=", scrollbar1.get())

    def Tab_event_1(event,scroll_height):

        neue_position_höhe2=0

        for element in (root.winfo_children()):
            if (str(element.winfo_class())) in elemente_welche_bei_Tab_scrolling_übersprungen_werden:
                neue_position_höhe2+=element.winfo_height()
        print("neue_position_höhe2=",neue_position_höhe2)

        neue_scrollpunkt=neue_position_höhe2/scrollregion_height

        print("neu_scrollpunkt=",neue_scrollpunkt)
        canvas_test.yview_moveto(neue_scrollpunkt)  # in dem write programm ist diese position an den button selbst gekoppelt so das
        # der sprung an der richtigen stelle landet und nicht erst noch der minimale rest gefüllt werden muss.

        print("scrollbar_position=", scrollbar1.get())


    def zurück():
        scrollbar_position=scrollbar1.get()
        print("scrollbar_position=", scrollbar_position)
        print("scroll_height=",scroll_height)
        #print("entry.winfo_pixels() =",entry.winfo_pixels(number)
        print("fraktion=(y=entry.winfo_y())",scrollbar1.fraction(x=0,y=entry.winfo_y()))
        print("entry.winfo_pointery()=",entry.winfo_pointery())
        print("fraktion=,scrollbar1.fraction(x=0,y=",entry.winfo_pointery(),"))",scrollbar1.fraction(x=0,y=entry.winfo_pointery()))
        print("entry.winfo_y()=",entry.winfo_y())

    def weiter():
        master.destroy()
        print('parameterliste= ',parameterliste)
        schreibe_buttons5eventhandling.alles(liste=liste, parameterliste=parameterliste)

    def parameterliste_pop():
        nonlocal parameterliste
        try:
            parameterliste.pop()
            parameterliste_label.delete("1.0",'end')
            parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))
        except:
            print("alle Einträge entfernt")
            parameterliste=[]

    def Alt_L_komplette_liste_zurucksetzen(event):
        nonlocal parameterliste
        parameterliste=[]
        i=0
        for element in ursprüngliche_parameterliste:
            parameterliste.append(element)
            FocusIn_handler(event=event,i=i)
            entryList[i].grid()
            buttonList[i].grid()
            i+=1

        parameterliste_label.delete("1.0",'end')
        parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))

    # bei dieser funktion gibt es einen mehr oder wniger Bug. Den ich aber nicht finden kann. Wenn man die liste komplett mit
    # del leert und dann erneut und dann wieder komplett lert muss man erst eine andere aktion durchführen um die liste wieder
    # zu leeren.


    def KeyPress_Delete_parameterliste_pop(event):
        nonlocal parameterliste

        try:
            parameterliste.pop()
            parameterliste_label.delete("1.0",'end')
            parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))
            parameterliste=parameterliste

            a=len(parameterliste)
            #print("len parameterliste=",a)
            #print(len(entryList))
            entryList[a].grid_remove()  #eigentlich wäre es ja a-1 aber da die liste vorher schon um eins reduziert wurde ist es nicht mehr nötig
            buttonList[a].grid_remove()

        #canvas_test["scrollregion"]=(0,0,0,scrollregion_height)

            #entry_grid_infoList[a]
            #button_grid_infoList[a]

        except:
            print("alle Einträge entfernt")
            #parameterliste=[]



    def parameterliste_append(event):
        b=entry_appending.get()
        if b != "":
            parameterliste.append(b)
            parameterliste_label.delete("1.0",'end')
            parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))
            variable_appending.set("")
        #print(parameterliste_label.winfo_height())
        #canvas_top_frame["scrollregion"]=(0,0,0,parameterliste_label.winfo_height())   #größe wird nicht erhöht


    def fenstergröße():
        a=master.winfo_geometry()
        print("geometry= ",str(a))

        b=master.winfo_width()
        print("width= ",str(b))
        beschreibung_label["wraplength"]=int(b)

    start=False
    scroll_height=0

    def fenstergröße_event(event,fenster_construiert3):
        #a=root.winfo_geometry()
        #print("geometry= ",str(a))
        #b=arbeits_fenster.winfo_width()
        #print("width= ",str(b))
        #nonlocal scroll_height
        nonlocal fenster_construiert
        nonlocal scrollregion_height
        nonlocal scroll_height
        fenster_construiert2=fenster_construiert3
        #c=canvas_test.winfo_width()
        #d=master.winfo_height()
        #e=root.winfo_geometry()


        #parameterliste_label.insert("1.0","hallo Welt ")
        #beschreibung_label["wraplength"]=c
        #parameterliste_label["wraplength"]=c

        if start is True:
            canvas_test.itemconfigure(id,width=canvas_test.winfo_width())

        #f=beschreibung_label.winfo_height()

        #g=button.winfo_height()
        # h=entry.winfo_height()

        # i=button_1.winfo_height()
        # j=entry_1.winfo_height()
        #k=parameterliste_label.winfo_height()

        #print("canvas_width=",c)
        #print("master_height=",d)
        #print("root geometry=",e)

        #print("beschreibung_label=",f)
        #print("button=",g)
        # print("entry=",h)
        # print("button_1=",i)
        # print("entry_1=",j)
        #print("parameterliste_label=",k)

        #print("anzahl_buttons= ",anzahl_buttons)

        #scrollregion_height_3= beschreibung_label.winfo_height() + len(buttonList) * button.winfo_height() + parameterliste_label.winfo_height()
        try:
            #print("window constructed")
            scrollregion_height=0
            for element in (root.grid_slaves()):
                if (str(element.winfo_class())) not in elemente_welche_bei_berechnung_der_scrollhöhe_übersprungen_werden:
                    scrollregion_height+=element.winfo_height()

            # aufpassen was wenn entry höhen mitgenommen werden

            #print("scrollregion_height=",scrollregion_height)
            #print("entry_height=",entry.winfo_height())
            #print("button=",button.winfo_height())
            #scrollregion_height2=anzahl_buttons*int(g)

            #print("scrollregion_height2= ", scrollregion_height2)
            #print("scrollregion_height= ", scrollregion_height)


            canvas_test["scrollregion"]=(0,0,0,scrollregion_height)
            #fenster_größen_anpassen()

            #print("fenster_construiert=",fenster_construiert2)

            scroll_height = button.winfo_height() / canvas_test.winfo_height()
        except:
            print("window not constructed.")
        # print("scrollregion_height=",str(scrollregion_height))


    info_event_liste=[]

    def info_event(event):

        print("scrollbar1.winfo_children()=",scrollbar1.winfo_children())
        print("root.winfo_children()=",str(root.winfo_children()))
        for element in (root.winfo_children()):
            #print("element=",element)
            #print("element_class=",element.winfo_class())
            if (str(element.winfo_class())) == "Label":
                print("element=",element)
                print("element_class=",element.winfo_class())
                print("element_height=",element.winfo_height())

    fenster_construiert=False
    h=0
    master=Tk()


    master.geometry(str(minwidth)+"x"+str(minhight))
    master.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    master.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)
    master.bind('<KeyPress-i>',info_event)

    def multi_argument_trick_fenstergröße_event(event,fenster_construiert=fenster_construiert):
        return fenstergröße_event(event,fenster_construiert)
        # eigentlich nicht nötig aber das wieder zu entfernen ist mehr arbeit als es einzubauen.

    master.bind('<Configure>',multi_argument_trick_fenstergröße_event)
    master.title('parameterliste_erstellen_fenster')

    master2=PanedWindow(master,orient=VERTICAL)
    master2.pack(fill="both",expand=True)

    arbeits_menü = Frame(master2,takefocus=0,width=0,height=0)
    #arbeits_menü.pack(fill="x",side="bottom",anchor="s",expand=False)


    top_frame=Frame(master2,height=0,width=0,takefocus=0)
    #top_frame.pack(side="top",anchor="n",expand=False,fill="both")

    arbeits_fenster=Frame(master2,width=0,height=0)
    #arbeits_fenster.pack(fill="both",side="top",anchor="n",expand=True)

    master2.add(top_frame,sticky=N,width=10000)

    master2.add(arbeits_fenster,sticky=NSEW,width=10000)
    #master2.add(arbeits_menü,after=arbeits_fenster,width=10000)


    #bot_frame=Frame(arbeits_menü)
    #bot_frame.pack(side="bottom",anchor="n",expand=True,fill="x")


    def info_event2(event):
        print(fenster_construiert)
        print("scrollhöhe=",scroll_height)

    master.bind('<KeyPress-Control_L>',info_event2)

    scrollbar_top_Frame=Scrollbar(top_frame,width=17)   #die scrollbar übernimmt die länge vom arbeitsfenster
    scrollbar_top_Frame.pack(anchor="se",side="right",fill="y")

    parameterliste_label=Text(top_frame,height=3,bg="#eeeeee",font=('Times', '-20'),wrap=WORD,takefocus=0)

    parameterliste_label.pack(anchor="se",fill="x",expand=True,side="left")
    parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))

    parameterliste_label.config(yscrollcommand=scrollbar_top_Frame.set)
    scrollbar_top_Frame.config(command=parameterliste_label.yview)

    zurück_button = Button(arbeits_menü, text="zurück",command=zurück,height="1",font=('Times', '-20'),takefocus=0)
    zurück_button.pack(side="left",fill="x",expand=True)


    weiter_button = Button(arbeits_menü, text="weiter",command=weiter,height="1",font=('Times', '-20'),takefocus=0)
    weiter_button.pack(side="right",fill="x",expand=True)

    i=10
    #arbeits_fenster

    scrollbar1=Scrollbar(arbeits_fenster,width=19)   #die scrollbar übernimmt die länge vom arbeitsfenster
    scrollbar1.pack(anchor="ne",side="right",fill="y")

    canvas_test= Canvas(arbeits_fenster,scrollregion=(0,0,0,0))
    canvas_test.pack(anchor="ne",fill="both",expand=True,side="right")



    canvas_test.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=canvas_test.yview)


    root=Frame(arbeits_fenster)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    beschreibung_variable = StringVar()
    beschreibung_variable.set(beschreibung)

    beschreibung_label = Label(root,text="",anchor="w",justify="left",textvariable=beschreibung_variable,wraplength=minwidth,
                               font=('Times', '-20'),pady="20",fg="black",bg="white")
    beschreibung_label.grid(column=0,row=0,columnspan=2,sticky=E+W)




    # ursprüngliche_parameterliste
    parameterliste_label_2=Label(root,text="ursprüngliche_parameterliste= "+str(parameterliste),anchor="w",justify="left",
                               wraplength=minwidth,font=('Times', '-20'),pady="20",fg="black",bg="white")
    parameterliste_label_2.grid(column=0,row=1,columnspan=2,sticky=E+W)


    anzahl_buttons=0


    def multi_argument_trick_Tab_event(event,scroll_height=scroll_height):
        print("scroll_height=", scroll_height)
        return Tab_event(event,scroll_height)

    def multi_argument_trick_Tab_event_1(event,scroll_height=scroll_height):
        print("scroll_height=", scroll_height)
        print("multi_argument_trick_Tab_event_1",scroll_height)
        return Tab_event_1(event,scroll_height)

    entryList = []
    buttonList= []
    entry_textvarList= []
    entry_event_textVarlist= []
    entry_grid_infoList=[]
    button_grid_infoList=[]
    h=0
    i=0
    for wort in parameterliste:

        entry_variable = StringVar()
        entry_variable.set(wort)
        entry = Entry(root,textvariable=entry_variable,font=('Times', '-20'))

        entry_textvarList.append(entry_variable)
        entryList.append(entry)

        entry.grid(column=0, row=i+2,sticky=N+S+E+W)
        entry_grid_infoList.append(entry.grid_info())

        def FocusIn_handler(event,i=i):
            event.a=StringVar()
            event.a.set(parameterliste[i])
            (entryList[i])["textvariable"]=event.a


        def FocusOut_handler(event,i=i):

            try:
                parameterliste[i]=entryList[i].get()
                parameterliste_label.delete("1.0",'end')
                parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))
            except:
                print("fehler oder ist die liste leer?")

        entry.bind('<FocusIn>',FocusIn_handler)
        entry.bind('<FocusOut>',FocusOut_handler)
        entry.bind('<KeyPress-Return>',FocusOut_handler)
        entry.bind('<KeyPress - Tab>',multi_argument_trick_Tab_event)

        def liste_zurücksetzen(event,i=i):
            parameterliste[i]=ursprüngliche_parameterliste[i]
            parameterliste_label.delete("1.0",'end')
            parameterliste_label.insert("1.0","parameterliste = "+str(parameterliste))

            #parameterliste_label["text"]="parameterliste = "+str(parameterliste)
            FocusIn_handler(event=event,i=i)



        button_text = "listeneintrag "+str(i)+" zurücksetzen"
        button = Button(root, text=button_text, font=('Times', '-20'), takefocus=0)
        buttonList.append(button)
        button.grid(column=1, row=i+2,sticky=N+S+E+W)
        button_grid_infoList.append(button.grid_info())
        button.bind('<Button>',liste_zurücksetzen)

        i += 1
        # anzahl_buttons+=1

    def __entry_event(event,entryNumber=i):
        pass

    variable_appending = StringVar()
    entry_appending = Entry(root,textvariable=variable_appending,font=('Times', '-20'))
    entry_appending.grid(column=0, row=i+2,sticky=N+S+E+W)
    entry_appending.bind('<Return>',parameterliste_append)
    entry_appending.bind('<KeyPress - Tab>',multi_argument_trick_Tab_event_1)

    button_entf = Button(root,text="entferne letzten listeneintrag (del)",font=('Times', '-20'),takefocus=0)
    button_entf.grid(column=1, row=i+2,sticky=N+S+E+W)
    button_entf.bind('<Button-1>',KeyPress_Delete_parameterliste_pop)

    anzahl_buttons+=1



    # scrollregion_height=anzahl_buttons

    id=canvas_test.create_window(0,0,anchor="nw",width=0,height=0,window=root)


    def mouse_whell_event(event):
        #print(str(event.delta))
        #print(scrollbar1.delta(0,-event.delta))
        #print(scrollbar1.get())
        #print(event.x,"=x")


        #mausposition= (event.x,event.y)
        #print(str(master.winfo_containing(event.x,event.y,displayof=T)))

        #rint("läuft")
        if fenster_betreten == "arbeits_fenster":
            if event.delta>0:
                canvas_test.yview_scroll(-1,UNITS)
            if event.delta<0:
                canvas_test.yview_scroll(1,UNITS)
        elif fenster_betreten == "arbeits_menü" or "top_frame":
            if event.delta>0:
                parameterliste_label.yview_scroll(-1,UNITS)
            if event.delta<0:
                parameterliste_label.yview_scroll(1,UNITS)
        else:
            print("hier gab es einen Fehler")

    #print("button "+str(button.winfo_height()))
    start=True


    fenster_betreten=None
    def arbeits_fenster_enter_event(event):
        nonlocal fenster_betreten
        fenster_betreten="arbeits_fenster"
        print(fenster_betreten)

    def arbeits_menü_enter_event(event):
        nonlocal fenster_betreten
        fenster_betreten="arbeits_menü"
        print(fenster_betreten)

    def top_frame_enter_event(event):
        nonlocal fenster_betreten
        fenster_betreten="top_frame"
        print(fenster_betreten)

    arbeits_menü.bind('<Enter>',arbeits_menü_enter_event)

    top_frame.bind('<Enter>',top_frame_enter_event)

    arbeits_fenster.bind('<Enter>',arbeits_fenster_enter_event)
    master.bind('<MouseWheel>',mouse_whell_event)
    mainloop()

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
                    "ooooooooooooooooooooooo","ppppppppppppppppppppppppp","qqqqqqqqqqqqqqqqqqqqqqqq","AAAAAAAAAAAAAAAAAAAA"
                    ,"BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"]


    code_der_in_datei_geschrieben_wird(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung,minwidth=1000,minhight=700)

    #example(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)

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
                                       elemente_welche_bei_berechnung_der_scrollhöhe_übersprungen_werden=["Button"]):

    import schreibe_buttons5eventhandling

    ursprüngliche_parameterliste=[]
    scrollregion_height=0
    for element in parameterliste:
        ursprüngliche_parameterliste.append(element)
    print("ursprüngliche_parameterliste= ",str(ursprüngliche_parameterliste))

    def liste_hinzufuegen_0():   #_0 wird später hochgezählt _h bzw _0 _1 _2 _3 ... korrektur unten entfernt da bereits
                                 # durch das Event gelöst stattdessen dem jeweiligen Button liste_zurücksetzten hinzugefügt.
        a= entry.get()
        print(a)
        parameterliste[0]=a
        print(parameterliste)
        parameterliste_label["text"]="parameterliste= "+str(parameterliste)


    def fenster_größen_anpassen():
        scrollregion_height2=parameterliste_label.winfo_height()
        #scrollbar_top_Frame["scrollregion"]=(0,0,0,parameterliste_label.winfo_height())
        canvas_top_frame["scrollregion"]=(0,0,0,scrollregion_height2)

    def Tab_event(event,scroll_height):
        scrollbar_position=scrollbar1.get()

        tab_scroll=scrollbar_position[0]+button.winfo_height()/scrollregion_height
        print("tab_scroll=",tab_scroll)
        canvas_test.yview_moveto(tab_scroll)
        # scrollbar_position=scrollbar1.get()
        print("scrollbar_position=", scrollbar1.get())

    def Tab_event_1(event,scroll_height):

        # entry_appending_y_position = button.winfo_pointery() #muss geändert werden

        # print("else")
        # print("scrollregion_height=",scrollregion_height)
        # print("button_y_position=",button_y_position)
        # print("button_y_position/scrollregion_height=",button_y_position/scrollregion_height)

        # neue_position_höhe=parameterliste_label.winfo_height() + beschreibung_label.winfo_height()
        neue_position_höhe2=0

        for element in (root.winfo_children()):
            if (str(element.winfo_class())) in elemente_welche_bei_Tab_scrolling_übersprungen_werden:
                #print("element=",element)
                #print("element_class=",element.winfo_class())
                #print("element_height=",element.winfo_height())
                neue_position_höhe2+=element.winfo_height()
        print("neue_position_höhe2=",neue_position_höhe2)

        neue_scrollpunkt=neue_position_höhe2/scrollregion_height

        # print("neu_scrollpunkt=",neue_scrollpunkt)
        canvas_test.yview_moveto(neue_scrollpunkt)  # in dem write programm ist diese position an den button selbst gekoppelt so das
        # der sprung an der richtigen stelle landet und nicht erst noch der minimale rest gefüllt werden muss.

        print("scrollbar_position=", scrollbar1.get())

    def FocusOut_event_0(event):
        # Achtung in die spätere datei wird nicht exakt der selbe code geschrieben dort wird folgender code geschrieben.
        # 1. die bind funktion wird an den jeweiligen button gekoppelt, bedeutet des if scrollbar position[1]<1 entfällt
        # und der code in der if schleife, für alle buttons auser dem letzten verwendet wird.
        # beim letzten wiederrum wird der else: code verwendet.
        # so wird auch der doppel Tab beim letzten Button vermieden.
        try:
            a= entry.get()
            # print(a)
            parameterliste[0]=a
            # print(parameterliste)
            parameterliste_label["text"]="parameterliste= "+str(parameterliste)

        # button_höhe= button.winfo_height()
        # canvas_höhe= canvas_test.winfo_height()

        # parameterliste_label_höhe= parameterliste_label.winfo_height()
        # beschreibung_label_höhe= beschreibung_label.winfo_height()

        # aaa=(canvas_höhe-parameterliste_label_höhe-beschreibung_label_höhe)/anzahl_buttons

        # frame_höhe=root.winfo_height()

        # print("frame_höhe",frame_höhe)

        # print("button_höhe=",button_höhe)
        # print("aaa=",aaa)

        # scrollbar_position=scrollbar1.get()
        # xx=scrollbar_position[0]
        # z= xx+scroll_height
        # print("z=",z)
        # print("xx=",xx)
        # canvas_test.yview_moveto(z)
        # scrollbar_position=scrollbar1.get()
        # print("scrollbar_position=", scrollbar_position)"""
        except:
            print("stellen sie sicher das die liste lang genug ist. Setzten sie sonst die liste zurück.")


    def liste_zurücksetzen_0():
        try:
            print("ursprüngliche_parameterliste= " ,str(ursprüngliche_parameterliste))
            variable_0.set(ursprüngliche_parameterliste[0])
            a= entry.get()
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
        #print("entry.winfo_pixels() =",entry.winfo_pixels(number)
        print("fraktion=(y=entry.winfo_y())",scrollbar1.fraction(x=0,y=entry.winfo_y()))
        print("entry.winfo_pointery()=",entry.winfo_pointery())
        print("fraktion=,scrollbar1.fraction(x=0,y=",entry.winfo_pointery(),"))",scrollbar1.fraction(x=0,y=entry.winfo_pointery()))
        print("entry.winfo_y()=",entry.winfo_y())

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
        i=0
        for element in ursprüngliche_parameterliste:
            parameterliste.append(element)
            FocusIn_handler(event=event,i=i)
            i+=1
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
        if b != "":
            parameterliste.append(b)
            parameterliste_label["text"]="parameterliste = "+str(parameterliste)
            variable_appending.set("")
        #print(parameterliste_label.winfo_height())
        canvas_top_frame["scrollregion"]=(0,0,0,parameterliste_label.winfo_height())   #größe wird nicht erhöht


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

        if start is True:
            canvas_test.itemconfigure(id,width=c)

        f=beschreibung_label.winfo_height()

        g=button.winfo_height()
        # h=entry.winfo_height()

        # i=button_1.winfo_height()
        # j=entry_1.winfo_height()
        k=parameterliste_label.winfo_height()

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

        scrollregion_height_3= beschreibung_label.winfo_height() + len(buttonList) * button.winfo_height() + parameterliste_label.winfo_height()
        scrollregion_height=0
        for element in (root.winfo_children()):
            if (str(element.winfo_class())) not in elemente_welche_bei_berechnung_der_scrollhöhe_übersprungen_werden:
                scrollregion_height+=element.winfo_height()
        # aufpassen was wenn entry höhen mitgenommen werden

        print("scrollregion_height=",scrollregion_height)
        print("entry_height=",entry.winfo_height())
        print("button=",button.winfo_height())
        #scrollregion_height2=anzahl_buttons*int(g)

        #print("scrollregion_height2= ", scrollregion_height2)
        #print("scrollregion_height= ", scrollregion_height)


        canvas_test["scrollregion"]=(0,0,0,scrollregion_height)
        fenster_größen_anpassen()

        if fenster_construiert2 is True:
            g=button.winfo_height()
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

        #print("scrollregion_height=",str(scrollregion_height))

        #print("master_geometry=",master.winfo_geometry())
        #print("...")
        #print("arbeits_fenster_geometry=",arbeits_fenster.winfo_geometry()) # wisth x height + x + y
        #print("...")

        #print("arbeits_menü_geometry=",arbeits_menü.winfo_geometry())   #
        #print("...")

        #print("root_geometry=",root.winfo_geometry())
        #print("...")

        #print("scrollbar_position=", scrollbar_position)
        #print("...")

        #print("scrollbar_geometry=",scrollbar_geometry)
        print("scrollbar1.winfo_children()=",scrollbar1.winfo_children())
        print("root.winfo_children()=",str(root.winfo_children()))
        for element in (root.winfo_children()):
            #print("element=",element)
            #print("element_class=",element.winfo_class())
            if (str(element.winfo_class())) == "Label":
                print("element=",element)
                print("element_class=",element.winfo_class())
                print("element_height=",element.winfo_height())

            #print("element_height=",element.winfo_height())
            #print("element_height=",element.winfo_height())

    # print("scrollbar1.winfo_children()=",.winfo_children())
        #print("scrollbar1.winfo_children()=",scrollbar1.winfo_children())




    #print("...")

        #print("button.winfo_geometry()=",button.winfo_geometry())


        #zzz= button.winfo_height()/scrollregion_height
        #print("zzz=",zzz)

        #scrollbar_position=scrollbar1.get()

        #tab_scroll=scrollbar_position[0]+button.winfo_height()/scrollregion_height
        #print("tab_scroll=",tab_scroll)

        #if scrollbar_position[1] <1:
        #    canvas_test.yview_moveto(tab_scroll)
        #    scrollbar_position=scrollbar1.get()
        #    print("scrollbar_position=", scrollbar1.get())
        #else:
        #    button_y_position = button.winfo_pointery()
        #    print("else")
        #    print("scrollregion_height=",scrollregion_height)
        #    #print("button_y_position=",button_y_position)
        #    #print("button_y_position/scrollregion_height=",button_y_position/scrollregion_height)

        #    neue_position_höhe=parameterliste_label.winfo_height() + beschreibung_label.winfo_height()

        #    neue_scrollpunkt=neue_position_höhe/scrollregion_height

        #    print("neu_scrollpunkt=",neue_scrollpunkt)
        #    canvas_test.yview_moveto(neue_scrollpunkt)  # in dem write programm ist diese position an den button selbst gekoppelt so das
        #    # der sprung an der richtigen stelle landet und nicht erst noch der minimale rest gefüllt werden muss.

        #    print("scrollbar_position=", scrollbar1.get())


        # print("scroll_height=",scroll_height)
        # print("entry.winfo_pixels() =",entry.winfo_pixels(number)
        # print("fraktion=(y=entry.winfo_y())",scrollbar1.fraction(x=0,y=entry.winfo_y()))
        # print("entry.winfo_pointery()=",entry.winfo_pointery())
        # print("fraktion=,scrollbar1.fraction(x=0,y=",entry.winfo_pointery(),"))",scrollbar1.fraction(x=0,y=entry.winfo_pointery()))
        # print("entry.winfo_y()=",entry.winfo_y())


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
        # eigentlich nicht nötig aber das wieder zu entfernen ist mehr arbeit als es einzubauen.

    master.bind('<Configure>',multi_argument_trick_fenstergröße_event)
    master.title('parameterliste_erstellen_fenster')
    master.minsize(width=500,height=380)    # bei einer kleineren größe bugt die GUI buttons verschwinden


    top_frame=Frame(master,height=0,width=0,takefocus=0)
    top_frame.pack(side="top",anchor="n",expand=False,fill="both")

    arbeits_fenster=Frame(master,width=0,height=0)
    arbeits_fenster.pack(fill="both",side="top",anchor="n",expand=True)

    arbeits_menü = Frame(master,takefocus=0,width=0,height=0)
    arbeits_menü.pack(fill="x",side="bottom",anchor="s",expand=False)




    #arbeits_menü

    #top_frame=Frame(arbeits_menü,height=0)
    #top_frame.pack(side="top",anchor="n",expand=False,fill="x")

    #arbeits_menü
    bot_frame=Frame(arbeits_menü)
    bot_frame.pack(side="bottom",anchor="n",expand=True,fill="x")

    #top_frame2=Frame(top_frame)

    #top_frame

    def info_event2(event):
        print(parameterliste_label.winfo_height())

    master.bind('<KeyPress-Control_L>',info_event2)
    canvas_top_frame= Canvas(top_frame,scrollregion=(0,0,0,0),height=62)
    canvas_top_frame.pack(anchor="se",fill="both",expand=True,side="left")

    scrollbar_top_Frame=Scrollbar(top_frame,width=17)   #die scrollbar übernimmt die länge vom arbeitsfenster
    scrollbar_top_Frame.pack(anchor="se",side="left",fill="y")





    parameterliste_label=Label(top_frame,text="parameterliste = "+str(parameterliste),justify="left",
                               wraplength=minwidth,font=('Times', '-20'),pady="7",fg="black",bg="#eeeeee")
    parameterliste_label.pack(side="left",expand=False,anchor="s")

    id_top_Frame = canvas_top_frame.create_window(0,0,anchor="nw",width=0,height=0,window=parameterliste_label)
    canvas_top_frame["scrollregion"]=(0,0,0,0)

    canvas_top_frame.config(yscrollcommand=scrollbar_top_Frame.set)
    scrollbar_top_Frame.config(command=canvas_top_frame.yview)


    zurück_button = Button(bot_frame, text="zurück",command=zurück,height="1",font=('Times', '-20'),takefocus=0)
    zurück_button.pack(side="left",fill="x",expand=True)


    weiter_button = Button(bot_frame, text="weiter",command=weiter,height="1",font=('Times', '-20'),takefocus=0)
    weiter_button.pack(side="right",fill="x",expand=True)

    i=10
    #arbeits_fenster
    canvas_test= Canvas(arbeits_fenster,scrollregion=(0,0,0,0))
    canvas_test.pack(anchor="nw",fill="both",expand=True,side="left")

    scrollbar1=Scrollbar(arbeits_fenster,width=19)   #die scrollbar übernimmt die länge vom arbeitsfenster
    scrollbar1.pack(anchor="ne",side="left",fill="y")

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


    def multi_argument_trick_Tab_event(event):
        print("scroll_height=", scroll_height)
        return Tab_event(event,scroll_height)

    def multi_argument_trick_Tab_event_1(event):
        print("scroll_height=", scroll_height)
        return Tab_event_1(event,scroll_height)

    entryList = []
    buttonList= []
    entry_textvarList= []
    entry_event_textVarlist= []
    h=0
    i=0
    for wort in parameterliste:

        entry_variable = StringVar()
        entry_variable.set(wort)
        entry = Entry(root,textvariable=entry_variable,font=('Times', '-20'))

        entry_textvarList.append(entry_variable)
        entryList.append(entry)

        entry.grid(column=0, row=i+2,sticky=N+S+E+W)

        def FocusIn_handler(event,i=i):
            event.a=StringVar()
            event.a.set(parameterliste[i])
            (entryList[i])["textvariable"]=event.a


        def FocusOut_handler(event,i=i):
            parameterliste[i]=entryList[i].get()
            parameterliste_label["text"]="parameterliste = "+str(parameterliste)

        entry.bind('<FocusIn>',FocusIn_handler)
        entry.bind('<FocusOut>',FocusOut_handler)
        entry.bind('<KeyPress-Return>',FocusOut_handler)


        def liste_zurücksetzen(event,i=i):
            parameterliste[i]=ursprüngliche_parameterliste[i]
            parameterliste_label["text"]="parameterliste = "+str(parameterliste)
            FocusIn_handler(event=event,i=i)



        button_text = "listeneintrag "+str(i)+" zurücksetzen"
        button = Button(root, text=button_text, font=('Times', '-20'), takefocus=0)
        buttonList.append(button)
        button.grid(column=1, row=i+2,sticky=N+S+E+W)

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

    button_entf = Button(root,text="entferne letzten listeneintrag (del)",font=('Times', '-20'),command=parameterliste_pop,takefocus=0)
    button_entf.grid(column=1, row=i+2,sticky=N+S+E+W)

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
                canvas_top_frame.yview_scroll(-1,UNITS)
            if event.delta<0:
                canvas_top_frame.yview_scroll(1,UNITS)
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
    datei.write("\n    scrollregion_height=0")

    h=0
    for element in parameterliste:

        datei.write(
    """
    def FocusOut_event_"""+str(h)+"""(event,scroll_height):

    
    """)

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

    def zurück():
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

        g=button.winfo_height()
        # h=entry.winfo_height()

        # i=button_1.winfo_height()
        # j=entry_1.winfo_height()
        k=parameterliste_label.winfo_height()

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

        scrollregion_height= beschreibung_label.winfo_height() + anzahl_buttons * button.winfo_height() + parameterliste_label.winfo_height()
        #scrollregion_height2=anzahl_buttons*int(g)

        #print("scrollregion_height2= ", scrollregion_height2)
        #print("scrollregion_height= ", scrollregion_height)


        canvas_test["scrollregion"]=(0,0,0,scrollregion_height)


        if fenster_construiert2 is True:
            g=button.winfo_height()
            z=g/canvas_test.winfo_height()
            scroll_height=z
            fenster_construiert2=False
            #print("fenster construiert if bedigung durchlaufen")
            #print("c=",canvas_test.winfo_height())

        def test_ob_global_richtig():
            print("scroll_height=",scroll_height)
        #test_ob_global_richtig()
        print("scrollregion_height=",str(scrollregion_height))


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




    # root=Tk()
    # root.title('parameterliste_erstellen_fenster')


    fenster_construiert=False
    scroll_height=0
    h=0
    master=Tk()


    master.geometry(str(minwidth)+"x"+str(minhight))
    master.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    master.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)
    # master.bind('<KeyPress-i>',info_event)

    def multi_argument_trick_fenstergröße_event(event):
        nonlocal fenster_construiert
        fenster_construiert3=fenster_construiert
        #print("fenster_construiert3",fenster_construiert3)
        return fenstergröße_event(event,fenster_construiert3)
        # eigentlich nicht nötig aber das wieder zu entfernen ist mehr arbeit als es einzubauen.

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

    scrollbar1=Scrollbar(arbeits_fenster)  
    scrollbar1.pack(anchor="ne",side="right",fill="y")

    canvas_test.config(yscrollcommand=scrollbar1.set)
    scrollbar1.config(command=canvas_test.yview)


    root=Frame(arbeits_fenster)
    root.columnconfigure(0, weight=3)
    root.columnconfigure(1, weight=1)

    beschreibung_variable = StringVar()
    beschreibung_variable.set(beschreibung)

    # root.minsize(width=minwidth,height=minhight)
    # root.bind('<KeyPress-Delete>',KeyPress_Delete_parameterliste_pop)
    # root.bind('<Alt_L>',Alt_L_komplette_liste_zurucksetzen)

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
                    "ooooooooooooooooooooooo","ppppppppppppppppppppppppp","qqqqqqqqqqqqqqqqqqqqqqqq","AAAAAAAAAAAAAAAAAAAA"]


    code_der_in_datei_geschrieben_wird(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung,minwidth=1000,minhight=700)

    #example(liste=liste,parameterliste=parameterliste,beschreibung=beschreibung)

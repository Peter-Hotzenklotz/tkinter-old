# This Python file uses the following encoding: utf-8

from tkinter import *
from tkinter import filedialog

__all__ = ['Vorlage mainwindow_bearbeitet.py']


Zielpfade=[]

def main(font,Message_Text):

    #suchmethode_liste=[]
    suchmethode_matrix=[[]]

    def dropdown_1():
        pass

    def zurück():
        pass

    def weiter():
        pass

    def Suchbegriff_pop_liste_event():
        pass

    def Suchbegriff_pop_wort_event():
        pass

    def ask_filename():
        dat=filedialog.askopenfile(
            initialdir = "/",title="zu durchsuchende dateien auswählen",
            filetypes=(("Textdateien","*.txt"),("Ordner(noch nicht implementiert)","*.*"))
        )
        if dat != None and str(dat) not in Zielpfade:
            print("startet")
            try:
                Zielpfade.append(str(dat))
                M1["state"]=NORMAL
                M1.delete(1.0,END)
                n=1
                for element in Zielpfade:
                    index =float(str(n)+".0")
                    #print(index)
                    anzufügendes_element=str(n)+". Pfadname= "+str(element)+"\n"
                    M1.insert(index,anzufügendes_element)
                    n+=1
                print(Zielpfade)
                M1["state"]=DISABLED
                n=1
            except:
                pass

    def ask_filename_event(event):
        dat=filedialog.askopenfile(
            initialdir = "/",title="zu durchsuchende dateien auswählen",
            filetypes=(("Textdateien","*.txt"),("Ordner(noch nicht implementiert)","*.*"))
        )
        if dat != None and str(dat) not in Zielpfade:
            print("startet")
            try:
                Zielpfade.append(str(dat))
                M1["state"]=NORMAL
                M1.delete(1.0,END)
                n=1
                for element in Zielpfade:
                    index =float(str(n)+".0")
                    #print(index)
                    anzufügendes_element=str(n)+". Pfadname= "+str(element)+"\n"
                    M1.insert(index,anzufügendes_element)
                    n+=1
                print(Zielpfade)
                M1["state"]=DISABLED
                n=1
            except:
                pass

    def master_info(event):
        print("master_height=",master.winfo_height())
        print("master_width=",master.winfo_width())
        print("suchmethode_liste=",suchmethode_liste)
        print("suchmethode_matrix=",suchmethode_matrix)

    canvas_1_scrollregion_height=0
    def fenstergröße_event(event):
        nonlocal canvas_1_scrollregion_height
        print("größenänderung")
        canvas_1.itemconfigure(id, width=canvas_1.winfo_width())

        try:
            canvas_1_scrollregion_height=0
            #for objekt in (canvas_1.Frame.grid_slaves()):
            for objekt in (canvas_1.Frame.pack_slaves()):
                canvas_1_scrollregion_height += objekt.winfo_height()
        except:
            print("ein error")
        print(canvas_1_scrollregion_height)

        canvas_1["scrollregion"]=(0,0,0,canvas_1_scrollregion_height)


    master=Tk()

    master.bind("<KeyPress-i>",master_info)
    master.minsize(width=330,height=0)
    master.geometry("660x300")
    botFr = Frame(master,takefocus=0,width=0,height=0)
    botFr.pack(fill="x",side="bottom",anchor="s",expand=False)

    topFr=Frame(master,width=0,height=0,takefocus=0)
    botFr.pack(fill="both",side="top",anchor="n",expand=True)


    botFr.pack(fill="x",side="bottom",anchor="n",expand=False)
    topFr.pack(fill="both",side="top",anchor="n",expand=True)


    #botFr
    zurück_button = Button(botFr, text="zurück",command=zurück,height="1",font=('Times', '-20'),takefocus=0)
    weiter_button = Button(botFr, text="weiter",command=weiter,height="1",font=('Times', '-20'),takefocus=0)

    zurück_button.pack(side="left",fill="x",expand=True)
    weiter_button.pack(side="right",fill="x",expand=True)

    #topFr
    scrollbar1=Scrollbar(topFr,width=19)
    canvas_1= Canvas(topFr,scrollregion=(0,0,0,0),bg="yellow")

    scrollbar1.pack(anchor="ne",side="right",fill="y")
    canvas_1.pack(anchor="ne",fill="both",expand=True,side="right")

    scrollbar1.config(command=canvas_1.yview)
    canvas_1.config(yscrollcommand=scrollbar1.set)

    canvas_1.Frame = Frame(topFr,bg="orange")


    #canvas_1.Frame

    id=canvas_1.create_window(0,0,anchor="nw",width=0,height=0,window=canvas_1.Frame)



    master.bind('<Configure>',fenstergröße_event)

    LF1=LabelFrame(canvas_1.Frame,text="suchort")
    LF2_neu=LabelFrame(canvas_1.Frame,text="suchmethode")   #nachträglich von LF2 zu LF2_neu geändert
    LF3=LabelFrame(canvas_1.Frame,text="suchergebnissbehandlung")

    #canvas_1.Frame.columnconfigure(0,weight=1)
    #canvas_1.Frame.columnconfigure(1, weight=1)

    #LF1.grid(row=0,column=0,sticky=NSEW)
    #LF2.grid(row=1,column=0,sticky=NSEW)
    #LF3.grid(row=2,column=0,sticky=NSEW)

    LF1.pack(fill="x",expand=True,side="top",anchor=S)
    LF2_neu.pack(fill="x",expand=True,side="top",anchor=S)  # geht schneller es hier zu ändern anstatt unten jeden bezug
    LF3.pack(fill="both",expand=True,side="top",anchor=S)

    LF2=Frame(LF2_neu)
    LF2.pack(side="top",expand=True,fill="both")

    LF2_Textfeld=Text(LF2_neu,height=2,font=font,takefocus=0)
    LF2_Textfeld.pack(side="bottom",expand=True,fill="both")

    #LF1 suchort

    LF1_F1= Frame(LF1)
    LF1_F2= Frame(LF1)

    LF1_F1.pack(side="top",expand=True,anchor="w",fill="x")

    LF1_F2.pack(side="top",fill="both",expand=True)





    B1=Button(LF1_F1,text=".txt wählen",font=font,command=ask_filename)
    B1.bind("<KeyPress-Return>",ask_filename_event)

    #B2=Button(LF1_F1,text="zweiter",font=font)

    L1=Label(LF1_F1,text=" Anzahl:",font=font)
    L2=Label(LF1_F1,text=" .txt =",font=font)
    L3=Label(LF1_F1,text="0  ",font=font,bg="white")
    L4=Label(LF1_F1,text=" Ordner = ",font=font)
    L5=Label(LF1_F1,text="0  ",font=font,bg="white")
    L6=Label(LF1_F1,text=" Lösche: ",font=font)

    B6=Button(LF1_F1,text="komplett",font=font,takefocus=0)

    B5=Button(LF1_F1,text="letze",font=font,takefocus=0)



    B1.pack(side="left",anchor="w",fill="both")
    #B2.pack(side="left",fill="x",expand=False)

    B6.pack(side="right",fill="both",expand=True,anchor="e")
    B5.pack(side="right",fill="both",expand=True,anchor="e")
    L6.pack(side="right")

    L1.pack(side="left")
    L2.pack(side="left")
    L3.pack(side="left")
    L4.pack(side="left")
    L5.pack(side="left")

    M1=Text(LF1_F2,font=font,height="2")

    #T1_scrollbar= Scrollbar(LF1_F2)

    #T1_scrollbar.pack(side="right",fill="y",expand=False,anchor="w")
    M1.pack(side="left",fill="both",expand=True)

    #M1["state"]=DISABLED
    #M1["state"]=NORMAL

    M1.insert(1.0,"1. Pfadname = ")
    M1["state"]=DISABLED

    B3=Button(LF3,text="dritter",font=font)
    b4=Button(LF2,text="vieter",font=font)

    #B3.pack(side="left")

    #M1["height"]=LF1_F1["height"]

    #b4.pack(side="left")

    #LF2 suchmethode
    LF2_ModusListe=["neue_liste_Modus","liste_anhängen_Modus","liste_ersetzen_Modus"]

    LF2.var1=StringVar()
    LF2.var1.set(LF2_ModusListe[0])
    LF2_ModusListe_objekt=OptionMenu(LF2,LF2.var1,*LF2_ModusListe)

    #LF2_

    LF2_DropDown_var=StringVar()
    LF2_DropDown = Menubutton(LF2,textvariable=LF2_DropDown_var,font=font,relief=RAISED,takefocus=0)

    LF2_L1_var=StringVar()
    LF2_L1=Label(LF2,font=font,textvariable=LF2_L1_var,bg="white",width=7)


    def LF2_E1_event_enter(event):
        LF2_E1_var.set("")

    def LF2_E1_event_leave(event):
        LF2_E1_var.set("Suchbegriff")

    suchmethode_matrix_zähler = 0
    def LF2_E1_event_Return(event):
        nonlocal suchmethode_matrix
        nonlocal suchmethode_matrix_zähler
        wort=LF2_E1_var.get()
        print("wort=",wort)
        Modus=LF2_L1_var.get()
        print("Modus=",Modus)

 # alternaativ nutzung von len(suchmethode_matrix)

        LF2_Textfeld.delete(1.0,END)
        if Modus == "anhängen":
            (suchmethode_matrix[suchmethode_matrix_zähler]).append(wort)
            print(suchmethode_matrix[suchmethode_matrix_zähler])
        if Modus == "neu" and wort!="":
            if len(suchmethode_matrix[0]) >= 1:
                suchmethode_matrix.append([wort])
                suchmethode_matrix_zähler+=1
            else:
                suchmethode_matrix[0].append(wort)

        if Modus == "löschen":
            suchmethode_matrix=[[wort]]
            suchmethode_matrix_zähler=0
        LF2_Textfeld.insert(1.0,str(suchmethode_matrix))


        LF2_E1_var.set("")


    LF2_E1_var=StringVar()
    LF2_E1=Entry(LF2,font=font,textvariable=LF2_E1_var,width=15)
    LF2_E1_var.set("Suchbegriff")
    LF2_E1.bind("<FocusIn>",LF2_E1_event_enter)
    LF2_E1.bind("<FocusOut>",LF2_E1_event_leave)
    LF2_E1.bind("<KeyPress-Return>",LF2_E1_event_Return)


    LF2_L2=Label(LF2,text=" entf: ",font=font,anchor="e")
    LF2_B1=Button(LF2,text="Liste",font=font,command=Suchbegriff_pop_liste_event,takefocus=0)
    LF2_B2=Button(LF2,text="Wort",font=font,command=Suchbegriff_pop_wort_event,takefocus=0)
    LF2_L3=Label(LF2,text="      ",font=font)
    LF2_txt_wahlButton=Button(LF2,text=".txt settings nutzen",font=font,anchor="w",takefocus=0)

    #LF2_objekt_sticky_var="nsew"
    LF2_objekt_sticky_var="nsew"
    #LF2_objekt_sticky_var="ew"

    #gridding taugt hier nichts
    """
    LF2_E1.grid(row=0,column=0,sticky=LF2_objekt_sticky_var)
    LF2_DropDown.grid(row=0,column=1,sticky=LF2_objekt_sticky_var)
    LF2_L1.grid(row=0,column=2,sticky=LF2_objekt_sticky_var)
    LF2_L2.grid(row=0,column=3,sticky=LF2_objekt_sticky_var)
    LF2_B1.grid(row=0,column=4,sticky=LF2_objekt_sticky_var)
    LF2_B2.grid(row=0,column=5,sticky=LF2_objekt_sticky_var)
    LF2_txt_wahlButton.grid(row=0,column=5,sticky=LF2_objekt_sticky_var)
    """
    LF2_E1.pack(side="left",fill="both",expand=True)
    LF2_DropDown.pack(side="left",fill="both",expand=True)
    LF2_L1.pack(side="left",fill="both",expand=True)
    LF2_L2.pack(side="left",fill="both",expand=True)
    LF2_B1.pack(side="left",fill="both",expand=True)
    LF2_B2.pack(side="left",fill="both",expand=True)
    #LF2_L3.pack(side="left",fill="y")
    LF2_txt_wahlButton.pack(side="right",fill="both",expand=False)

    LF2_DropDown_var.set("Modus: ")
    LF2_DropDown.menu = Menu(LF2_DropDown,tearoff=0)
    LF2_DropDown["menu"]=LF2_DropDown.menu

    LF2_DropDown_menu_liste=["anhängen","neu","löschen"]

    i=0
    for eintrag in LF2_DropDown_menu_liste:

        def dropdown(i=i):
            print(LF2_DropDown_menu_liste[i])
            LF2_L1_var.set(LF2_DropDown_menu_liste[i])

        LF2_DropDown.menu.add_command(label=LF2_DropDown_menu_liste[i],command=dropdown,font=font)

        i+=1
    LF2_L1_var.set(LF2_DropDown_menu_liste[1])






    mainloop()


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

    main(font=('Times', '-20'),Message_Text=beschreibung)

# This Python file uses the following encoding: utf-8

# mir ist bewusst das ich hier ziemliche Spagethicode produziert habe.

__all__ = ['schreibe_buttons5eventhandling.py']


def liste_als_objekte (liste=[], bezugsobjekt= "fr", dateiname= "jjj.py", objekttyp= "Button", bennenung= "l",
                       title_is_dateiname= True, title= "ops", fenster_text_breite = 150, farbgebung = "blue",
                       nach_farbgebung = "red", mainloop_hinzufügen= False, erase_file_if_it_already_exists= True,
                       ziellistenname="zielliste",zeichenliste = [".",",","/",":",";","-","+","'",'"'],
                       Menübottons_schreiben = True, Menü_Buttons_Liste=["Nomen","verben","adjektive","Orte","adverben",
                                                                        "buxdehude","jens","daniel","Politik","Fenster","Poster"],
                       menu_frame_width="300", menu_frame_height="120", menu_frame="menu_frame",fg_menü="black",
                       bg_menü= "gray", hight_menü="3",root_width="1000",root_hight=300, root_fenster=True,
                       Tk_fenstername="root"):
    """ergebniss ist ein Fenster mit den Listeneinträgen als Button (der Name des Buttons ist das Wort in der Liste)
    Die Buttons werden je links oben angeordnet und bei einer Textlänge von fenster_test_breite (170 zeichen)
    in die Nächste Zeile versetzt. farbgebung(blue) gibt die schriftfarbe des Buttons vor dem Klicken an, nach_farbgebung
    die Farbgebung nach dem klicken auf den Button. Jeder Button ist ein eigenes Objekt. Der Name des Objekts ist
    bennung+1 (bsp. l1, l2, l3, l4) usw. jeweils mit der Position in der Liste. Um diese Objekte zu erstellen wird eine
    .py-datei beschrieben der dateiname = dateiname (hhh.py). Zum aufrufen der einzelnen objekte ist daher ein
    import dateiname(hhh.py) nötig danach muss zum Zugriff auf die Objekte der Name der angelegten datei .
    der Name des Objekts benutzt werden. (z.b. hhh.l1) oder um darin bsp elemente zu verändern (hhh.l1.configure())
    ACHTUNG: um das Textfenster zu verfolständigen ist unbedingt ein dateiname.mainloop() bzw. (hhh.mainloop()) nötig
    auser .mainloop hinzufügen steht nicht auf False. Achtung sollte ein \\\ in der liste auftauchen hagelt es fehler."""


    tastatur_liste=["1","2","3","4","5","6","7","8","9","0",
                    "q","w","e","r","t","z","u","i","o","p","ü",
                    "a","s","d","f","g","h","j","k","l","ö","ä",
                    "y","x","c","v","b","n","m"]

    if title_is_dateiname is True:
        title=dateiname
    else:
        title=title


    try:
        datei = open(dateiname,"x",encoding='utf-8')
    except:
        print(dateiname, "already in existence,")
        if erase_file_if_it_already_exists is True:
            print("erase_file_if_it_already_exists is True",dateiname,"will be erased and newly written with open 'w' ")
            datei = open(dateiname,"w",encoding='utf-8')

    ä = []
    for wort in liste:
        if wort not in zeichenliste:
            ä.append("")
        else:
            ä.append(wort)

    #beginn

    datei.write(
"""
from tkinter import *


print('Datei """+ dateiname +""" wurde importiert')

def temp ():
    betreten = ''

    Menü_Buttons_Liste = """+str(Menü_Buttons_Liste)+"""
    
    """
        +ziellistenname+""" = """+str(ä)+"""

    nach_farbgebung = '"""+nach_farbgebung +"""'
    farbgebung = '"""+farbgebung+"""'

    """)

    i = 0

    #aktionen definieren
    # ich weiß es gibt einen besseren weg (was die farbe und die koppelung an den Klik auf den Button und die vorherige
    # liste angeht aber der Code ist schon weit geschrieben daher, andere ich die fg im Button und der funktion.


    i=0

    for wort in liste:
        datei.write("\n")
        datei.write("    ")
        datei.write("liste_"+str(i)+"= []")

        i+=1

    i=0
    testliste=[]
    datei.write("\n    Keyliste = {'':'wort', ")
    for wort in liste:
        if wort not in testliste:
            datei.write("'"+wort+"':"+"liste_"+str(i)+", ")
        testliste.append(wort)
        i+=1
    datei.write("}\n")

    i=0
    for wort in liste:
        datei.write(
"""
    nach_farbgebung"""+str(i)+" = '"+nach_farbgebung +"""'
    farbgebung"""+str(i)+" = '"+farbgebung +"""'
    
    def aktion"""+str(i)+"""():
        l"""+str(i)+""".config(fg= nach_farbgebung"""+""", command = zurück"""+str(i)+""")
        a = l"""+str(i)+""".cget('text')
        """
        +ziellistenname+"""["""+str(i)+"""] = str(a)
        """+ziellistenname+"_Label['text']= '"+ziellistenname+" = '+str("+ziellistenname+""")
    
    def zurück"""+str(i)+"""():
        l"""+str(i)+""".config(fg=farbgebung"""+""", command = aktion"""+str(i)+""")
        """
        +ziellistenname+"""["""+str(i)+"""] = ''
        """+ziellistenname+"_Label['text']= '"+ziellistenname+" = '+str("+ziellistenname+""")
    
    """)
        i+=1

    if root_fenster is True:

        datei.write(
"""
    root = Tk()
    root.title('"""+title+""" maximalbildschirmgröße')
    root.minsize(width=1000, height=200)
    
    """)
    else:
        print("wird noch implementiert")
        datei.write(
"""
    # root = 
    
    """)

    #for wort in liste:
    #    datei.write()

    h = 1
    text_länge = 0
    #framename =  str(bezugsobjekt)+str(h)
    #datei.write(framename+" = Frame(root, width=300, height=20)")
    #datei.write("\n")
    #datei.write(framename+".pack(anchor='nw',side='top')")
    #datei.write("\n")





    i = 0
    h = 1
    framename = str(bezugsobjekt)+str(h)
    datei.write(framename +" = Frame(root, width=300, height=20)\n    ")
    datei.write(str(bezugsobjekt)+str(h)+".pack(anchor='nw',side='top')\n    ")
    for wort in liste:
        datei.write(
"""


    def on_enter"""+str(i)+"""(event):
        nonlocal betreten
        betreten= '"""+str(wort)+"""'
    
        # print('betreten= ',betreten)
    """)
        i+=1

    i=0
    h=0

    for eintrag in Menü_Buttons_Liste:

        datei.write(
"""
    def print_betreten"""+str(h)+"""(event):
        # print(betreten+'= """+str(h+1)+"""')
        
        if betreten not in Menübutton_Liste_"""+str(h)+""":
            Menübutton_Liste_"""+str(h)+""".append(betreten)
            Menübutton_Label_"""+str(h)+"""['text']= '"""+str(h+1)+" "+str(eintrag)+" = ' +str(Menübutton_Liste_"+str(h)+""")
            Keyliste[betreten].append('"""+eintrag+"""')
    
        else:
            Menübutton_Liste_"""+str(h)+""".remove(betreten)
            Menübutton_Label_"""+str(h)+"""['text']= '"""+str(h+1)+" "+str(eintrag)+" = ' +str(Menübutton_Liste_"+str(h)+""")
            Keyliste[betreten].remove('"""+eintrag+"""')
        print('Keyliste= ',Keyliste)
        
    root.bind('<KeyPress - """+str(tastatur_liste[h])+""">',print_betreten"""+str(h)+""")
    """)
        h+=1

    h=0
    i=0
    text_länge = 0
    for wort in liste:
        if text_länge + len(wort) >= fenster_text_breite:
            h+=1
            framename = str(bezugsobjekt)+str(h)    #root.framename
            datei.write("\n    ")
            datei.write(framename+" = Frame(root, width=300, height=20)")
            datei.write("\n    ")
            datei.write(framename+".pack(anchor='nw',side='top')")
            datei.write("\n    ")

            buttonname= bennenung+str(i)    #root.framename.buttonname
            datei.write("farbgebung"+str(i)+"= "+"'"+farbgebung+"'")
            datei.write("\n    ")

            if wort in zeichenliste:
                button_fg = "'"+'red'+"'"
                button_command = "zurück"+str(i)

            else:
                button_fg = "'"+farbgebung+str(i)+"'"
                button_command = "aktion"+str(i)

            datei.write(buttonname + "= "+objekttyp+"("+framename+", text= '"+(wort)+"' , fg = "+button_fg+", textvariable= '"+str(i)+"',command="+button_command+")") #button
            datei.write("\n    ")

            #datei.write(buttonname +".bind('<Enter>', farbgebung"+str(i)+"= 'red' )")
            #datei.write("\n")

            datei.write(buttonname + ".pack(anchor='nw',side='left')")
            datei.write("\n    ")
            text_länge = 0

        else:
            buttonname= bennenung+str(i)    ##root.framename.buttonname
            datei.write("farbgebung"+str(i)+ "= 'blue'")
            datei.write("\n    ")

            if wort in zeichenliste:
                button_fg = "'"+'red'+"'"
                button_command = "zurück"+str(i)

            else:
                button_fg = 'farbgebung'+str(i)
                button_command = "aktion"+str(i)

            datei.write(buttonname + "= "+objekttyp+"("+framename+", text= '"+(wort)+"' , fg = "+button_fg+", textvariable= '"+str(i)+"',command="+button_command+")") #button
            datei.write("\n    ")

            #datei.write(buttonname +".bind('<Enter>', farbgebung"+str(i)+"= 'red' )")
            #datei.write("\n")

            datei.write(buttonname + ".pack(anchor='nw',side='left')")
            datei.write("\n    ")
            datei.write(buttonname + ".bind('<Enter>',on_enter"+str(i)+")")
            datei.write("\n    ")

        i += 1
        text_länge += len(wort)

    menu_frame_name = str(menu_frame)+str(h)
    menu_frame_width = str(menu_frame_width)
    menu_frame_height = str(menu_frame_height)

    datei.write("\n    ")
    datei.write(menu_frame_name+" = Frame(root, width= "+menu_frame_width+", height="+menu_frame_height+")")
    datei.write("\n    ")
    datei.write(menu_frame_name+".pack(anchor='nw',side='top')")
    datei.write("\n    ")

    h=0
    for eintrag in Menü_Buttons_Liste:

        datei.write(
"""            
    def m_aktion"""+str(h)+"""():
        pass         
    """)
        h+=1

    h=0     #listeneinträge in Menübutton_zähler
    r=0     #row
    c=0     #column
    text_länge = 0


    for eintrag in Menü_Buttons_Liste:
        datei.write(
"""
    # erstelle Listenlabel
    Menübutton_Liste_"""+str(h)+""" = []
    Menübutton_Label_"""+str(h)+"= Label(root, text= '"+str(h+1)+" "+str(eintrag)+" = '+str(Menübutton_Liste_"+str(h)+"""))
    Menübutton_Label_"""+str(h)+""".pack(anchor='sw', side='top')
    """)
        h+=1

    datei.write("\n    ")
    datei.write(ziellistenname+"_Label= Label(root, text= '"+ziellistenname+" = []' )")
    datei.write("\n    ")
    datei.write(ziellistenname+"_Label.pack(anchor='sw',side='top')")
    datei.write("\n    ")

    datei.write(
"""
    zielliste_Menu= []
    def liste_umwandeln():
        zielliste_Menu= []
        # global zielliste_Menu
        # print("global= ",zielliste_Menu)
        i=0
        for wort in zielliste:
            Else=True
    """)
    h=0  #zähler Menü_buttons_liste

    for eintrag in Menü_Buttons_Liste:

        datei.write(
"""
            if wort in Menübutton_Liste_"""+str(h)+""":
                zielliste_Menu.append('"""+eintrag+"""')
                Else=False
    """)
        h+=1
    h=0
    datei.write(
"""
            else:
                if Else is True:
                    zielliste_Menu.append(wort)
                else:
                    continue
                
            i+=1
            # print('zielliste_Menu= ',zielliste_Menu)
    """)
    datei.write(
"""
        # ändere liste
        """+ziellistenname+"""_Menu_Label['text']= 'zielliste_Menu = '+str(zielliste_Menu)
        
    """)


    datei.write(
"""
    def Keyliste_umwandeln():
        zielliste_Menu_Key= []
        zielliste_Menu_Key_ohne= []
        # global zielliste_Menu
        # print("global= ",zielliste_Menu)
        i=0
        for wort in zielliste:
            Else=True
    """)
    h=0  #zähler Menü_buttons_liste


    datei.write(
"""
            
            if wort in Keyliste and len(Keyliste[wort]) >=1:
                zz= str(wort)+' = '+str(Keyliste[wort])
                zielliste_Menu_Key.append(zz)
                zielliste_Menu_Key_ohne.append(Keyliste[wort])
                Else=False
    
            else:
                if Else is True:
                    zielliste_Menu_Key.append(wort)
                    zielliste_Menu_Key_ohne.append(wort)
    
                else:
                    continue
                
            i+=1
            # print('zielliste_Menu_Key= ',zielliste_Menu_Key)
    """)

    datei.write(
"""
        # ändere liste
        """+ziellistenname+"""_Menu_Label_Key['text']= 'zielliste_Menu_Key = '+str(zielliste_Menu_Key)
        """+ziellistenname+"""_Menu_Label_Key_ohne['text']= 'zielliste_Menu_Key_ohne = '+str(zielliste_Menu_Key_ohne)
    
    """)
    datei.write("\n    ")
    datei.write(ziellistenname+"_Menu_Label= Label(root, text= '"+ziellistenname+"_Menu = [] ')")
    datei.write("\n    ")
    datei.write(ziellistenname+"_Menu_Label.pack(anchor='sw',side='top')")
    datei.write("\n    ")

    datei.write(ziellistenname+"_Menu_Label_Key= Label(root, text= '"+ziellistenname+"_Menu_Key = [] ')")
    datei.write("\n    ")
    datei.write(ziellistenname+"_Menu_Label_Key.pack(anchor='sw',side='top')")
    datei.write("\n    ")

    datei.write(ziellistenname+"_Menu_Label_Key_ohne= Label(root, text= '"+ziellistenname+"_Menu_Key_ohne = [] ')")
    datei.write("\n    ")
    datei.write(ziellistenname+"_Menu_Label_Key_ohne.pack(anchor='sw',side='top')")
    datei.write("\n    ")


    if mainloop_hinzufügen is True:
        datei.write("mainloop()")
    datei.write(
"""
    print('Datei """+ dateiname+ """.temp wurde erfolgreich durchlaufen')
    """)
    datei.close()

    #import temporärer_button_code
    #temporärer_button_code.temp()


def schreibe_buttons(wortliste=[],parameterliste=[],mainloop_hinzufügen=False):

    liste_als_objekte(liste=wortliste, Menü_Buttons_Liste=parameterliste,dateiname="temporärer_button_code.py", mainloop_hinzufügen=mainloop_hinzufügen)
    datei=open("../22-07-2021 fertiger code/temporärer_button_code.py", "a")
    datei.write(
"""
    def finish():
        liste_umwandeln()
        Keyliste_umwandeln()
        # print("zielliste=",zielliste)
        datei = open("Vorliste.txt","a",encoding='utf-8')
        datei.write("suchwort="+str(zielliste)+"\\n")
        datei.close()

    def listen_erzeugen():
        liste_umwandeln()
        Keyliste_umwandeln()

    unteres_menu = Frame(root)    
    unteres_menu.pack(side="bottom",fill="both")


    listen_erzeugen= Button(unteres_menu, text="listen erzeugen",height="3",command=listen_erzeugen)
    listen_erzeugen.pack(anchor="w",side="left",fill="x",expand=True)

    finish= Button(unteres_menu, text="finish",command=finish,height="3")
    finish.pack(anchor="e",side="right",fill="x",expand=True)



    mainloop()""")
    datei.close()

def alles(liste=[],parameterliste=[],ausnahmen_für_zeichensplit=["J.R.R.Martin"],warnung_abbruch=True, mainloop_hinzufügen=False):
    import zeichensplit
    a = "\\"
    # print("a=",a)
    if a not in liste and warnung_abbruch is True:
        zielliste = zeichensplit.zeichensplit(liste, ausnahmen=ausnahmen_für_zeichensplit)

        print(zielliste)

        if a not in zielliste and warnung_abbruch is True:
            schreibe_buttons(wortliste = zielliste,parameterliste=parameterliste,mainloop_hinzufügen=mainloop_hinzufügen)

        else:
            print("Warnung bei 2, beim zweiten mal ist \\ in der Liste, daher .py datei konnte nicht geschrieben werden")
    else:
        print("Warnung bei 1, stellen sie sicher das kein \\ in der liste ist")

    import temporärer_button_code
    temporärer_button_code.temp()

def example(liste):

    liste_als_objekte(liste=liste, dateiname="temporärer_button_code.py",mainloop_hinzufügen=True)
    import temporärer_button_code
    temporärer_button_code.temp()

if __name__ == "__main__":

    liste=[".Haus.klasse,raus.maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,mu//sik:raus-hausaufgaben"
        ,"Faust.","ostern.","J.R.R.Martin","essen"]
    parameterliste=["Nomen","verben","adjektive"]
    #example(liste=liste)
    alles(liste=liste,parameterliste=parameterliste)



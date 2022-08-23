# This Python file uses the following encoding: utf-8

__all__ = ['zeichensplit']


liste = ["...Haus.klasse,raus...maus.aktion","J.R.R.Martin","a.","Klaus",".", "raus:ofer,musik:raus-hausaufgaben", "Faust.","\\"
         ,"ostern.","essen"]
zeichenliste = [".",",","/",":",";","-","+","'",'"']


def zeichensplit(liste=[], zeichenliste=[".",",","/",":",";","-","+","'",'"',"\\"], ausnahmen=["J.R.R.Martin"]):
    __zielliste=[]
    for wort in liste:
        if wort not in ausnahmen and len(wort)>=2:
            von=0
            bis=0
            for buchstabe in wort:
                if buchstabe in zeichenliste:
                    try:
                        a= (wort[bis-1])
                    except:
                        continue

                    if bis == 0:
                        __zielliste.append(wort[bis]) #das zeichen steht hier am anfang des wortes

                    elif a in zeichenliste:  #wenn nächster Buchtabe in der zeichenliste ist
                        __zielliste.append(wort[bis])
                    else:
                        __zielliste.append(wort[von:bis])    #ist bis zu dem zeichen
                        __zielliste.append(wort[bis])    #bis ist das auszuklammernde zeichen
                    von = bis+1
                bis+=1
                #von = bis
                if bis == len(wort) and buchstabe not in zeichenliste:
                    __zielliste.append(wort[von:])
        else:
            __zielliste.append(wort)

    return (__zielliste)

def example():
    liste_nach_zeichensplit = zeichensplit(liste)
    print("liste_nach_zeichensplit=",liste_nach_zeichensplit)

if __name__ == "__main__":
    example()

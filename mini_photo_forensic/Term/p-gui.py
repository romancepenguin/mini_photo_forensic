from Tkinter import *
import FilePath
import os
import _modEXIF
import _modifyEXIF
import _caesarHandler
import _transpositionHandler
import _CipherAndDetect
import _affineHandler

def hack():
    if radVar.get() == 1:
        key = _caesarHandler.hackCaesar(str(t4.get()))
        #_caesarHandler.hackCaesar(str(t5.get()))
        #_caesarHandler.hackCaesar(str(t6.get()))
        if key == -1:
            t2.delete(0, END)
            t2.insert(0, "impossible hack")
        else :
            en2 = str(_caesarHandler.encryptOrdecrypt(str(t4.get()), 'decrypt',key))
            en3 = str(_caesarHandler.encryptOrdecrypt(str(t5.get()), 'decrypt',key))
            en4 = str(_caesarHandler.encryptOrdecrypt(str(t6.get()), 'decrypt',key))

            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)

            t4.insert(0, en2)
            t5.insert(0, en3)
            t6.insert(0, en4)

            t2.delete(0, END)
            t2.insert(0, "hack complete")

    if radVar.get() == 2:

        key = _transpositionHandler.hackTransposition(str(t4.get()))
        # _caesarHandler.hackCaesar(str(t5.get()))
        # _caesarHandler.hackCaesar(str(t6.get()))
        if key == -1:
            t2.delete(0, END)
            t2.insert(0, "impossible hack")
        else:
            en2 = str(_transpositionHandler.decryptMessage(key,str(t4.get())))
            en3 = str(_transpositionHandler.decryptMessage(key,str(t5.get())))
            en4 = str(_transpositionHandler.decryptMessage(key,str(t6.get())))

            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)

            t4.insert(0, en2)
            t5.insert(0, en3)
            t6.insert(0, en4)

            t2.delete(0, END)
            t2.insert(0, "hack complete")

    if radVar.get() == 3:
        key = _affineHandler.hackAffine(str(t4.get()))
        # _caesarHandler.hackCaesar(str(t5.get()))
        # _caesarHandler.hackCaesar(str(t6.get()))
        if key == -1:
            t2.delete(0, END)
            t2.insert(0, "impossible hack")
        else:
            en2 = str(_affineHandler.decryptMessage(key, str(t4.get())))
            en3 = str(_affineHandler.decryptMessage(key, str(t5.get())))
            en4 = str(_affineHandler.decryptMessage(key, str(t6.get())))

            t4.delete(0, END)
            t5.delete(0, END)
            t6.delete(0, END)

            t4.insert(0, en2)
            t5.insert(0, en3)
            t6.insert(0, en4)

            t2.delete(0, END)
            t2.insert(0, "hack complete")

def encrypt():
    if radVar.get() == 1:
        key=0
        key = _CipherAndDetect.randomKey(_caesarHandler.LETTERS)

        en2 = str(_caesarHandler.encryptOrdecrypt(str(t4.get()), 'encrypt',key))
        en3 = str(_caesarHandler.encryptOrdecrypt(str(t5.get()), 'encrypt',key))
        en4 = str(_caesarHandler.encryptOrdecrypt(str(t6.get()), 'encrypt',key))

        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)

        t4.insert(0, en2)
        t5.insert(0, en3)
        t6.insert(0, en4)

        t2.delete(0, END)
        t2.insert(0, "encrypt complete")

    if radVar.get() == 2:

        if len(str(t4.get())) < len(str(t5.get())):
            MinStr = str(t4.get())
        else :
            MinStr = str(t5.get())
        if len(MinStr) > len(str(t6.get())):
            MinStr = str(t6.get())

        key = _CipherAndDetect.randomKey(MinStr)


        en2 = str(_transpositionHandler.encryptMessage(key, str(t4.get())))
        en3 = str(_transpositionHandler.encryptMessage(key, str(t5.get())))
        en4 = str(_transpositionHandler.encryptMessage(key, str(t6.get())))

        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)

        t4.insert(0, en2)
        t5.insert(0, en3)
        t6.insert(0, en4)

        t2.delete(0, END)
        t2.insert(0, "encrypt complete")

    if radVar.get() == 3:
        key = 0
        key = _CipherAndDetect.randomKeyAffine(len(_affineHandler.SYMBOLS) ** 2)

        en2 = str(_affineHandler.encryptMessage(key, str(t4.get())))
        en3 = str(_affineHandler.encryptMessage(key, str(t5.get())))
        en4 = str(_affineHandler.encryptMessage(key, str(t6.get())))

        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)

        t4.insert(0, en2)
        t5.insert(0, en3)
        t6.insert(0, en4)

        t2.delete(0, END)
        t2.insert(0, "encrypt complete")


def callback():
    name=FilePath.test()
    #print name
    if name!=None:
        t1.delete(0,END)
        t1.insert(END,name)

def forensic():
    #print t1.get()
    gpsDictionary, exifList = _modEXIF.ExtractGPSDictionary(t1.get())

    if(gpsDictionary!=None):
        gps=_modEXIF.ExtractLatLon(gpsDictionary)
        t3.delete(0, END)
        t3.insert(0, str(gps.get("Lat")) + "," + str(gps.get("Lon")))
    else:
        t2.delete(0, END)
        t2.insert(0, "not exist gps data")

    if (gpsDictionary == None and exifList == None):
        t2.delete(0, END)
        t2.insert(0, "not exist exif data")
    else:
        t4.delete(0, END)
        t5.delete(0, END)
        t6.delete(0, END)

        t4.insert(0, exifList[0])
        t5.insert(0, exifList[1])
        t6.insert(0, exifList[2])
        # exifList[TS], exifList[MAKE], exifList[MODEL]
    #print(gpsDictionary)
        #print(exifList)

def modifyexif():
    m=_modifyEXIF._modifyEXIF(t1.get())

    cnt=0
    for x in t3.get():
        if x==",":
            cnt+=1
    if cnt!=1:
        t2.delete(0,END)
        t2.insert(0,"error gps data")
    else:
        tlist=t3.get().split(",")
        if(tlist[0].isdigit and tlist[1].isdigit):
            m.ModifyGps(t3.get())
            m.ModifyTime(t4.get())
            m.ModifyMake(t5.get())
            m.ModifyModel(t6.get())
            t2.delete(0, END)
            t2.insert(0, "modify complite")

window=Tk()
window.title("exif cotrol")
        #window.geometry("550x500")

l1=Label(window,text="!!EXIF Control!!", fg = "blue",font = "Times 16 bold italic")
        #Image Path","TimeStamp","Camera Make","Camera Model","Lat Ref","Latitude","Lon Ref","Longitude"

l2=Label(window,text="path : ")
l3=Label(window,text="state : ")
l4=Label(window,text="gps : ")
l5=Label(window,text="time stamp : ")
l6=Label(window,text="maker : ")
l7=Label(window,text="model : ")

ch1=Checkbutton(window, text="TransPosition")

b1 = Button(window, text="BROWSE",command=callback)
b2 = Button(window, text="FORENSIC",command=forensic)
b3 = Button(window, text="CYPER",command=encrypt)
b4 = Button(window, text="MODIFY", command=modifyexif)
b5 = Button(window, text="EXIT", command=quit)
b6 = Button(window, text="HACK", command=hack)

radVar = IntVar()
r1=Radiobutton(window, text="Caesar", value=1, variable=radVar)
r2=Radiobutton(window, text="TransPosition", value=2, variable=radVar)
r3=Radiobutton(window, text="Affine", value=3, variable=radVar)

t1= Entry(window)
t2= Entry(window)
t3= Entry(window)
t4= Entry(window)
t5= Entry(window)
t6= Entry(window)

l1.grid(row=0, column=1, padx=5, pady=5, sticky=W)
l2.grid(row=1, column=0, padx=5, pady=5, sticky=W)
l3.grid(row=2, column=0, padx=5, pady=5, sticky=W)
l4.grid(row=3, column=0, padx=5, pady=5, sticky=W)
l5.grid(row=4, column=0, padx=5, pady=5, sticky=W)
l6.grid(row=5, column=0, padx=5, pady=5, sticky=W)
l7.grid(row=6, column=0, padx=5, pady=5, sticky=W)

t1.grid(row=1, column=1, padx=5, pady=5, sticky=W)
t2.grid(row=2, column=1, padx=5, pady=5, sticky=W)
t3.grid(row=3, column=1, padx=5, pady=5, sticky=W)
t4.grid(row=4, column=1, padx=5, pady=5, sticky=W)
t5.grid(row=5, column=1, padx=5, pady=5, sticky=W)
t6.grid(row=6, column=1, padx=5, pady=5, sticky=W)

r1.grid(row=7, column=1, padx=5, pady=5, sticky=W)
r2.grid(row=8, column=1, padx=5, pady=5, sticky=W)
r3.grid(row=9, column=1, padx=5, pady=5, sticky=W)

b1.grid(row=1, column=2, padx=5, pady=5, sticky=W)
b2.grid(row=2, column=2, padx=5, pady=5, sticky=W)
b3.grid(row=7, column=2, padx=5, pady=5, sticky=W)
b4.grid(row=8, column=2, padx=5, pady=5, sticky=W)
b5.grid(row=9, column=2, padx=5, pady=5, sticky=W)
b6.grid(row=7, column=0, padx=5, pady=5, sticky=W)


window.mainloop()

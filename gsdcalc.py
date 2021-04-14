from guizero import App, Text, TextBox, Combo, PushButton
import math as m

def update():
    if drone.value=="-Custom-":
        resw.value="0"
        resh.value="0"
        sensw.value="0"
        sensh.value="0"
        pcount.value="0"
        psize.value="0"
        fole.value="0"
    elif drone.value=="DJI Inspire 1 - Zenmuse X5":
        resw.value = "4096"
        resh.value = "2160"
        sensw.value = "17.3"
        sensh.value = "13"
        fole.value = "15"
    elif drone.value=="Test":
        resw.value = "14216"
        resh.value = "14216"
        sensw.value = "79"
        sensh.value = "79"
        fole.value = "102"
        qpro_v.value = "30"
        ppro_v.value = "60"
        areal_v.value = "17100000"
        areaw_v.value = "15500000"
        gsd_v.value = "5"

def calcgsd():
    x=float(gsd_v.value)/100 #gsd_v.value gibt die gewünschte GSD in mm an
    y=float(fole.value) #fole.value gibt die Brennweite an
    z=float(psize.value) #psize.value gibt die Pixelgröße an
    fheight=x*y/z #fheight ist die errechnete Flughöhe
    gsd_h.value=str(fheight)

def pixelsize():
    a = float(sensw.value) #sensw.value=Sensorbreite
    b = float(sensh.value) #sensh.value=Sensorhöhe
    asens = a * b #asens=Sensorfläche
    c=float(resh.value)*float(resw.value) #res=Auflösung
    pcount.value=str(c)
    apixel = asens / c #Pixelfläche
    pixels = m.sqrt(apixel) #Kantenlänge Pixel
    psize.value = str(pixels)

def picturecount():
    s = float(resw.value) * (float(gsd_v.value)*10)
    print("s=" + str(s))
    b = s*(1-(float(ppro_v.value)/100))
    print("b=" + str(b))
    nm = float(areal_v.value)/b+1
    nm = round(nm+1)
    print("nm+" + str(nm))
    nl = nm +1
    print("nl=" + str(nl))
    d = s*(1-(float(qpro_v.value)/100))
    print("d=" + str(d))
    nb = float(areaw_v.value)/d+1
    nb = round(nb+1)
    print("nb=" + str(nb))
    n = nl*nb
    print("n=" + str(n))
    pct.value = str(n)


app = App(title="GSD-Berechner", width=550, height=450,layout="grid")
drone_t = Text(app, text="Drohne:", grid=[0,0])
drone=Combo(app, options=["-Custom-","DJI Inspire 1 - Zenmuse X5", "Test"],grid=[1,0], command=update)
gsd_vt = Text(app, text="Gewünschte GSD", grid=[0,1])
gsd_v = TextBox(app, grid=[1,1])
gsd_ht = Text(app, text="Benötigte Höhe", grid=[0,2])
gsd_h = TextBox(app, grid=[1,2])
gsd_c = PushButton(app, text="2.Flughöhe berechnen", command=calcgsd, grid=[1,13])
resw_t = Text(app, text="Auflösung breit", grid=[0,3])
resw = TextBox(app, text=" ", grid=[1,3])
resh_t = Text(app, text="Auflösung hoch", grid=[2,3])
resh = TextBox(app, text=" ", grid=[3,3])
sensw_t = Text(app, text="Sensorbreite", grid=[0,4])
sensw = TextBox(app, text=" ", grid=[1,4])
sensh_t = Text(app, text="Sensorhöhe", grid=[2,4])
sensh= TextBox(app,text=" ", grid=[3,4])
fole_t = Text(app, text="Brennweite", grid=[0,5])
fole = TextBox(app, text=" ", grid=[1,5])
psize_t = Text(app, text="Pixelgröße", grid=[0,6])
psize = TextBox(app, text=" ", grid=[1,6])
pcount_t = Text(app, text="Pixelanzahl", grid=[0,7])
pcount = TextBox(app, text=" ", grid=[1,7])
psize_but = PushButton(app, text="1.Pixelgröße berechnen", command=pixelsize, grid=[0,13])
areaw_t = Text(app, text="Breite des Bereichs in mm", grid=[0,8])
areaw_v = TextBox(app, text=" ", grid=[1,8])
areal_t = Text(app, text="Länge des Bereichs in mm", grid=[0,9])
areal_v = TextBox(app, text=" ", grid=[1,9])
qpro_t = Text(app, text="Querüberdeckung", grid=[0,10])
qpro_v = TextBox(app, text=" ", grid=[1,10])
ppro_t = Text(app, text="Längsüberdeckung", grid=[0,11])
ppro_v = TextBox(app, text=" ", grid=[1,11])
pcbut = PushButton(app, text="Bildanzahl berechnen", command=picturecount, grid=[2,13])
pct = TextBox(app, text="Bildanzahl", grid=[1,12])

app.display()
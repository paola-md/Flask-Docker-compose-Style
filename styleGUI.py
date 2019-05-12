from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import requests
#import base64
import scipy.misc
import time
from art import StyleTransfer


path1='.\\estilos\\vang.jpg'
path2= '.\\estilos\\cubism.jpg'

def browsefunc1():
    filename = filedialog.askopenfilename()
    
    img = resize_image(filename)
    imgEstilo.config(image=img)
    imgEstilo.image = img
    
    #pathlabel.config(text=filename)
    global path1
    path1=filename
    print(path1)
    
def browsefunc2():
    filename = filedialog.askopenfilename()
    
    img = resize_image(filename)
    imgContenido.config(image=img)
    imgContenido.image = img
    
    #pathlabel2.config(text=filename)
    global path2
    path2=filename
    print(path2)

def obtenResultado():
    global img
    ni = entry.get()
    numi = 1
    print(ni)
    if ni != '': 
        numi = int(entry.get())
        print(type(numi))
             
    URL = "http://localhost:5000/"

    response = requests.post(URL, data={"path1":path2, "path2":path1, "numi":numi})
    #print(response.content) 
    #artist = StyleTransfer()
    #time.sleep(20)
    
    #best, best_loss = artist.run_style_transfer(path2, path1, numi)
    #scipy.misc.toimage(best, cmin=0.0, cmax=...).save('outfile.jpg')
    #print("Termine")
    
    img = resize_image("outfile.jpg")
    imgRes.config(image=img)
    
# on change dropdown value
def change_dropdown(*args):
    estilo = tkvar.get() 
    dirEstilos = ".\\estilos\\"
    if estilo == 'Cubismo':
        filename = "cubism.jpg"
    elif estilo == 'Puntillismo':
        filename = "puntillism.jpg"
    else:
        filename = "vang.jpg"
    #choices = {'Cubismo','Puntillismo'}
    path = dirEstilos +  filename
    
    global path2
    path2=path
    print(args)
    img = resize_image(path)
    imgEstilo.config(image=img)
    imgEstilo.image = img
    print( tkvar.get() )
    
def resize_image(path):
    image = Image.open(path)
    [imageSizeWidth, imageSizeHeight] = image.size
    image1 = image.resize((150, 100), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image1)
    return img


window = Tk()
window.title("Bienvenido al estilizador de imagenes")

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=2,row=11, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)


image = Image.open("C.jpg")
#[imageSizeWidth, imageSizeHeight] = image1.size
image1 = image.resize((150, 100), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image1)
imgEstilo = Label(mainframe)
imgEstilo.config(image = img)
#imgEstilo.image = img
imgEstilo.grid(column= 2, row=3)

descripcion = Label(mainframe,text="Elige el estilo a aplicar:")
descripcion.grid(column= 1,row=1)

choices = {'Cubismo','Puntillismo'}

# Create a Tkinter variable
tkvar = StringVar(window)
tkvar.set('Cubismo') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
popupMenu.grid(column= 1,row=2)

# link function to change dropdown
tkvar.trace('w', change_dropdown)


browsebutton = Button(mainframe, text="Otro", command=browsefunc1)
browsebutton.grid(column= 1,row=3)

pathlabel = Label(mainframe)
pathlabel.grid(column= 1,row=4)

descripcionEs = Label(mainframe,text="Elige la imagen a estilizar: ")
descripcionEs.grid(column= 1,row=5)

browsebutton2 = Button(mainframe, text="Browse", command=browsefunc2)
browsebutton2.grid(column= 1,row=6)

image2 = Image.open("C.jpg")
#[imageSizeWidth, imageSizeHeight] = image1.size
image2 = image2.resize((150, 100), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(image2)
imgContenido = Label(mainframe)
imgContenido.config(image = img2)
#imgEstilo.image = img
imgContenido.grid(column= 2, row=6)

pathlabel2 = Label(mainframe)
pathlabel2.grid(column= 1,row=7)

pathlabel3 = Label(mainframe,text='Ingresa la intensidad del estilo (numero)')
pathlabel3.grid(column= 1,row=8)

entry = Entry(mainframe, width=10)
entry.grid(column= 1,row=9)

obtenRes = Button(mainframe, text="Mostrar Resultado",command=obtenResultado)
obtenRes.grid(column= 1,row=11)

image3 = Image.open("C.jpg")
#[imageSizeWidth, imageSizeHeight] = image1.size
image3 = image3.resize((150, 100), Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(image3)
imgRes= Label(mainframe)
imgRes.config(image = img3)
#imgEstilo.image = img
imgRes.grid(column= 2, row=11)



window.mainloop()

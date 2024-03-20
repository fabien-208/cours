import tkinter 

fenetre = tkinter.Tk()
fenetre.title('tesst')
image = tkinter.Canvas(fenetre, width=50, height=50)
for k in range(5):
    image.create_image(k, k+5, image='mine.gif')
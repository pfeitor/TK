from tkinter import *

app = Tk()


app.eval('tk::PlaceWindow %s center' % app.winfo_pathname(app.winfo_id()))

app.geometry('400x200')

app.mainloop()
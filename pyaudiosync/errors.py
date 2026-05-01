import tkinter

def error(msg = "Error: Null"):
    root = tkinter.Tk()
    root.geometry("400x100")
    root.title("Error")

    label = tkinter.Label(root, text="PyAudioSync Error")
    label.pack()

    text = tkinter.Text()
    text.insert(tkinter.END, msg)
    text.pack()

    root.mainloop()
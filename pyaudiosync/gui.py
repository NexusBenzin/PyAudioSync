import tkinter

def gui(device_list):
    root = tkinter.Tk()
    root.title("PyAudioSync")

    Label = tkinter.Label(root, text="PyAudioSync")
    Label.pack()

    listbox = tkinter.Listbox(root, height=20, width=100)
    for i in device_list:
        display_text = f"ID {i['id']}: {i['name']}"
        listbox.insert(tkinter.END, display_text)




    listbox.pack()
    root.mainloop()


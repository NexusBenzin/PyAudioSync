import tkinter
from playing_sounds import play_beep




def gui(device_list, quote):
    selected_device = None

    root = tkinter.Tk()
    root.title("PyAudioSync")
    root.geometry("800x500")

    Label = tkinter.Label(root, text=quote)
    Label.pack()

    listbox = tkinter.Listbox(root, height=20, width=100)
    for i in device_list:
        display_text = f"ID {i['id']}: {i['name']}"
        listbox.insert(tkinter.END, display_text)

    def unselect():
        nonlocal selected_device
        listbox.selection_clear(0, tkinter.END)
        selected_device = 0
        print("current device: None")


    def on_click(event):
        nonlocal selected_device

        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            value = event.widget.get(index)


            try:
                raw_id = value.split(" ")[1].replace(":", " ")
                selected_device = int(raw_id)
                print(f"current device: {selected_device}")
            except:
                print("Could not retrieve device id")






    listbox.bind("<<ListboxSelect>>", on_click)

    btn = tkinter.Button(root, text="Test device", command=lambda: play_beep(selected_device) if selected_device is not None else print("No device selected"))
    btn.pack()

    btn2 = tkinter.Button(root, text="Unselect Device", command=unselect)
    btn2.pack(pady=5)

    listbox.pack()
    root.mainloop()








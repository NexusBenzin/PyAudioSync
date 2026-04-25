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

    btn = tkinter.Button(root, text="Test device", command=lambda: play_beep(selected_device) if selected_device else print("No device selected"))
    btn.pack()

    listbox.pack()
    root.mainloop()








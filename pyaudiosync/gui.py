import tkinter
import playing_sounds as pyas




def gui(device_list, quote):
    selected_devices = None

    root = tkinter.Tk()
    root.title("PyAudioSync")
    root.geometry("800x500")

    Label = tkinter.Label(root, text=quote)
    Label.pack()

    listbox = tkinter.Listbox(root, height=20, width=100, selectmode=tkinter.MULTIPLE)
    for i in device_list:
        display_text = f"ID {i['id']}: {i['name']}"
        listbox.insert(tkinter.END, display_text)

    def unselect():
        nonlocal selected_devices
        listbox.selection_clear(0, tkinter.END)
        selected_devices = []
        print("current device: None")

    def on_click(event):
        nonlocal selected_devices
        indices = listbox.curselection()
        selected_devices = []

        for i in indices:
            value = listbox.get(i)
            try:
                raw_id = value.split(" ")[1].replace(":", "")
                device_id_int = int(raw_id)
                selected_devices.append(device_id_int)
                print(f"Added device ID: {device_id_int}")
            except (ValueError, IndexError):
                print("Could not retrieve device id from selection")






    listbox.bind("<<ListboxSelect>>", on_click)

    btn = tkinter.Button(root, text="Test selected", command=lambda: pyas.play_multiple(selected_devices) if selected_devices is not None else print("No device selected"))
    btn.pack()

    btn2 = tkinter.Button(root, text="Unselect Device", command=unselect)
    btn2.pack(pady=5)

    listbox.pack()
    root.mainloop()








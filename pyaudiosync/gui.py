import tkinter
from pyaudiosync.devices import AudioDeviceManager

beep = AudioDeviceManager


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


            selected_device = value.split(" ")[1].replace(":", " ")
            print(f"current device: {selected_device}")

    listbox.bind("<<ListboxSelect>>", on_click)

    btn = tkinter.Button(root, text="Test device", command=lambda: beep.play_beep(int(selected_device)) if selected_device else print("No device selected"))
    btn.pack()

    listbox.pack()
    root.mainloop()








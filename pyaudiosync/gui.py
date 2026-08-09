import errors
import customtkinter
import test
import play_file as pf




def gui(device_list, quote):
    selected_devices = set()

    try:
        root = customtkinter.CTk()
        root.title("PyAudioSync")
        root.geometry("1920x1080")

        Label = customtkinter.CTkLabel(root, text=quote)
        Label.pack()

        listbox = customtkinter.CTkScrollableFrame(root, width=600, height=600)
        listbox.pack()
    except Exception as e:
        errors.error(f"Could not create main GUI: {e}")

    def toggle_device(device_id):
        if device_id in selected_devices:
            selected_devices.remove(device_id)
        else:
            selected_devices.add(device_id)

    for device in device_list:
        row_frame = customtkinter.CTkFrame(listbox, fg_color="transparent")
        row_frame.pack(fill="x", pady=5, padx=5 )



        cb = customtkinter.CTkCheckBox(row_frame, text="", width=24, command=lambda d_id=device['id']: toggle_device(d_id))
        cb.pack(side="left", anchor="n")


        label = customtkinter.CTkLabel(row_frame, text=f"ID {device['id']}: {device['name']}", wraplength=350, justify="left")
        label.pack(side="left", padx=5, fill="x")

    btn = customtkinter.CTkButton(root, text="Test selected", command=lambda: test.test_multiple(list(selected_devices)) if selected_devices else print("No device selected"))
    btn.pack()

    btn2 = customtkinter.CTkButton(root, text="Play file on selected", command=lambda: pf.play_file_multiple(list(selected_devices)) if selected_devices else print("No device selected"))
    btn2.pack(pady=5)

    root.mainloop()

import customtkinter

def error(msg = "Error: Null"):
    root = customtkinter.CTk()
    root.geometry("900x200")
    root.title("Error")

    label = customtkinter.CTkLabel(root, text="PyAudioSync Error")
    label.pack()

    text = customtkinter.CTkTextbox(root, width=900, height=200)
    text.insert(customtkinter.END, msg)
    text.pack()

    root.mainloop()
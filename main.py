import os
import shutil
import tkinter as tk
import customtkinter
from tkinter import messagebox

class ReadFileFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)

        self.setup_form()

    def setup_form(self):

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # file path text box
        self.textbox = customtkinter.CTkEntry(self, placeholder_text="Loadin zip file", width=120)
        self.textbox.grid(row=0, column=0)

        # Open file explorer button
        self.button_select = customtkinter.CTkButton(self, fg_color="transparent", text_color=("gray10", "#DCE4EE"), command=self.button_select_callback, text="Select zip file")
        self.button_select.grid(row=0, column=1, padx=20)

        # Unzip button
        self.unzip_button = customtkinter.CTkButton(self, command=self.button_unzip_callback, text="Unzip")
        self.unzip_button.grid(row=1, column=1, padx=20)

    def button_select_callback(self):
        # Open file explorer
        file_names = ReadFileFrame.file_read()

        if file_names is not None:
            # Insert file path into text box
            for i in range(len(file_names)):
                self.textbox.insert(0, ",")
                self.textbox.insert(0, file_names[i])
            
    def button_unzip_callback(self):
        # default output directory
        output_dir = "./output"
        duplicate_coutnt = 0

        # Get file path from text box and split by comma
        file_paths = self.textbox.get().split(",")
        # delete last element of list
        del file_paths[-1]

        # Check for duplicate directories
        print(os.path.exists(output_dir))

        while os.path.exists(output_dir):
            duplicate_coutnt += 1
            output_dir = f"./output_{duplicate_coutnt}"

        # Unzip selected files
        for i in range(len(file_paths)):
            if file_paths != "":
                shutil.unpack_archive(file_paths[i], output_dir)

        messagebox.showinfo("Information", f"Unzipped all files! output directory : {output_dir}")

        # delete text box
        self.textbox.delete(0, tk.END)
            

    @staticmethod
    def file_read():
        current_dir = os.path.abspath(os.path.dirname(__file__))
        
        file_paths = tk.filedialog.askopenfilenames(filetype=[("zip file", "*.zip")], initialdir=current_dir)

        if len(file_paths) != 0:
            return file_paths
        else:
            return None

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Set default theme
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # main window settings
        self.geometry("400x300")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # read component
        self.readfile_frame = ReadFileFrame(self)
        self.readfile_frame.grid(row=0, column=0, sticky="nsew")

        

app = App()
app.mainloop()
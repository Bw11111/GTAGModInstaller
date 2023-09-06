import os
from tkinter import messagebox
from tkinter import filedialog
from tkinter import *
import shutil
import configparser
import tkinter as tk
directory = ""
directory2 = ""
gorillatagexe = ""
load = messagebox.askyesno("Load Settings?", "Load Previous Settings?")
if load == True:
    try:
        if os.path.isfile("C:\\Users\\" + os.getlogin() + "\\modconfig.ini") == True:
            config = configparser.ConfigParser()
            config.sections()
            config.read("C:\\Users\\" + os.getlogin() + "\\modconfig.ini")
            directory = config['DIRS']['InstallDir']
            print(config['DIRS']['InstallDir'])
            directory2 = config['DIRS']['DisabledDir']
            gorillatagexe = config["DIRS"]['exe']
            print(config['DIRS']['DisabledDir'])
        else:
            with open("C:\\Users\\" + os.getlogin() + "\\modconfig.ini", "x") as f:
                f.write("[DIRS]")
        
    except:
        with open("C:\\Users\\" + os.getlogin() + "\\modconfig.ini", "x") as f:
                f.write("[DIRS]")
else:
    directory = filedialog.askdirectory()

    messagebox.showinfo("Selected directory for mods", "Mod install directory: " +  directory)
    directory2 = filedialog.askdirectory()
    messagebox.showinfo("Selected directory for disabled mods", "Mod disable directory: " +  directory2)
    gorillatagexe = filedialog.askopenfilename()
    
    with open("C:\\Users\\" + os.getlogin() + "\\modconfig.ini", "w") as file:
        file.write("[DIRS]\nInstallDir = " + directory + "\nDisabledDir = "+ directory2 + "\nexe = " + gorillatagexe)
    

#file = open("C:\\Users\\" + os.getlogin() + "\\modconfig.ini", "w")


app = tk.Tk()
app.geometry("200x200")
app.title("Viva's Mod Installer")
def install_mod():
    dllfile = filedialog.askopenfilename()
    messagebox.showinfo("Selected Mod", "Selected mod: " + dllfile)
    shutil.copy(dllfile,directory)
    os.system("taskkill /f /im \"Gorilla Tag.exe\"")
    os.system(gorillatagexe)
def uninstall_mod():
    dllfile = filedialog.askopenfilename()
    messagebox.showinfo("Selected Mod", "Selected mod: " + dllfile)
    messagebox.showwarning("Warning", "Uninstalling mod")
    os.remove(dllfile)
def disable_mod():
    dllfile = filedialog.askopenfilename()
    messagebox.showinfo("Selected Mod", "Selected mod to disable: " + dllfile)
   
    shutil.move(dllfile, directory2)
def undisable_mod():
    dllfile = filedialog.askopenfilename()
    messagebox.showinfo("Selected Mod", "Selected mod to enable: " + dllfile)
   
    shutil.move(dllfile, directory)
def closegtag():
    os.system("taskkill /f /im \"Gorilla Tag.exe\"")
txt = Label(app, text="Viva's Mod Installer")
txt.pack()

btn = Button(app, text="Install Mod", command=install_mod)
btn.pack()
btn2 = Button(app, text="Disable Mod", command=disable_mod)
btn2.pack()
btn3 = Button(app, text="Re-enable mod", command=undisable_mod)
btn3.pack()
btn4 = Button(app, text="Close Gorilla Tag", command=closegtag)
btn4.pack()
app.mainloop()

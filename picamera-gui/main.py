#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Main

from PiCameraGUI import PiCameraGUI
from Exceptions_ModuleCamera import TkinterError, PiCameraError
from tkinter import Tk, messagebox, PhotoImage
from picamera import PiCamera

# Exécute le programme
def run():
    try:
        win = Tk()
    except:
        messagebox.showerror("Tkinter error", "GUI initialization error")
        raise TkinterError("Tkinter initialization error")
        print("Finished")
        return 0
    
    try:
        camera = PiCamera()  # Mode autre que 0 pour pouvoir changer de mode plus tard
        camera.sensor_mode = 0	# Retourne au mode 0
    except:
        messagebox.showerror("PiCamera error", "Camera initialization error\nIt may be badly installed\nIf it still doesn't work,\nplease restart the system")
        raise PiCameraError("Error creating the PiCamera instance")
        print("Finished")
        return 0
    photo = PhotoImage(file = "../ekamera.png")
    win.iconphoto(False, photo)
    win.resizable(width=False, height=False)
    app = PiCameraGUI(win,camera,title="PiCamera")
    win.mainloop()

    camera.close()
        
# Exécute le programme
if __name__ == "__main__":
    print("Window initialization")
    run()

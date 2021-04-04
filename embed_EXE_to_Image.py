import tkinter as tk
from tkinter import filedialog
from tkinter.font import Font
import psutil
import _thread
import os


def image_path():
    path = filedialog.askopenfilename(initialdir="C:\\", title="Select Image",
                                      filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("All Files", "*.*")))
    path = path.replace('/', '\\')
    image_info.config(text=path)


def exe_path():
    path = filedialog.askopenfilename(initialdir="C:\\", title="Select Image",
                                      filetypes=(("EXE Files", "*.exe"), ("All Files", "*.*")))
    path = path.replace('/', '\\')
    exe_info.config(text=path)


def embed(ignore1, ignore2):
    img_path = image_info['text']
    exe_path = exe_info['text']
    if img_path == "" or exe_path == "":
        print("Enter both fields")
        return
    global end
    print("EXE Embedded to Image...")

    embed_btn.config(state=tk.DISABLED)
    reset_btn.config(state=tk.DISABLED)
    while not file_in_use(img_path):
        if end:
            break
        continue
    embed_btn.config(state=tk.NORMAL)
    reset_btn.config(state=tk.NORMAL)
    if end:
        print("Stopped")
        end = False
        return
    print(img_path + " is in use")
    os.system(exe_path)


def embed_code():
    _thread.start_new_thread(embed, (None, None))


end = False


def stop():
    global end
    embed_btn.config(state=tk.NORMAL)
    end = True


def file_in_use(file_path):
    for proc in psutil.process_iter():
        for item in proc.open_files():
            if file_path == item.path:
                return True
        break
    try:
        with open(file_path, "r+") as f:
            pass
    except (PermissionError, IOError):
        return True
    return False


def reset():
    image_info.config(text="")
    exe_info.config(text="")


HEIGHT = 200
WIDTH = 500
root = tk.Tk()

root.title("Embed EXE to Image")

myFontResult = Font(family='Arial', size=10, weight="bold")
pathFont = Font(family='Arial', size=8)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bgFrame = tk.Frame(root, bg='#423a31')
bgFrame.place(relwidth=1, relheight=1)

select_image = tk.Button(bgFrame, text="Select Image", font=myFontResult, command=image_path)
select_image.place(relx=0.1, rely=0.1, relheight=0.2, relwidth=0.2)

image_info = tk.Label(bgFrame, font=pathFont)
image_info.place(relx=0.3, rely=0.1, relheight=0.2, relwidth=0.6)

select_exe = tk.Button(bgFrame, text="Select EXE", font=myFontResult, command=exe_path)
select_exe.place(relx=0.1, rely=0.4, relheight=0.2, relwidth=0.2)

exe_info = tk.Label(bgFrame, font=pathFont)
exe_info.place(relx=0.3, rely=0.4, relheight=0.2, relwidth=0.6)

embed_btn = tk.Button(bgFrame, text="Embed", font=myFontResult, command=embed_code)
embed_btn.place(relx=0.1, rely=0.75, relheight=0.15, relwidth=0.25)

stop_btn = tk.Button(bgFrame, text="Stop", font=myFontResult, command=stop)
stop_btn.place(relx=0.377, rely=0.75, relheight=0.15, relwidth=0.25)

reset_btn = tk.Button(bgFrame, text="Reset", font=myFontResult, command=reset)
reset_btn.place(relx=0.65, rely=0.75, relheight=0.15, relwidth=0.25)


root.mainloop()
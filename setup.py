from cx_Freeze import setup, Executable

base = None

includefiles = None
executables = [Executable("embed_EXE_to_Image.py", icon=r"C:\Users\Kenneth\PycharmProjects\embedEXEtoImage\iconExe.ico",base=base)]

packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
        'include_files':includefiles
    },
}

setup(
    name="WaveSwapper",
    options=options,
    version="1.0",
    description='Embed an EXE to an Image file',
    executables=executables, requires=['psutil']
)
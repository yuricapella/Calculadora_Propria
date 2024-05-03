from cx_Freeze import setup, Executable

exe = Executable(script="main.py", base="Win32GUI")

setup(
    name="Yuri Capella Dos Santos",
    version="1.0",
    description="Calculadora própria",
    executables=[exe]
)
from color import *

if __name__ == '__main__':
    print("Base:")
    print(Base.FAIL,"This is a test!", Base.END)

    print("ANSI_Compatible:")
    print(ANSI_Compatible.Color(120),"This is a test!", ANSI_Compatible.END)

    print("Formatting:")
    print(Formatting.Bold,"This is a test!", Formatting.Reset)

    print("GColor:") # Gnome terminal supported
    print(GColor.RGB(204,100,145),"This is a test!", GColor.END)

    print("Color:")
    print(Color.F_Cyan,"This is a test!",Color.F_Default)

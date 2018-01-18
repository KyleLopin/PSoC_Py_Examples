# standard libraries
import tkinter as tk


def hello():
    print("hello world")


# root = tk.Tk()
# root.title("Basic GUI")
# root.geometry("300x300")
#
# tk.Button(root, text="Hello", command=hello).pack()
#
# root.mainloop()


#################################

class HelloGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        tk.Button(self, text="Hello", command=hello).pack()

if __name__ == "__main__":
    root = HelloGUI()
    root.title("Basic GUI")
    root.geometry("300x300")
    root.mainloop()

#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
'''GUI tool for killing stuck processes'''

from tkinter import Tk, Label, Button
from subprocess import call


class PkillGui:
    def __init__(self, master):
        self.master = master
        master.title("Kill 'em dead!")

        self.label = Label(master, text='Click a button to murdile a process.')
        self.label.pack()

        # Buttons region
        self.kill_citrix = Button(
            master,
            text='Kill BadApp',
            command=lambda: self.kill_process('BadApp'),
        )
        self.kill_citrix.pack()

        self.kill_bomgar = Button(
            master,
            text='Kill CantStopWontStop',
            command=lambda: self.kill_process('CantStopWontStop'),
        )
        self.kill_bomgar.pack()

        self.quit = Button(
            master,
            text='Quit',
            command=master.quit
        )
        self.quit.pack()

    def kill_process(self, process: str):
        call(['/usr/bin/pkill', '-i', process])


root = Tk()
my_gui = PkillGui(root)
root.mainloop()

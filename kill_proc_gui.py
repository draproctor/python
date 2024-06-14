from tkinter import Tk, Label, Button
from subprocess import call


class PkillGui:
    def __init__(self, master: Tk):
        self.master = master
        master.title("Kill 'em dead!")

        self.label = Label(master, text="Click a button to murdilate a process.")
        self.label.pack()

        # Buttons region
        self.kill_citrix = self.stop_process_button(
            text="Kill BadApp", process_name="BadApp"
        )
        self.kill_bomgar = self.stop_process_button(
            text="Kill CantStopWontStop", process_name="CantStopWontStop"
        )
        self.quit = Button(master, text="Quit", command=master.quit)
        self.quit.pack()

    def stop_process_button(self, text: str, process_name: str) -> Button:
        button = Button(
            self.master,
            text=text,
            command=lambda: call(["/usr/bin/pkill", "-i", process_name]),
        )
        button.pack()
        return button


if __name__ == "__main__":
    root = Tk()
    my_gui = PkillGui(root)
    root.mainloop()

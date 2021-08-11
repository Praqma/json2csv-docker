import subprocess
from tkinter import Tk, Button, Label, filedialog, scrolledtext, Toplevel, END, E, W, CENTER
from subprocess import check_output, run, Popen
from pathlib import Path


window = Tk()
window.title("json2csv")

window_width, window_height = 220, 80
window.geometry(f"{window_width}x{window_height}")

json2csv =  Path(__file__).parent.joinpath("modules/json2csv.cmd") #Path(__file__).parent.absolute().joinpath("modules").joinpath("json2csv")

def open_file():
    done_label.configure(text="")
    f = filedialog.askopenfile()
    file_path = Path(f.name)
    return file_path.parent, file_path


def clicked():
    done_label.configure(text="")
    global file_dir, file
    file_dir, file = open_file()


def convert(dryrun=False):
    cmd = [json2csv, "--unwind", "orderItems", "--flatten-arrays", "--flatten-objects", "-i", file]
    process = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
    process.wait()
    res, err = process.communicate()

    if res:
        if not dryrun:
            with open(file_dir.joinpath(f"{file}.csv"), "w+") as csv:
                csv.write(res.decode())
            done_label.configure(text="Conversion done!")
        else:
            dryrun_window = Toplevel(window)
            dryrun_window.title("Preliminary results")
            dryrun_text = scrolledtext.ScrolledText(dryrun_window)
            dryrun_text.insert(END, res.decode())
            dryrun_text.pack(expand=True)
    else:
        pass
        #print(res.stderr.decode())


def convert_dry_run():
    convert(dryrun=True)


file_chooser = Button(window, text="Open file", command=clicked)
file_chooser.place(relx=0.0, rely=0.5, x=10, y=-10, anchor=W)

convert_file = Button(window, text="Convert", command=convert)
convert_file.place(relx=0.5, rely=0.5, x=5, y=-10, anchor=CENTER)

convert_file_dry_run = Button(window, text="Dry run", command=convert_dry_run)
convert_file_dry_run.place(relx=1.0,rely=0.5, x=-10, y=-10, anchor=E)

done_label = Label(window, text="")
done_label.place(relx=0.5, rely=0.75, anchor=CENTER)

window.mainloop()


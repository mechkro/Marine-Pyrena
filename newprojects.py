import tkinter as tk
from tkinter import ttk
import random
import tkcalendar as tcal
import datetime as dt
import subprocess

x = """After this operation, 14.0 MB of additional disk space will be used.
Get:1 http://mirror.os6.org/raspbian/raspbian buster/main armhf libboost-random1.67.0 armhf 1.67.0-13+deb10u1 [230 kB]
Get:3 http://mirror.os6.org/raspbian/raspbian buster/main armhf qbittorrent armhf 4.1.5-1+deb10u1 [5,294 kB]
Get:2 http://raspbian.phirephly.design/raspbian buster/main armhf libtorrent-rasterbar9 armhf 1.1.11-2 [1,103 kB]
Fetched 6,628 kB in 51s (130 kB/s)
Selecting previously unselected package libboost-random1.67.0:armhf.
(Reading database ... 214533 files and directories currently installed.)
Preparing to unpack .../libboost-random1.67.0_1.67.0-13+deb10u1_armhf.deb ...
Unpacking libboost-random1.67.0:armhf (1.67.0-13+deb10u1) ...
Selecting previously unselected package libtorrent-rasterbar9.
Preparing to unpack .../libtorrent-rasterbar9_1.1.11-2_armhf.deb ...
Unpacking libtorrent-rasterbar9 (1.1.11-2) ...
Selecting previously unselected package qbittorrent.
Preparing to unpack .../qbittorrent_4.1.5-1+deb10u1_armhf.deb ...
Unpacking qbittorrent (4.1.5-1+deb10u1) ...
Setting up libboost-random1.67.0:armhf (1.67.0-13+deb10u1) ...
Setting up libtorrent-rasterbar9 (1.1.11-2) ...
Setting up qbittorrent (4.1.5-1+deb10u1) ...
Processing triggers for mime-support (3.62) ...
Processing triggers for hicolor-icon-theme (0.17-2) ...
Processing triggers for gnome-menus (3.31.4-3) ...
Processing triggers for libc-bin (2.28-10+rpi1) ...
Processing triggers for man-db (2.8.5-2) ...
Processing triggers for desktop-file-utils (0.23-4) ...
pi@raspberrypi:~ $ qbittorrent &\
>
[3] 8067
pi@raspberrypi:~ $ qt5ct: using qt5ct plugin
qt5ct: D-Bus global menu: no
qt5ct: D-Bus system tray: no
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile
libpng warning: iCCP: known incorrect sRGB profile""".splitlines()


class projects:

    def __init__(self, master):
        self.master = master
        self.master.config(bg = "black")
        #self.master.geometry("625x550+25+25")
        self.master.resizable(tk.FALSE, tk.FALSE)

        #FRAME CREATION --------------------------------------
        self.frm1 = tk.Frame(self.master, bg = "black")
        self.frm1.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = tk.NS)
        self.frm2 = tk.Frame(self.master, bg = "black")
        self.frm2.grid(row = 0, column = 1, padx = 10, pady = 10, sticky = tk.NS)

        #PANNED WINDOW 1 (LEFT) ----------------------------------------
        self.p = ttk.Panedwindow(self.frm1, orient=tk.VERTICAL)
        # first pane, which would get widgets gridded into it:
        self.f1 = tk.LabelFrame(self.p, text='Accounts', width=100, height=30, bg = "black", fg = "cyan", font = "terminal 10 bold")
        self.f2 = tk.LabelFrame(self.p, text='Contacts', width=100, height=30, bg = "black", fg = "cyan", font = "terminal 10 bold")   # second pane
        self.f3 = tk.LabelFrame(self.p, text='Vendors', width=100, height=30, bg = "black", fg = "cyan", font = "terminal 10 bold")
        self.f4 = tk.LabelFrame(self.p, text='Projects', width=100, height=30, bg = "black", fg = "cyan", font = "terminal 10 bold")   # second pane
        self.p.add(self.f1)
        self.p.add(self.f2)
        self.p.add(self.f3)
        self.p.add(self.f4)
        self.p.grid(row = 0, column = 0, columnspan = 2)
        self.p.bind("<<EnterChild>>", self.expand)

        self.f1contain = [self.f1,self.f2,self.f3,self.f4]

        #LABELFRAME WIDGETS -----------------------------------------------------------
        self.p1f1widgets()
        self.p2f2widgets()
        self.p3f3widgets()
        self.p4f4widgets()

        containr = [self.lboxf1, self.lboxf2, self.lboxf3, self.lboxf4, self.lboxf11, self.lboxf22, self.lboxf33, self.lboxf44]
        for i in containr:
            for j in range(100):
                chc = random.choice(x)
                i.insert(tk.END, f"{j+1}:{chc}")

        #CALENDAR AND NOTEPAD ----------------------------------------------------------
        today = dt.date.today()
        mindate = dt.date(year=2019, month=12, day=1)
        maxdate = today + dt.timedelta(days=30)

        self.c = tcal.Calendar(self.frm1, font="terminal 12", selectmode='day', locale='en_US',
                   mindate=mindate, maxdate=maxdate, disabledforeground='red', selectforeground = 'white', selectbackground = 'gray2',
                   cursor="hand1")#, year=2018, month=2, day=5)
        self.c.grid(row = 1, rowspan = 8, column = 0, padx = 10, pady = 10, sticky = tk.W)
        #self.c.bind("<<CalendarSelected>>", self.peekentries)

        self.tasklabel = tk.LabelFrame(self.frm2, text = "TaskWarrior", bg = "black", fg = "cyan", font = "terminal 10 bold")
        self.tasklabel.grid(row = 0, column = 0, padx = 5, pady = 3)
        self.npad = tk.Text(self.tasklabel, font = "terminal 7 normal", width = 80, height = 60, bg = "black", fg = "cyan")
        self.npad.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.npad.insert(tk.END, subprocess.check_output(["task", "info"]))


        #BUTTONS FOR ACTIONS --------------------------------------------------------
        self.newbutt = tk.Button(self.frm2, text = "Add New", bg = "black", fg = "cyan", command = lambda: None, font = "terminal 6 normal")
        self.newbutt.grid(row = 1, column = 0, padx = 3, pady = 1, sticky = tk.EW)
        self.annbutt = tk.Button(self.frm2, text = "Annotate", bg = "black", fg = "cyan", command = lambda: None, font = "terminal 6 normal")
        self.annbutt.grid(row = 2, column = 0, padx = 3, pady = 1, sticky = tk.EW)
        self.donebutt = tk.Button(self.frm2, text = "Done", bg = "black", fg = "cyan", command = lambda: None, font = "terminal 6 normal")
        self.donebutt.grid(row = 3, column = 0, padx = 3, pady = 1, sticky = tk.EW)

        self.taskcalendar = tk.Button(self.frm1, text = "Calendar", bg = "black", fg = "cyan", command = lambda: self.taskcommand("calendar"), font = "terminal 6 normal")
        self.taskcalendar.grid(row = 1, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.taskburn = tk.Button(self.frm1, text = "Burndown", bg = "black", fg = "cyan", command = lambda: self.taskcommand("burndown"), font = "terminal 6 normal")
        self.taskburn.grid(row = 2, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.tasksummary = tk.Button(self.frm1, text = "Summary", bg = "black", fg = "cyan", command = lambda: self.taskcommand("summary"), font = "terminal 6 normal")
        self.tasksummary.grid(row = 3, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.taskstats = tk.Button(self.frm1, text = "Stats", bg = "black", fg = "cyan", command = lambda: self.taskcommand("stats"), font = "terminal 6 normal")
        self.taskstats.grid(row = 4, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.tasksync = tk.Button(self.frm1, text = "Sync", bg = "black", fg = "cyan", command = lambda: self.taskcommand("sync"), font = "terminal 6 normal")
        self.tasksync.grid(row = 5, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.tasktags = tk.Button(self.frm1, text = "Tags", bg = "black", fg = "cyan", command = lambda: self.taskcommand("tags"), font = "terminal 6 normal")
        self.tasktags.grid(row = 6, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.taskproj = tk.Button(self.frm1, text = "Projects", bg = "black", fg = "cyan", command = lambda: self.taskcommand("projects"), font = "terminal 6 normal")
        self.taskproj.grid(row = 7, column = 1, padx = 3, pady = 1, sticky = tk.EW)
        self.taskexport = tk.Button(self.frm1, text = "Exports", bg = "black", fg = "cyan", command = lambda: self.taskcommand("export"), font = "terminal 6 normal")
        self.taskexport.grid(row = 8, column = 1, padx = 3, pady = 1, sticky = tk.EW)


    #------------------------------------------------
    def taskcommand(self, comm):
        """ """
        self.npad.delete(1.0, tk.END)
        self.npad.insert(tk.END, subprocess.check_output(["task", f"{comm}"]))


    #------------------------------------------------
    def expand(self, event):
        """ """
        pan = event.widget.identify(0,event.x, event.y)#identify(event.x,event.y)
        print(pan)


    #------------------------------------------------
    def shrink(self, event):
        """ """
        for i in self.f1contain:
            if i == event.widget:
                i.config(height = 50)
            else:
                i.config(height = 25)


    #------------------------------------------------
    def p1f1widgets(self):
        """ """
        #LABELFRAME 1 WIDGETS -----------------------------------------------------------
        self.labf1 = tk.Label(self.f1, text = 'Account List', font = "terminal 6 normal", bg = "black", fg = "cyan").grid(row = 0, column = 0, padx = 2, pady = 2)
        self.entf1 = tk.Entry(self.f1, width = 15, font = "terminal 6 normal", bg = "black", fg = "cyan")
        self.buttf1 = tk.Button(self.f1, text = 'Add NEW', font = "terminal 6 normal", command = lambda: None, bg = "black", fg = "cyan")
        self.entf1.grid(row = 1, column = 0, padx = 2, pady = 2)
        self.buttf1.grid(row = 2, column = 0, padx = 2, pady = 2, sticky = tk.EW)

        self.f1scroll = tk.Scrollbar(self.f1, orient = tk.VERTICAL)
        self.f11scroll = tk.Scrollbar(self.f1, orient = tk.VERTICAL)

        self.lboxf1 = tk.Listbox(self.f1, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f1scroll.set, bg = "black", fg = "cyan")
        self.lboxf1.grid(row = 0, rowspan = 3, column = 1, padx = 2, pady = 2)
        self.lboxf11 = tk.Listbox(self.f1, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f11scroll.set, bg = "black", fg = "cyan")
        self.lboxf11.grid(row = 0, rowspan = 3, column = 3, padx = 2, pady = 2)

        self.f1scroll.config(command = self.lboxf1.yview)
        self.f11scroll.config(command = self.lboxf11.yview)
        self.f1scroll.grid(row = 0, rowspan = 3, column = 2, sticky = tk.NS)
        self.f11scroll.grid(row = 0, rowspan = 3, column = 4, sticky = tk.NS)

    #------------------------------------------------
    def p2f2widgets(self):
        """
        CONTACTS:

        """
        #LABELFRAME 2 WIDGETS -----------------------------------------------------------
        self.labf2 = tk.Label(self.f2, text = 'Label 1', font = "terminal 6 normal", bg = "black", fg = "cyan").grid(row = 0, column = 0, padx = 2, pady = 2)
        self.entf2 = tk.Entry(self.f2, width =15, font = "terminal 6 normal", bg = "black", fg = "cyan")
        self.buttf2 = tk.Button(self.f2, text = 'Button 1', font = "terminal 6 normal", command = lambda: None, bg = "black", fg = "cyan")
        self.entf2.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.buttf2.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.f2scroll = tk.Scrollbar(self.f2, orient = tk.VERTICAL)
        self.f22scroll = tk.Scrollbar(self.f2, orient = tk.VERTICAL)

        self.lboxf2 = tk.Listbox(self.f2, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f2scroll.set, bg = "black", fg = "cyan")
        self.lboxf2.grid(row = 0, rowspan = 3, column = 1, padx = 2, pady = 2)
        self.lboxf22 = tk.Listbox(self.f2, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f22scroll.set, bg = "black", fg = "cyan")
        self.lboxf22.grid(row = 0, rowspan = 3, column = 3, padx = 2, pady = 2)

        self.f2scroll.config(command = self.lboxf2.yview)
        self.f22scroll.config(command = self.lboxf22.yview)
        self.f2scroll.grid(row = 0, rowspan = 3, column = 2, sticky = tk.NS)
        self.f22scroll.grid(row = 0, rowspan = 3, column = 4, sticky = tk.NS)

    #------------------------------------------------
    def p3f3widgets(self):
        """
        VENDORS:

        """
        #LABELFRAME 3 WIDGETS -----------------------------------------------------------
        self.labf3 = tk.Label(self.f3, text = 'Vendors', font = "terminal 6 normal", bg = "black", fg = "cyan").grid(row = 0, column = 0, padx = 2, pady = 2)
        self.entf3 = tk.Entry(self.f3, width = 15, font = "terminal 6 normal", bg = "black", fg = "cyan")
        self.buttf3 = tk.Button(self.f3, text = 'Ok', font = "terminal 6 normal", command = lambda: None, bg = "black", fg = "cyan")
        self.entf3.grid(row = 1, column = 0, padx = 2, pady = 2)
        self.buttf3.grid(row = 2, column = 0, padx = 2, pady = 2)

        self.f3scroll = tk.Scrollbar(self.f3, orient = tk.VERTICAL)
        self.f33scroll = tk.Scrollbar(self.f3, orient = tk.VERTICAL)

        self.lboxf3 = tk.Listbox(self.f3, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f3scroll.set, bg = "black", fg = "cyan")
        self.lboxf3.grid(row = 0, rowspan = 3, column = 1, padx = 2, pady = 2)
        self.lboxf33 = tk.Listbox(self.f3, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f33scroll.set, bg = "black", fg = "cyan")
        self.lboxf33.grid(row = 0, rowspan = 3, column = 3, padx = 2, pady = 2)

        self.f3scroll.config(command = self.lboxf3.yview)
        self.f33scroll.config(command = self.lboxf33.yview)
        self.f3scroll.grid(row = 0, rowspan = 3, column = 2, sticky = tk.NS)
        self.f33scroll.grid(row = 0, rowspan = 3, column = 4, sticky = tk.NS)


    #------------------------------------------------
    def p4f4widgets(self):
        """
        PROJECTS:

        """

        #LABELFRAME 4 WIDGETS -----------------------------------------------------------
        self.labf4 = tk.Label(self.f4, text = 'Projects', font = "terminal 6 normal", bg = "black", fg = "cyan").grid(row = 0, column = 0, padx = 2, pady = 2)
        self.entf4 = tk.Entry(self.f4, width = 15, font = "terminal 6 normal", bg = "black", fg = "cyan")
        self.buttf4 = tk.Button(self.f4, text = 'Search', font = "terminal 6 normal", command = lambda: None, bg = "black", fg = "cyan")
        self.entf4.grid(row = 1, column = 0, padx = 5, pady = 5)
        self.buttf4.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.f4scroll = tk.Scrollbar(self.f4, orient = tk.VERTICAL)
        self.f44scroll = tk.Scrollbar(self.f4, orient = tk.VERTICAL)

        self.lboxf4 = tk.Listbox(self.f4, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f4scroll.set, bg = "black", fg = "cyan")
        self.lboxf4.grid(row = 0, rowspan = 3, column = 1, padx = 2, pady = 2)
        self.lboxf44 = tk.Listbox(self.f4, width = 50, height = 7, font = "terminal 6 normal", yscrollcommand = self.f44scroll.set, bg = "black", fg = "cyan")
        self.lboxf44.grid(row = 0, rowspan = 3, column = 3, padx = 2, pady = 2)

        self.f4scroll.config(command = self.lboxf4.yview)
        self.f44scroll.config(command = self.lboxf44.yview)
        self.f4scroll.grid(row = 0, rowspan = 3, column = 2, sticky = tk.NS)
        self.f44scroll.grid(row = 0, rowspan = 3, column = 4, sticky = tk.NS)


#------------------------------------------------
if __name__ == "__main__":
    """ """
    root = tk.Tk()
    root.wm_attributes("-alpha", "0.25")
    root.title("DXP")
    projects(root)
    root.mainloop()

from tkinter import ttk
from license_plate import *
from car_data import Settings
from car_output import create_doc
import sys


class Window:

    def __init__(self):
        # Creating the window
        self.tab1 = None
        self.window = Tk()
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        self.window.geometry('%dx%d' % (width, height))
        self.window.title('Welcome to CARS!')

        # Creating a search portion for the window
        start = ttk.Frame(self.window)
        start.grid(column=0, row=0)
        lbl = Label(start, text='Type license-plate here')
        lbl.grid(column=0, row=0)
        self.txt = Entry(start, width=10, justify='center')
        self.txt.grid(column=1, row=0)
        self.txt.focus()
        btn = Button(start, text='start search', command=self.clicked, justify='right')
        btn.grid(column=3, row=0)

        # Creating a control notebook for the tabs
        self.tab_control = ttk.Notebook(self.window)
        self.tab_control.grid(row=1, sticky='NW', columnspan=420)
        self.txt.bind('<Return>', (lambda event: self.clicked()))
        self.txt.bind('<*>', (lambda event: sys.exit()))

        # Start main loop
        self.window.mainloop()

        """Defining the function of the search button"""

    def clicked(self):
        # Clear all the tabs and variables and set up the settings
        cd = Settings()
        i = self.tab_control.index('end')
        while i > 0:
            self.tab_control.forget(i - 1)
            i -= 1

            # Create the very first tab for the main API response
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text='General')

        # Set up the base API response and retrieve the license-plate
        kenteken = self.txt.get().upper()
        url = cd.base_url + kenteken
        append_tab(cd, url, self.tab1)
        i = 0

        # If any additional APIs are found in the previous API, search through those and add another tab
        for item in cd.additional_urls:
            tab = ttk.Frame(self.tab_control)
            string = cd.additional_urls_titles[i]
            # Make sure you do not include the 'api_gekentekende_voertuigen_' and set it as a title
            title = string[28:]
            cd.titles.append(title)
            self.tab_control.add(tab, text=title)
            # Create the data within the tab
            url = item + '?kenteken=' + kenteken
            append_tab(cd, url, tab)
            i += 1
        create_doc(cd.dict_output, cd.titles, kenteken)


w = Window()

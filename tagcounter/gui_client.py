from tkinter import *
from .scraper import Scraper
from .data_access import DataAccess


class GUIClient:

    def __init__(self):
        root = Tk()
        root.title("Tag Counter")

        self.site_name = StringVar()

        name_label = Label(text="Enter site name or synonym:")
        name_label.grid(row=0, column=0, sticky="w")

        name_entry = Entry(textvariable=self.site_name)

        name_entry.grid(row=0, column=1, padx=5, pady=5)

        download_button = Button(text="Download", command=self.download)
        download_button.grid(row=2, column=0, padx=5, pady=5)

        view_button = Button(text="View", command=self.view)
        view_button.grid(row=2, column=1, padx=5, pady=5)

        self.output = Text(root, height=10, width=35, state=DISABLED)
        self.output.grid(row=3, columnspan=2, padx=10, pady=10)

        self.status = Text(root, height=5, width=35, state=DISABLED)
        self.status.grid(row=4, columnspan=2, padx=10, pady=10)

        root.mainloop()

    def view(self):
        self.output.config(state="normal")
        self.status.config(state="normal")

        da = DataAccess()
        report = da.get(self.site_name.get())

        self.output.delete(1.0, END)
        self.output.insert(END, report)
        self.output.config(state=DISABLED)

        self.status.insert(END, f"\nTags for {self.site_name} have been read from database.")
        self.status.config(state=DISABLED)

    def download(self):
        Scraper.scrape(self.site_name.get())
        self.status.config(state="normal")
        self.status.insert(END, f"\nTags for {self.site_name} have been scraped.")
        self.status.config(state=DISABLED)

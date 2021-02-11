from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import validators
import urllib.request


def Crawl(arg=None):
    # Checking for blank url
    if url_entry.get() == '':
        ms.showerror('Oops', 'This field requires URL!')

    else:
        # Giving url
        url = url_entry.get()

        # Checking if given URL is valid
        if not validators.url(url):
            ms.showerror('Error', 'Enter a valid URL!')
        # Reading all content
        content = urllib.request.urlopen(url).read()

        # Passing the content to function
        soup = BeautifulSoup(content, features="lxml")

        # Storing html in one variable
        info = soup.prettify()

        # Creating New Window
        root = tk.Toplevel()

        # Creating Title
        root.title('URL Crazy')

        # Creating title icon
        root.iconbitmap('img/spider.ico')

        # Locking the window size
        root.resizable(width=False, height=False)

        # Adding scrollbar to the window
        scrollbar = Scrollbar(root)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Using text widget to show scraped content
        text = Text(root, yscrollcommand=scrollbar.set, wrap=WORD)
        text.insert(INSERT, info)
        text.pack()

        # Scroll bar settings
        scrollbar.config(command=text.yview)

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
        
        
        crawler = tk.Tk()

        # Creating size of window
        crawler.geometry('500x500')

        # Doesn't let the window size to be changeable
        crawler.resizable(width=False, height=False)

        # Creating Title
        crawler.title('URL Crazy')

        # Creating title icon
        crawler.iconbitmap('img/spider.ico')

        # Top Frame
        top_frame = Label(crawler, text='WEB CRAWLER',font = ('Cosmic', 25, 'bold'), bg='#778899', fg='white', relief='groove',padx=500, pady=30, bd='5')
        top_frame.pack(side='top')

        canvas = Canvas(crawler, width=500, height=500)

        image = ImageTk.PhotoImage(Image.open('img/img1.jpg'))

        #Positioning Image
        canvas.create_image(0,0, anchor=NW, image=image)
        canvas.pack()
        
        # Creating Frame
        frame = LabelFrame(crawler, padx=30, pady=40, bg='#F5FFFA', bd='5', relief='groove')
        frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        # Label 
        url_add = tk.Label(frame, text = 'Enter a URL or Web Address',font=('Arial',12, 'bold'),bg='white', fg='#778899').pack()

        # Entry or Input
        url_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#B0C4DE', width='30')

        # Returning value to the function
        url_entry.bind('<Return>', Crawl)

        # Setting focus for input
        url_entry.focus_set()

        # Placing the button
        url_entry.pack()

        # Label for seperating Buttons
        label = Label(frame, bg='white').pack()

        # Creating Submit button and positioning it
        crawl = tk.Button(frame, text = "Go", width="10", bd = '3', command = Crawl, font = ('Times', 12, 'bold'), bg='#778899',relief='groove', justify = 'center', pady='5').pack()

        # Creating window only once
        crawler.mainloop()


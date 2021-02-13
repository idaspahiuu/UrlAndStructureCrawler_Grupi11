from tkinter import *
import tkinter as tk
from tkinter import messagebox as ms
from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import validators
import urllib.request


def Scrape(arg=None):
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

def About(arg=None):
    root = Tk()
    root.geometry("500x500")

    # specify size of window.
    root.title("URL Crazy")
    root.iconbitmap("img/spider.ico")

    # Create text widget and specify size.
    T = Text(root, height=20, width=50)

    # Create label
    l = Label(root, text="Web Crawling")
    l.config(font=("Courier", 14))

    Fact = """
    A web crawler, spider or search engine bot do-wnloads and indexes content from all over the Internet. The goal of such a bot is to  learn what(almost) every webpage on the web is  about, so that  the information can be retrieved when it's needed.     They're called "web crawlers" because crawli-ng is the technical term for automatically accessi-ng a website and obtaining data via a software pro-   gram. A web crawler bot is like someone who goes through all the books in a disorganized libra-ry  and puts together a card catalog so that anyo-ne   who visits the library can quickly and easily find the information they need. To help categori-ze and sort the library's books by topic, the organizer will read the title, summary, and some of   the internal text of each book to figure out what it's about."""

    # Create button for next text.

    # Create an Exit button.
    b2 = Button(root, text="Exit",
                command=root.destroy)

    l.pack()
    T.pack()
    b2.pack()

    # Insert The Fact.
    T.insert(tk.END, Fact)

    tk.mainloop()

def donothing():
    x = 0


crawler = tk.Tk()

# Creating size of window
crawler.geometry('500x500')

# Doesn't let the window size to be changeable
crawler.resizable(width=False, height=False)

# Creating Title
crawler.title('URL Crazy')

# Creating title icon
crawler.iconbitmap('img/spider.ico')

# Creating menubar
menubar = Menu(crawler)
choose = Menu(menubar, tearoff=0)
choose.add_command(label="Scrape", command=donothing)
choose.add_separator()
choose.add_command(label="Exit", command=crawler.quit)
menubar.add_cascade(label="Choose", menu=choose)

aboutmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=aboutmenu)
aboutmenu.add_command(label="About", command=About)


# Top Frame
top_frame = Label(crawler, text='WEB CRAWLER', font=('Cosmic', 25, 'bold'), bg='#778899', fg='white', relief='groove',
                  padx=500, pady=30, bd='5')
top_frame.pack(side='top')

canvas = Canvas(crawler, width=500, height=500)

image = ImageTk.PhotoImage(Image.open('img/img1.jpg'))

# Positioning Image
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()

# Creating Frame
frame = LabelFrame(crawler, padx=30, pady=40, bg='#F5FFFA', bd='5', relief='groove')
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Label
url_add = tk.Label(frame, text='Enter a URL or Web Address', font=('Arial', 12, 'bold'), bg='white',
                   fg='#778899').pack()

# Entry or Input
url_entry = tk.Entry(frame, font=('calibre', 10, 'normal'), justify='center', bg='#B0C4DE', width='30')

# Returning value to the function
url_entry.bind('<Return>', Scrape)
# Setting focus for input
url_entry.focus_set()

# Placing the button
url_entry.pack()

# Label for seperating Buttons
label = Label(frame, bg='white').pack()

# Creating Submit button and positioning it
crawl = tk.Button(frame, text="Go", width="5", bd='3', command=Scrape, font=('Times', 12, 'bold'), bg='#778899',
                  relief='groove', justify='left', pady='5').pack()


# Creating window only once
crawler.config(menu=menubar)
crawler.mainloop()


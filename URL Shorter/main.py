#liblary improtation
from tkinter import *
from tkinter import ttk
import pyshorteners
import webbrowser

#main window setings
root=Tk()
root.title("URL Shortener")
root.geometry("500x250")
root.resizable(0, 0)

#Main Title Label
Label=ttk.Label(root, text="URL Shortener", font=('Popping', 25))
Label.grid(row=0)

#input label
url_input=ttk.Label(root,text="Enter URL: ")
url_input.grid(row=1, column=0, pady=10)

#input fied for URL
url=StringVar()
url_entry=ttk.Entry(root, textvariable=url, width=40)
url_entry.grid(row=1, column=1, pady=10)

#BTN for short URL
Shorten_button=ttk.Button(root, text="Shorten", command=lambda: shorten_url(url.get()))
Shorten_button.grid(row=2,column=0, pady=10)

#Label for shorted url
Shorten_url_label=ttk.Label(root, text="Shortened URL: ")
Shorten_url_label.grid(row=4, column=0, pady=10)

#input field for output URL
output_url=StringVar()
output_url_entry=ttk.Entry(root, textvariable=output_url, width=40)
output_url_entry.grid(row=4, column=1, pady=10)

#button for copy URL
copy_button=ttk.Button(root, text="COPY", command=lambda: copy_url(output_url.get()))
copy_button.grid(row=5, column=0, pady=10)

#open button
open_button=ttk.Button(root, text="OPEN", command=lambda: open_url(url.get()))
open_button.grid(row=5, column=1, pady=10)


#Function to get the shortened URL and display it
def shorten_url(url):
    try:
        shorten_url=pyshorteners.Shortener().tinyurl.short(url)
        output_url.set(shorten_url)
    except:
        print("Incorrect URL Entered !!")
        
#function to copy URL
def copy_url(url):
    try:
        url_entry.clipboard_clear()
        url_entry.clipboard_clear(url)
        print("URL Copied to clipboard")
    except:
        print("INVAILD URL")
        
#function to open URL
def open_url(url):
    try:
        webbrowser.open(url)
    except:
        print("invaild URL")

root.mainloop()
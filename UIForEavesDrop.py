from tkinter import *
import requests
from bs4 import BeautifulSoup
import re

def display(url):
    text = Text(root)
    text.grid(row=1, columnspan=8)
    source = requests.get(url).text
    text.insert(INSERT, source)

def show_year(url):
    year = Menubutton(root, text="Logs", relief=RAISED)
    year.grid(row=0, column=3)
    year.menu = Menu(year, tearoff=0)
    year["menu"] = year.menu

    source = requests.get(url).text
    soup = BeautifulSoup(source)
    for project in soup.find_all('a'):
        x = project.text
        year.menu.add_command(label=x, command=lambda i=project['href']: display(url+i))


def show_log(url, name):
    letter = Menubutton(root, text=name, relief=RAISED)
    letter.grid(row=0, column=2)
    letter.menu = Menu(letter, tearoff=0)
    letter["menu"] = letter.menu

    source = requests.get(url).text
    soup = BeautifulSoup(source)
    for project in soup.find_all('a'):
        x = project.text
        letter.menu.add_command(label=x, command=lambda i=project['href']: (display(url+i) if name == "Logs" else show_year(url+i)))


def show_project(url, i):
    p = Menubutton(root, text="Project", relief=RAISED)
    p.grid(row=0, column=1)
    p.menu = Menu(p, tearoff=0)
    p["menu"] = p.menu

#***** the p button should be it's own function along with all of the other buttons for overwriting ****

    name = ("Logs" if i == r"/irclogs/" else "Years")

    source = requests.get(url).text
    soup = BeautifulSoup(source)
    for project in soup.find_all('a'):
        x = project.text
        p.menu.add_command(label=x, command=lambda n=project['href']: show_log(url+n, name))

#************* Start **********

root = Tk()
root.geometry("600x600")

t = Menubutton(root, text="Type", relief=RAISED)
t.grid(row=0, column=0)
t.menu = Menu(t, tearoff=0)
t["menu"] = t.menu

url = "http://eavesdrop.openstack.org"

source = requests.get(url).text
soup = BeautifulSoup(source)
for ty in soup.find_all('a'):
    x = ty.text
    t.menu.add_command(label=x, command=lambda i=ty['href']: show_project(url+i, i))

root.mainloop()

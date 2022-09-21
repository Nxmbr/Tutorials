from asyncore import read
from bs4 import BeautifulSoup

# Open the simple html file we wrote as read only so that
# we can parse it into content and manipulate it with BeautifulSoup
with open('home.html', 'r') as html_file:
    
    content = html_file.read()
    
    # Make a new BeautifulSoup object that will contain the methods we can use for webscraping
    soup = BeautifulSoup(content, 'lxml')
    

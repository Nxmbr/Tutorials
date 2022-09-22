from asyncio import *
from bs4 import BeautifulSoup

# Open the simple html file we wrote as read only so that
# we can parse it into content and manipulate it with BeautifulSoup
with open('home.html', 'r') as html_file:
    
    content = html_file.read()
    
    # Make a new BeautifulSoup object that will contain the methods we can use for webscraping
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(f'{course_name} costs {course_price}')
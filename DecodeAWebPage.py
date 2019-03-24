import requests #Getting html from a site
from bs4 import BeautifulSoup #parses that disgustingness from requests (ty bs)

# Use the BeautifulSoup and requests Python packages to print out a list
# of all the article titles on the New York Times homepage.
# https://www.nytimes.com/

# I poked around a bit and even looked in the comments at some of the videos
# but nothing worked, so I went to the solution on this one.  4 chilis, not
# so disappointed in myself for finally breaking on a problem. I did add
# comments so I would understand it.

if __name__ == '__main__':
    base_url = 'http://www.nytimes.com' # the url
    r = requests.get(base_url) #the source code
    soup = BeautifulSoup(r.text,features="html.parser") #the html goes into BeautifulSoup
    print("0") #Are we even getting to the loop? Yes
    print(soup.find_all(class_="story-heading")) #there's nothing in class_="story-heading"
    for story_heading in soup.find_all(class_="story-heading"): # a list of found bits of the soup that contains the class "story-heading"
        print("1") #the "Solution" isn't working, so I added this to test if the loop did anything, and it doesn't?
        if story_heading.a: #link version
            print(story_heading.a.text.replace("\n", " ").strip())
        else: #not a link version
            print(story_heading.contents[0].strip())
    
#       MORAL OF THE CODE
#        It doesn't work
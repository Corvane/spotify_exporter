import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#put playlist link in url1 variable
url1 = 'https://open.spotify.com/playlist/0MfsDiMAzW1lopCNpjhnKG?si=6e8515fcd6d54737&nd=1' 
html = urllib.request.urlopen(url1).read()
soup = BeautifulSoup (html, 'html5lib')
tag_data = soup.find_all('button')

i = 0
list_of_songs = []

#Find text and isert there a desired separator

def spoty_list(text):
    splitted_text = text.rsplit(' - ')
    list_of_songs.append(splitted_text[1] + ' - ' + splitted_text[2] + '\n')
    return list_of_songs

#Extracting Song Name and Artist Name as a string to list:
tag_data = soup.find_all('button')
for tag_text in tag_data:
    text = tag_text.get_text(' - ')

    if text == 'Open App' or text == '':
        continue
    else:
        list_to_write = spoty_list(text)


string_songs= ''
for i in list_to_write:
    string_songs = string_songs + i

#additional print for testing
print (string_songs)


f = open ('list.txt', 'w', encoding="utf-8")
f.write(string_songs)
f.close()





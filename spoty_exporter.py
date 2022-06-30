import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url1 = 'https://open.spotify.com/playlist/0MfsDiMAzW1lopCNpjhnKG?si=6e8515fcd6d54737&nd=1' #my playlist
url2 = 'https://open.spotify.com/playlist/37i9dQZF1DWZHuNxMieWwk'
html = urllib.request.urlopen(url1).read()
# f = open ('SpotifyPlaylist.html')
i = 0
songs_list={}
list_of_songs = []
soup = BeautifulSoup (html, 'html5lib')
tag_data = soup.find_all('button')

#Find text and isert there a desired separator
#print (tag_data[5].get_text('|'))

def spoty_dict(text):
    splitted_text = text.rsplit(' - ')
    name = splitted_text[1]
    artist = splitted_text[2]
    songs_list[name] = artist
    return songs_list

def spoty_list(text):
    splitted_text = text.rsplit(' - ')
    list_of_songs.append(splitted_text[1] + ' - ' + splitted_text[2] + '\n')
    return list_of_songs


#Extracting Song Name and Artist Name as a string to list:
tag_data = soup.find_all('button')
for tag_text in tag_data:
    text = tag_text.get_text(' - ')
#    print (text)
    if text == 'Open App' or text == '':
        continue
    else:
        # spoty_dict (text)
        list_to_write = spoty_list(text)
# print (list_to_write)

string_songs= ''
for i in list_to_write:
    string_songs = string_songs + i
print (string_songs)


f = open ('list.txt', 'w', encoding="utf-8")
f.write(string_songs)
f.close()





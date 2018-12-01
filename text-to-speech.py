from gtts import gTTS
import webbrowser
import os 
import re 
from mutagen.mp3 import MP3

f= open("guru99.txt","r+")

#mytext ='C:/Users/CAU VANG/eclipse-workspace/doan3/guru99.txt'
content = f.read()
print('Noi dung file cua ban la:\n', str)

# language in which you want to convert
language ='en'
#language='vi'

tts = gTTS(text=str(content) ,lang=language,slow =False)

# saving the converted audio in mp3 file named
# welcome
tts.save("hello.mp3") 

os.System("mpg321 hello.mp3")


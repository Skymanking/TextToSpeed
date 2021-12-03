import gtts
from playsound import playsound
with open('text.txt', 'r', encoding='UTF-8') as f:
    data = f.read()
print(data)
tts = gtts.gTTS(data, lang="vi")
tts.save("hello.mp3")
playsound("hello.mp3")
f.close()


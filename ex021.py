from pygame import mixer
from time import sleep
musica = 'C:/Users/Raphael/Desktop/PythonAula/ex021-1.mp3'
mixer.init()
mixer.music.load(musica)
mixer.music.play()
sleep(2)
musica = 'C:/Users/Raphael/Desktop/PythonAula/ex021-2.mp3'
mixer.music.load(musica)
mixer.music.play()
x = input()

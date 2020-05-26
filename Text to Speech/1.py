from tkinter import *
from gtts import gTTS
import os
class text_voice:

    def __init__(self):
        
        self.gui = Tk()
        self.label = Label(self.gui,text = "Enter the text you want as voice:")
        self.text = StringVar(self.gui)
        self.entry = Entry(self.gui,textvariable = self.text)
        self.button = Button(self.gui,text = "Press me to hear the voice", command = self.voice)
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.gui.mainloop()

        
    def voice(self):
        
        self.txt = self.entry.get()
        self.tts=gTTS(text=self.txt,lang="en")
        self.tts.save("voice.mp3")
        os.system("voice.mp3")

text_voice()

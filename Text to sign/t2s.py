from tkinter import *
from PIL import ImageTk, Image

class text_speech:
    
    def __init__(self):

        self.master= Tk()
        self.master.geometry("500x600")


        Label(self.master,text="Enter the text you want to convert to sign language").pack()
        self.value=StringVar(self.master)
        self.e1=Entry(self.master,textvariable=self.value)
        self.e1.pack()

        self.button = Button(self.master,text="Press me to convert",command=self.convert)
        self.button.pack()

        self.master.mainloop()

    def convert(self):
        self.result=self.value.get()
        self.result=self.result.strip()
        self.result=self.result.lower()
        self.result=self.result.split()
        self.word=[]
        self.f=open("Common Words/words.txt")
        for wd in self.f:
            if("\n" in wd):
                wd=wd[:-1]
            self.word.append(wd)
        self.f.close()
        for i in self.result:
            if i in self.word:
                img_label=Label(self.master)
                imgg=PhotoImage(file="Common Words/"+i+".PNG")
                img_label.image=imgg
                img_label['image']=img_label.image
                img_label.pack(side=LEFT)
            else:
                for j in i:
                    img_label=Label(self.master)
                    imgg=PhotoImage(file="Alphabets/"+j+".PNG")
                    img_label.image=imgg
                    img_label['image']=img_label.image
                    img_label.pack(side=LEFT)

text_speech()

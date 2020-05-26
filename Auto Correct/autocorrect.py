import enchant
from tkinter import *
from gtts import gTTS
import os


class autocorrect:

    '''
        Module to help dyslexic persons write/type without errors.
        This module gives 4 predictions based on relative equality, based on modified mon-edit
        Predictions are complemented with voice and image.
    '''
    
    def __init__(self):
        '''
            Initialize the class object.
            Param : None
            Return : None
        '''
        self.root = Tk()
        self.root.geometry("300x150")
        self.all = ""
        self.get_string()
        self.show = Label(self.root,text = "")
        self.show.pack(side = BOTTOM)
        self.root.mainloop()

    def fix_text(self):
        '''
            Takes text
            Calls other functions
            To Predict
            Param : None
            Return : None
        '''
        self.string = self.str.get()
        self.ln = len(self.string)
        self.dict = enchant.Dict("en_US") #change language as per need
        self.sentence = self.dict.suggest(self.string)
        self.comparision = {}
        self.predict2()
        self.display()

    def get_string(self):
        self.label1 = Label(self.root,text = "Please Enter the text : ")
        self.str = StringVar(self.root)
        self.e1 = Entry(self.root,textvariable = self.str)
        self.label1.pack()
        self.e1.pack()
        self.button = Button(self.root,text = "Press me once done to get predictions", command = self.fix_text)
        self.button.pack()

    def min_edit(self,str1,str2,m,n):
        '''
            Returns a number based on relative equality
            Lower the better
            Parameters: The two strings and length of the two strings
            Return: Min-Edit Distance
        '''
        dp = [[0 for x in range(n + 1)] for x in range(m + 1)] 
        for i in range(m + 1): 
            for j in range(n + 1): 
                if i == 0: 
                    dp[i][j] = j    
                elif j == 0: 
                    dp[i][j] = i    
                elif str1[i-1] == str2[j-1]: 
                    dp[i][j] = dp[i-1][j-1] 
                else: 
                    dp[i][j] = 1 + min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1]) 
      
        return dp[m][n] 
    
    def predict2(self):
        '''
            Based on Permutation
            Give Predictions
            Param : None
            Return : None
        '''
        for i in self.sentence:
            t = self.min_edit(i,self.string,len(i),self.ln) 
            if(t not in self.comparision):
                self.comparision[t] = [i]
            else:
                self.comparision[t].append(i)

    def voice(self,text):
        self.tts=gTTS(text=text,lang="en",slow = "True")
        self.tts.save("voice.mp3")
        os.system("voice.mp3")

    def set(self,string):
        self.show.destroy()
        self.all += string
        self.show = Label(self.root,text = self.all)
        self.show.pack(side = BOTTOM)
    def display(self):
        '''
            Printing the predictions
            Param : None
            Return : None
        '''
        self.predict = [i for x in sorted(self.comparision.keys()) for i in self.comparision[x] ] 
        text = "Your predictions for the entered text are "

        while(len(self.predict) < 4):
                self.predict.append("")

        Button(self.root,text = self.predict[0],command = lambda : self.set(self.predict[0])).pack(side = LEFT)
        Button(self.root,text = self.predict[1],command = lambda : self.set(self.predict[1])).pack(side = LEFT)
        Button(self.root,text = self.predict[2],command = lambda : self.set(self.predict[2])).pack(side = LEFT)
        Button(self.root,text = self.predict[3],command = lambda : self.set(self.predict[3])).pack(side = LEFT)
            
        
    def ts(self,li):
        global sentence
        t="".join(li)
        '''d = enchant.Dict("en_US")
        if(d.check(t)):
            sentence.append(t)'''
        #print(t)
    

    def permutate(self,a,l,r):
        '''
            Generates all permutation
            Not used as too time consuming
            O(n+n^2+n^3+...n^n) = O(n^n)
            Param : String, length and required length
            Return : Combinations/checked one based on implementations
        '''
        if(l==r):
            ts(a)
        else:
            for i in range(l,r+1):
                a[l],a[i]=a[i],a[l]
                permutate(a,l+1,r)
                a[l],a[i]=a[i],a[l]


obj = autocorrect()

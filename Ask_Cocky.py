import Tkinter
from Tkinter import *
import speech_recognition as sr
import pyaudio
import random
import pyttsx
 
root = Tkinter.Tk()
root.geometry("1050x550") #this gives us larger window, not larger image... but will be good for adding other stuff
root.configure(bg='black') #change color of background
canvas = Tkinter.Canvas(root)
canvas.grid(row = 0, column = 0)
canvas.config(width=1000, height=500, bg='#990000') #this changes size of canvas (which is where images go)
engine=pyttsx.init()
voices=engine.getProperty('voices')
# Here is the voice ID change spot
engine.setProperty('voice',voices[0].id)
  
 
  
def getImageName():
    map=["U","P","N"]
    return 'Images/'+'answer'+map[mood]+str(number)+'.gif'
      
photo = Tkinter.PhotoImage(file = 'Images/cockyblank.gif')
canvas.create_image(0,0, anchor=NW, image=photo)
  
directions=Tkinter.PhotoImage(file = "Images/directions.gif")
canvas.create_image(0,1,anchor=NE,image=directions)
 
 
round=1
list1=[] 
g=()
YorNquestions=["Do","do","Did","did","does","Does","Am",'am','are','Are','Is','is','Was','was','were','Were','Will','will']
f=()
def listen():
    global labelVariable
    global list1,round,Tkinter,root,photo, photo1,val,number,mood,f,g
    global canvas
    r = sr.Recognizer()
    with sr.Microphone() as source:                # use the default microphone as the audio source
        # r.adjust_for_ambient_noise(source)   ##if you're playing the game in a noisy area, use this line and it will calibrate bkground b4 you speak
        audio = r.listen(source)                   # listen for the first phrase and extract it into audio data
    g=r.recognize_google(audio)
    string=str(g)
    splitted=string.split()
    if splitted[0] in YorNquestions:
        f=g
        def numgen(a,b):
            x=[int(a*random.random()) for i in xrange(b)]
            return x
        val=numgen(3,2) 
        number=val[0]
        mood=val[1]
        # labelVariable.set( "Time for Question %d" % round)
        photo = Tkinter.PhotoImage(file = getImageName())
        canvas.create_image(0,0, anchor=NW, image=photo) 
 
        if val[0]==0 and val[1]==0:
            engine.say("I'm not sure right now, Ask me again later!")
        if val[0]==1 and val[1]==0: 
            engine.say("I need to think about that one... try again soon!")
        if val[0]==2 and val[1]==0:
            engine.say("Too Hard! I'm just the mass cot! Ask me something else.")
        if val[0]==0 and val[1]==2:
            engine.say("It's going to be a no.")
        if val[0]==1 and val[1]==2:
            engine.say("I'm sorry. It's not looking so good.")
        if val[0]==2 and val[1]==2:
            engine.say("No, you're not going to convert on That play.")
        if val[0]==0 and val[1]==1:
            engine.say("oh yes, for sure! U S C Goooo cocks!")
        if val[0]==1 and val[1]==1:
            engine.say("My sources say definitely!! hashtag beakflap.")
        if val[0]==2 and val[1]==1:
            engine.say("You can count on it like Carolina football.")  
        round+=1
        labelVariable.set("You Asked: "+f+"?"+" "*10+"Time for question %d" % round)  
    else:
        labelVariable.set("Try Another Question Please")
        photo=Tkinter.PhotoImage(file='Images/reask.gif')
        canvas.create_image(0,0, anchor=NW, image=photo) 
        engine.say("What? I don't understand... Please ask a yes or no question")
    engine.runAndWait()
    
    # print string
 
button = Tkinter.Button(root,text=u"Ask Cocky",command=listen, anchor='s', background="black", foreground='white', activebackground='#8D0000')
button.configure(width=10)
buttonwindow=canvas.create_window(670,400,anchor="sw",window=button)
  
labelVariable = Tkinter.StringVar()
label = Tkinter.Label(root,textvariable=labelVariable,anchor="w",fg="black",bg="white")
label.grid(column=0,row=6,columnspan=2,sticky='EW')
labelVariable.set(u"Ask away!")
 
#placing the directions file on the canvas
photo1=Tkinter.PhotoImage(file = 'Images/directions.gif')
canvas.create_image(820, 185, image=photo1)
  
# maybe able to get it running w/o continuing to click
  
  
root.mainloop()
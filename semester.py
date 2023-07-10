from tkinter import filedialog
from tkinter import messagebox
from PoseModule import PoseDetector
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import mediapipe as mp
import pyttsx3
import webbrowser
import time
import threading


#### GLOBAL VARIABLES ###
global cap, Analysis
global var1, frame_1
global win, label1, v, q, Next
global canvas,link1,link2,link3,link4
adit = 0
SajCount = 0
link1="https://github.com/Muhammad-Anees99/Salah-Analysis-using-Mediapipe-and-OpenCV-with-Creative-and-User-Friendly-GUI.git "
link2="https://medium.com/@m.anees990011/salah-analysis-using-mediapipe-and-opencv-along-with-gui-in-python-beeb8d91a87a"
link3="https://github.com/Muhammad-Anees99/Salah-Analysis-using-Mediapipe-and-OpenCV-with-Creative-and-User-Friendly-GUI.git "
link4="https://medium.com/@m.anees990011/salah-analysis-using-mediapipe-and-opencv-along-with-gui-in-python-beeb8d91a87a"
check = False
Draw = False
Analysis = False
Update = False
CheckAgain = True
engine=pyttsx3.init() 

Prayer = {'Takbir': False, 'Qayam': False, 'Ruku':False, 'Qomah': False, 'Sajdah': False, 'Atahyaat': False}
cap = cv2.VideoCapture(0)
detector = PoseDetector()

mpPose=mp.solutions.pose # From different
mpDraw=mp.solutions.drawing_utils


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
# engine.say("Loading Started, Please Hold on for few seconds!")
engine.runAndWait()
#opens links
def o_link(linky):
    webbrowser.open(linky)
#Current pose speak
def read_out():
    true_vars = [key for key, value in Prayer.items() if value]
    if len(true_vars) == 1:
        engine.say(true_vars[0])
        engine.runAndWait()
        

# Function to update the variables in the dictionary and call read_out if necessary
def update_variables():
    while True:
        time.sleep(3)
        read_out()

### FUNCTION FOR START LIVE BUTTON ###
def Starting():
    global Analysis, Update, wid, heit, label1
    win.after(1000, lambda: engine.say("Starting Live"))
    win.after(1000, engine.runAndWait)
    wid = 550
    heit = 400
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    # print(lmlist)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    label1=Label(frame_1,width = wid, height = heit)
    label1.place(x=420, y=180)
    Analysis = True
    Update = True

### FUNCTION FOR START RECORDED BUTTON ###
def RecordedVideo():

    global win, label1, cap, wid, heit, Analysis, Update, check
    cap.release()
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    # print(lmlist)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    win.after(1000, lambda: engine.say("Select a RecordedVideo"))
    win.after(1000, engine.runAndWait)
    win.filename = filedialog.askopenfilename(initialdir = "Users\manee\OneDrive\Desktop",  \
    title = "Select Any Recorded Video")
    label1.destroy()
    label1 = Label(frame_1, width = 500, height= 400)
    if win.filename:
        cap = cv2.VideoCapture(win.filename)
        label1.place(x=450, y=180)
        threading.Thread(target=update_variables).start()
        Analysis = True
        Update = True
        wid = 500
        heit = 400
    else:
        cap = cv2.VideoCapture(0)
        Analysis = False
        check = False
        Update = False
        label1.configure(width = 210, height= 100)
        label1.place(x=860, y=300)
        wid = 140
        heit = 80
    LiveVideo()
    select_img()


### FUNCTION FOR EXIT TO MAIN MENU BUTTON
def MMenu():
    global Analysis, DetectionLabel, label1, wid, heit, cap, MainMenu, check, img, rgb, DetectMssg
    global image, Update, DrawScl, NextMssg, Draw 
    
    cap.release()

    DetectionLabel.destroy()
    label1.destroy()
    DrawScl.destroy()
    MainMenu.destroy()
    DetectMssg.destroy()
    NextMssg.destroy()
    welc1.destroy()
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    win.after(1000, lambda: engine.say("Exiting"))
    win.after(1000, engine.runAndWait)
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    Draw = False
    Analysis = False
    check = False
    Update = False
    label1 = Label(frame_1, width = 2, height= 1, bg= "#2C2F33")
    label1.place(x=0, y=0)
    wid = 140
    heit = 80
    cap = cv2.VideoCapture(0)
    LiveVideo()
    welcome()

# Exit from About Us
def MMenu2():
    global Analysis, DetectionLabel, label1, wid, heit, cap, MainMenu, check, img, rgb, DetectMssg
    global image, Update, DrawScl, NextMssg, Draw 
    
    cap.release()

    label1.destroy()
    MainMenu2.destroy()
    welc4.destroy()
    welc5.destroy()
    welc6.destroy()
    An_Git.destroy()
    An_Med.destroy()
    Mua_Git.destroy()
    Mua_Med.destroy()
    welc1.destroy()
    welc2.destroy()
    win.after(1000, lambda: engine.say("Exiting"))
    win.after(1000, engine.runAndWait)
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    Draw = False
    Analysis = False
    check = False
    Update = False
    label1 = Label(frame_1, width = 2, height= 1, bg= "#2C2F33")
    label1.place(x=0, y=0)
    wid = 140
    heit = 80
    cap = cv2.VideoCapture(0)
    LiveVideo()
    welcome()
    
def MMenu3():
    global Analysis, DetectionLabel, label1, wid, heit, cap, MainMenu, check, img, rgb, DetectMssg
    global image, Update, DrawScl, NextMssg, Draw 
    
    cap.release()

    label1.destroy()
    MainMenu3.destroy()
    Tak.destroy()
    Qay.destroy()
    Ruk.destroy()
    Qom.destroy()
    Saj.destroy()
    Atah.destroy()
    win.after(1000, lambda: engine.say("Exiting"))
    win.after(1000, engine.runAndWait)
    canvas = Canvas(win, width=win.winfo_screenwidth(), height=win.winfo_screenheight())
    canvas.pack()
    canvas.create_image(0, 0, image=bg_image, anchor=NW)
    Draw = False
    Analysis = False
    check = False
    Update = False
    label1 = Label(frame_1, width = 2, height= 1, bg= "#2C2F33")
    label1.place(x=0, y=0)
    wid = 140
    heit = 80
    cap = cv2.VideoCapture(0)
    LiveVideo()
    welcome()
### fUNCTION FOR DRAW SCALE BUTTON ###
def callback1(value):
    global Draw
    if Draw:
        Draw = False
    else:
        Draw = True

### FUNCTION FOR STARTING VIDEO PROCESING ###
def LiveVideo():
    global cap, img, _, wid, heit, rgb, image, finalImage
    _, img = cap.read()
    img = cv2.resize(img, (wid, heit))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb =cv2.flip(rgb, 1)
    image = Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage

### MAIN ANALYSYS FUNCTION ###
def select_img():
    global img, finalImage, image, rgb, _, wid, heit, lmlist, check, Update, label1
    global cap, v, q, pos, Next, CheckAgain, SajCount

    _, img = cap.read()
    img = cv2.resize(img, (wid, heit))
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    rgb =cv2.flip(rgb, 1)

    # img = detector.findPose(img)
    # lmlist2, bbxInf = detector.findPosition(img, bboxWithHands=True)
    lmlist = []

    if Update:
        AnalysisWinUpdate()
        Update = False
    
    if Analysis:
        detector.results = detector.pose.process(rgb)
        if detector.results.pose_landmarks:
            check = True
            for id, lm in enumerate(detector.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy, cz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                lmlist.append([id, cx, cy, cz])
                # if Draw:
                #     detector.mpDraw.draw_landmarks(rgb, detector.results.pose_landmarks, detector.mpPose.POSE_CONNECTIONS)
            lmlist=detector.nvc(lmlist)

            if Draw:
                detector.mpDraw.draw_landmarks(rgb, detector.results.pose_landmarks, detector.mpPose.POSE_CONNECTIONS)
                cv2.circle(rgb, (int(lmlist[33][1]) , int(lmlist[33][2])), radius=3, color=(255, 0, 0), thickness=2)
                
        else:
            check = False
    
    if check:
        Nose_Y=lmlist[0][2]
        earRight_X=lmlist[8][1]
        earRight_y=lmlist[8][2]
        
        earLeft_X=lmlist[7][1]
        earLeft_y=lmlist[7][2]
        
        IndexRight_X=lmlist[22][1]
        IndexRight_Y=lmlist[22][2]

        IndexLeft_X=lmlist[21][1] #changing made using thummbs insted of index fingers
        IndexLeft_Y=lmlist[21][2]
        
        ThumbRight_X=lmlist[22][1]
        ThumbRight_Y=lmlist[22][2]

        ThumbLeft_X=lmlist[21][1] 
        ThumbLeft_Y=lmlist[21][2]

        KneeRight_X=lmlist[26][1] 
        KneeRight_Y=lmlist[26][2]

        KneeLeft_X=lmlist[25][1]  
        KneeLeft_Y=lmlist[25][2] 

        HipRight_Y=lmlist[24][2]  
        HipLeft_Y=lmlist[23][2]

        ShoulderRight_Y=lmlist[12][2]  
        ShoulderLeft_Y=lmlist[11][2]

        AnkleRight_X=lmlist[28][1] 
        AnkleRight_Y=lmlist[28][2]

        AnkleLeft_X=lmlist[27][1]   
        AnkleLeft_Y=lmlist[27][2]

        ToeRight_X =lmlist[32][1]   
        ToeLeft_X = lmlist[31][1]

        ToeRight_Y =lmlist[32][2]   
        ToeLeft_Y = lmlist[31][2]

        LeftKneeAngle = int(detector.Angle(lmlist,23, 25, 27))#variable name changed
        RightKneeAngle=int(detector.Angle(lmlist,24,26,28))#use of right knee angle
        ElbowAngle = int(detector.Angle(lmlist,11, 13, 15))
        print(ElbowAngle,LeftKneeAngle)

        adit = abs(ShoulderRight_Y - HipRight_Y)
        adit = adit/2

        if (IndexRight_Y<ShoulderRight_Y and IndexLeft_Y<ShoulderLeft_Y):
            # and (IndexRight_Y>earRight_y and IndexLeft_Y>earLeft_y) and (abs(IndexRight_Y-IndexLeft_Y)<10) and \
            # (abs(IndexRight_X-IndexLeft_X)<120) and ((abs(earRight_X-earLeft_X)+10)<(abs(ThumbRight_X-ThumbLeft_X))):#changing made in condition and taking difference of thumbs 
            Prayer['Takbir'] = True
        else:
            Prayer['Takbir'] = False

        if (LeftKneeAngle > 169 and LeftKneeAngle < 175) and \
            (ElbowAngle > 20 and ElbowAngle < 50) and (abs(ThumbLeft_Y-ThumbRight_Y)<15) :#changing made in elbow angle and use of thumb
            Prayer['Qayam'] = True
        else:
            Prayer['Qayam'] = False

        if (IndexRight_Y > (HipRight_Y + (KneeRight_Y-HipRight_Y)/2) and \
            (IndexLeft_Y > (HipLeft_Y + (KneeLeft_Y-HipLeft_Y)/2))) and ((LeftKneeAngle) > 160) and \
             (ElbowAngle > 135) :
            Prayer['Ruku'] = True
        else:
            Prayer['Ruku'] = False

        if (IndexRight_Y > HipRight_Y) and (IndexLeft_Y > HipRight_Y) and ((LeftKneeAngle) > 165) and \
            ((RightKneeAngle) > 165) and (abs(ThumbRight_Y-ThumbLeft_Y) < 10) :#why hip right in both and changing made for thumbs position use of elbow angle
            Prayer['Qomah'] = True
        else:
            Prayer['Qomah'] = False

        if (ToeLeft_X < AnkleLeft_X) or (ToeRight_X < AnkleRight_X):
            if  ((Nose_Y > ShoulderRight_Y) or (Nose_Y > ShoulderLeft_Y)) and \
            ((HipRight_Y < ShoulderRight_Y) or (HipLeft_Y < ShoulderLeft_Y)) and \
            (((IndexRight_X > KneeRight_X) or (IndexLeft_X > KneeLeft_X)) or ((IndexRight_X < KneeRight_X) or (IndexLeft_X < KneeLeft_X))) and \
            (LeftKneeAngle  < 70 and LeftKneeAngle  > 50) and (ElbowAngle > 50 and ElbowAngle < 70) and \
            ((ToeLeft_Y or ToeRight_Y) - (KneeLeft_Y or KneeRight_Y) < 10) :
            # (Nose_Y - (IndexLeft_Y or IndexRight_Y) < 10)
                Prayer['Sajdah'] = True
            else:
                Prayer['Sajdah'] = False

        if (((HipRight_Y > (AnkleRight_Y - adit)) or (HipLeft_Y > (AnkleLeft_Y - adit))) \
            and (LeftKneeAngle < 20 and LeftKneeAngle > 12) and (ElbowAngle>145 and ElbowAngle<155) ):# use of elbow angle
            Prayer['Atahyaat'] = True
        else:
            Prayer['Atahyaat'] = False

        if Prayer['Takbir']:
            v.set("Takbir")
        elif Prayer['Sajdah']:
            v.set("Sajdah")
        elif Prayer['Ruku']:
            v.set("Ruku")
        elif Prayer['Atahyaat']:
            v.set("Atahyaat")
        elif Prayer['Qomah']:
            v.set("Qomah")
        elif Prayer['Qayam']:
            v.set("Qayam")
        else:
            v.set("None")

        if Prayer["Sajdah"] and CheckAgain:
            SajCount += 1
            CheckAgain = False
        if (not Prayer["Sajdah"]) and Prayer["Atahyaat"]:
            CheckAgain = True


        pos = v.get()
        pos = "Your current position is " + pos
        q.set(pos)

        pos = "The next position should be "
        if v.get() == 'Takbir':
            nex = "Qayam"
        elif v.get() == 'Qayam':
            nex = "Ruku"
        elif v.get() == 'Ruku':
            nex = "Qomah"
        elif v.get() == 'Qomah':
            nex = "Sajdah"
        elif v.get() == 'Sajdah':
            nex = "Atahyaat"
        elif v.get() == 'Atahyaat' and SajCount == 1:
            nex = "Sajdah"
        elif v.get() == 'Atahyaat' and SajCount>1:
            nex = "Salam"
        else:
            pos = ""
            nex = ""
        pos = pos + nex
        Next.set(pos)
        

    
    image = Image.fromarray(rgb)
    finalImage = ImageTk.PhotoImage(image)
    label1.configure(image=finalImage)
    label1.image = finalImage
    win.after(1, select_img)
    

def Takb():
    messagebox.showinfo('Takbir',f'Raise both of your hands next to each ears. Touch the lobes of your each ear with thumbs')

def Qaya():
    messagebox.showinfo('Qayam',f'Place the hands on navel right hand on top of left hand. Thumb and Pinky (smallest finger) should be wraped around the wrist of left hands wrist. It should be like you are locking or grabbing the left hand wrist. Rest of the three fingers of right hand should be strait in line to each other.')

def RUk():
    messagebox.showinfo('Ruku',f'When one bows, Your hands must reach Ypur knees. It is Sunnah to make\
the height of the head equal to that of the hips. The hands should be supported by the knees and should \
be apart from your sides. The hands should be open upon your knees and thighs, and the palms should be flat.')

def QOm():
    messagebox.showinfo('Qomah',f'It is also a wajib act of Namaz to stand straight after Ruku for a while before going to Sujood.',)

def Sajd():
    messagebox.showinfo('Sajdah',f'In sajdah all the fingers of feet should be twisted so that the round soft part of the fingers is touching the ground. Hand fingers should be close to face and facing Kabah in strait line. Put enough pressure on nose so that the bone of nose should feel the hardness of earth (do not hurt your self but should be firm) Arms should be away from body like a bird opens the wings.')

def Atahy():
    messagebox.showinfo('Atahyat',f'Rest the palms of your hands on your knees. Sit on the flat of your left foot, whilst keeping the toes of the right foot planted and pointing forward. Women should lean on their left hip pointing the toes of both feet to the right side. ')

def AdditonalLM():
    messagebox.showinfo('About Additional Landmark',f'We have generated an Additional Landmark at Navel By using Left Shoulder x and y points, Right Shoulder x and y points, Left Hip x and y points, Right Hip x and y points.')

def welcom_destroy():
    StartLive.destroy()
    StartRecord.destroy()
    About.destroy()
    Exit.destroy()
    Salah.destroy()
    Additonal.destroy()
    
def Salah_Info():
    global Tak,Qay,Ruk,Qom,Saj,Atah,MainMenu3
    inner_frame = Frame(win)
    inner_frame.place(x=500,y=550)
    welcom_destroy()
    Tak= Button(win,text="Takbir",borderwidth=12,font=("Times",14), command= Takb,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Tak.place(x = 335, y = 360)
    Qay= Button(win,text="Qayam",borderwidth=12,font=("Times",14), command=Qaya,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Qay.place(x = 865, y = 360)
    
    Ruk= Button(win,text="Ruku",borderwidth=12,font=("Times",14), command= RUk,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Ruk.place(x = 335, y = 445)
    Saj= Button(win,text="Sajdah",borderwidth=12,font=("Times",14), command=Sajd,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Saj.place(x = 335, y = 530)
    Qom = Button(win,text="Qomah",borderwidth=12,font=("Times",14), command=QOm,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Qom.place(x = 865, y = 445)
    Atah = Button(win,text="Atahyat",borderwidth=12,font=("Times",14), command=Atahy,width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Atah.place(x = 865, y = 530)
    MainMenu3 = Button(win,text='Exit to Main Menu',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    command= MMenu3, relief = RAISED)
    MainMenu3.place(x = 605, y = 615)
    
def About_Us():
    global welc2,welc4,welc4,welc5,welc6,An_Git,An_Med,Mua_Git,Mua_Med,MainMenu2
    inner_frame = Frame(win)
    inner_frame.place(x=500,y=550)
    welcom_destroy()
    An_Git = Button(win,text="GitHub",borderwidth=12,font=("Times",14), command= lambda:o_link(link1),width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    An_Git.place(x = 335, y = 465)
    An_Med= Button(win,text="Medium",borderwidth=12,font=("Times",14), command=lambda:o_link(link2),width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    An_Med.place(x = 335, y = 550)
    Mua_Git = Button(win,text="GitHub",borderwidth=12,font=("Times",14), command=lambda:o_link(link3),width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Mua_Git.place(x = 865, y = 465)
    Mua_Med = Button(win,text="Medium",borderwidth=12,font=("Times",14), command=lambda:o_link(link4),width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    relief = RAISED)
    Mua_Med.place(x = 865, y = 550)
    welc4 = Message(win,borderwidth=6, justify = CENTER, text= "Developed By :", \
    font = ("Times", 18), fg = "white",bg = "black", relief = RAISED, width = 1280)
    welc4.place(x = 600, y = 330)
    # engine.say("This Project is Developed by Muhammad Anees (2021-MC-03) and Muawwiz Ali Yousaf (2021-MC-13) in Department of Mechatronics & Control Engineering, University of Engineering and Technology, Lahore")
    # win.after(1500, lambda: engine.say("For More information Click Any Button"))
    # win.after(1500, engine.runAndWait)
    welc5= Message(win, justify = CENTER,borderwidth=6, text= "Muhammad Anees (2021-MC-03)", \
    font = ("Times", 18), fg = "white",bg = "black", relief = RAISED, width = 1280)
    welc5.place(x = 245, y = 395)
    welc6= Message(win, justify = CENTER,borderwidth=6, text= "Muawwiz Ali Yousaf (2021-MC-13)", \
    font = ("Times", 18), fg = "white",bg = "black", relief = RAISED, width = 1280)
    welc6.place(x = 785, y = 395)
    welc2 = Message(win, justify = CENTER,borderwidth=6, font = ("Times", 19), fg = "white", \
    bg = "black",text= "Department of Mechatronics & Control Engineering, University of Engineering and Technology, Lahore",\
    width = 1200,relief = RAISED)
    welc2.place(x = 168, y = 660)
    MainMenu2 = Button(win,text='Exit to Main Menu',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    command= MMenu2, relief = RAISED)
    MainMenu2.place(x = 595, y = 575)
    
    
def welcome():
    global StartLive, welc1, welc2, welc4, label1, wid, heit, WelcMsg, Exit, win, StartRecord,About,Salah,Additonal
    WelcMsg = StringVar()
    WelcMsg.set("WELCOME TO THE PRAYER ANALYSIS MEDIAPIPE PROJECT")
    welc1 = Message(win,borderwidth=6, justify = CENTER, textvariable = WelcMsg, font = ("Times", 20), \
    fg = "white",bg = "black", relief = RAISED, width = 1000)
    welc1.place(x = 270, y = 120)
    About = Button(win, text="About us",borderwidth=12,font = ("Times", 14),width = 16, fg = "white",bg = "black", padx=10,pady=10, \
    command=About_Us,relief = RAISED)
    About.place(x=735,y=560)
    Additonal = Button(win, text="Additional",borderwidth=12,font = ("Times", 14),width = 16, fg = "white",bg = "black", padx=10,pady=10, \
    command=AdditonalLM,relief = RAISED)
    Additonal.place(x=490,y=560)
    StartLive=Button(win,text='Start Live Video',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    command= Starting, relief = RAISED)
    StartLive.place(x = 490, y = 475)
    StartRecord =Button(win,text='Start Recorded Video',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black",padx=10,pady=10, relief = RAISED, \
    command = RecordedVideo)
    StartRecord.place(x = 735, y = 475)
    Salah = Button(win,text='Salah Poses',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    command= Salah_Info, relief = RAISED)
    Salah.place(x = 490, y = 645)
    Exit = Button(win,text='Exit Program',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10,\
    command= ExitTheProgram, relief = RAISED)
    Exit.place(x = 735, y = 645)
    
    
def ExitTheProgram():
    engine.say("Exiting")
    engine.runAndWait()
    win.destroy()
    
def AnalysisWinUpdate():
    global v, q, pos, wid, heit, label1, StartLive, welc1, welc2, welc4
    global DetectionLabel, MainMenu, DrawScl, WelcMsg, DetectMssg, NextMssg, Next,NextVoice
    welc1.destroy()
    welcom_destroy()
    canvas.destroy()

    # welc1.destroy()
    DetectionLabel=Label(win,width=30,borderwidth=6, height = 1, font = ("Times", 21), \
    bg = "black", fg= "white", textvariable= v, relief=RAISED)
    DetectionLabel.place(x = 465, y = 115)

    if (wid == 236 and heit == 400):
        DetectionLabel.place(x = 634, y = 104)
        DetectionLabel.configure(width = 15)

    MainMenu=Button(win,text='Exit to Main Menu',borderwidth=12,font = ("Times", 14), width = 16, fg = "white",bg = "black", padx=10,pady=10, relief = RAISED, command = MMenu)
    MainMenu.place(x = 420, y = 620)

    DrawScl = Scale(win, label="Enable Draw Landmarks",highlightthickness=6,highlightbackground="#2C2F33", from_ =0, to=1, orient=HORIZONTAL,width=8, command = callback1,\
    bg = "black", length= 200, font = ("Times", 14), fg = "white",\
    borderwidth=4, relief= RAISED)
    DrawScl.set(0)
    DrawScl.place(x=765, y=620)
    
    DetectMssg = Message(win,borderwidth=6, justify = CENTER, font = ("Times", 18), bg = "black", fg = "white", \
    textvariable= q, width = 200,relief = RAISED)
    DetectMssg.place(x = 200, y = 330)

    NextMssg = Message(win,borderwidth=6, justify = CENTER, font = ("Times", 18), bg = "black", fg = "white", \
    textvariable= Next, width = 200,relief = RAISED)
    NextMssg.place(x = 200, y = 450)
   

#Main Program
win = Tk()
win.after(1000, lambda: engine.say("WELCOME TO THE SALAH ANALYSIS "))
win.after(1000, engine.runAndWait)
wid = win.winfo_screenwidth()
heit = win.winfo_screenheight()
win.geometry("%dx%d" % (wid, heit))
win.title('Salah Analysis using Mediapipe')
frame_1 = Frame(win, width=0, height=0, bg= "#FFFF00").place(x=0, y=0)
label1 = Label(frame_1, width = 600, height= 400)
label1.place(x=700, y=160)
bg_image = PhotoImage(file="bg20.png")
canvas = Canvas(win, width=wid, height=heit)
canvas.pack()
canvas.create_image(0, 0, image=bg_image, anchor=NW)
wid = 110
heit = 60
v = StringVar()
q = StringVar()
Next = StringVar()
if not Analysis:
    
    welcome()

select_img()
win.mainloop()

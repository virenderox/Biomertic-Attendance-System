import face_recognition as fc
import pandas as pd
import pyttsx3
from PIL import Image, ImageDraw
import cv2
import ast
import list_
import time
from datetime import datetime, timedelta, date
import schedule
import attendence_file

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1])
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def camera_on():
    v = cv2.VideoCapture(0)
    data = pd.read_csv("My_faces.csv")
    dn = (data["Name"].values)
    q = list(set(dn))
    de = data.drop("Name" , axis = 1)
    de = de.to_numpy()
    dic = {}
    for i in q:
        dic[i] = []
    for i in range(len(dn)):
        dic[dn[i]].append(list_.change_to_list(de[i][0]))
    while True:
        r,live = v.read()
        i  = cv2.resize(live,(200,200))
        fll = fc.face_locations(i)
        if len(fll)>0:
            E = fc.face_encodings(i,fll)
            for k in range(len(fll)):
                [x1,y1,x2,y2] = fll[k]
                cv2.rectangle(i,(y2,x1),(y1,x2),(0,0,255),2)
            for k in range(len(fll)):
                dic_e = {}
                for f in q:
                    dic_e[f] = fc.compare_faces(dic[f],E[k])
                dic_t = {}
                for g in dic_e:
                    dic_t[g] = dic_e[g].count(True)
                m = max(dic_t.values())
                
                for h in dic_t:
                    if dic_t[h] == m :
                        if h not in lis:
                            print("Hello",h)
                            lis.append(h)
                            Attendence_name(h,1)
                            speak("Enter q after your face is recognised for further completion of your Attendence.")
                        else:
                            speak("Attendence is already done...")
                            print("Attendence is already done...")
                    else:
                        pass        
            live = cv2.resize(i,(live.shape[1],live.shape[0]))
            cv2.imshow('img',live)
            k = cv2.waitKey(10000)
            if k == ord('q'):
                cv2.destroyAllWindows()
                return(h,q)

def Attendence_name(name,A):
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    d = d1[:2]
    m = d1[3:5]
    if m[0] == '0':
        m = m[1:]
    for i in range(1,13):
        if str(i) == m:
            data = pd.read_csv(' My_attendence' + m + '.csv')
            a = list(data[data['Name'] == name].index)
            if A == 1:
                data.iloc[a[0], data.columns.get_loc('Day' + d)] = 'P'
            elif A == 0:
                data.iloc[a[0], data.columns.get_loc('Day' + d)] = 'A'
            data.to_csv(r'C:\Users\Virender Pal Singh\AppData\Local\Programs\Python\Python36\ My_attendence' + m +'.csv',index = None , header = True)


def start():
    end_time = datetime.now() + timedelta(seconds=8)
    while datetime.now() < end_time:
        speak("Welcome to the Attendence System")
        speak("Please read the instruction carefully.")
        print("\n              Welcome to the Attendence System.")
        print(" 1.) Please enter 'c' to start the camera.")
        print(" 2.) please dont move until camera recognize yourself or it close.")
        print(" 3.) please dont use moblie to recognize yourself , if you doing so action must be take against yourself.")
        print(" 4.) please come in front of camera at a time for your Attendence , if mutilple face is detected no attendence is there against you.")
        print(" 5.) Thank you for your paciances")
        print(" 6.) Please Enter q after your face is recognised for further completion of your Attendence.")
        print(" 7.) The attendence  is taken in between 9:00 am to 9:30 am , after that no attendence is taken.")

        ic = input("\nEnter 'c' to start the camera : ")
        if ic == 'c':
            h,q = camera_on()
            if h not in lis:
                speak("Your Attendence is done....")
                print("Your Attendence is done....")
            else:
                speak("Attendence is already done...")
                print("Attendence is already done...")
        else:
            speak("please read the instrustion carefully")
            print("Invalid Key")
    for i in q:
        if i not in lis:
            Attendence_name(i,0)
            
lis = []
start()





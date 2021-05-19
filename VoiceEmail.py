import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import random
import getpass
import smtplib
import imaplib
import email
from email.message import EmailMessage
from bs4 import BeautifulSoup




engine = pyttsx3.init()
engine.setProperty('rate',130)




pyttsx3.speak("To use function of this program enter valid ID and  password")
print("\n\n-----------------------To use function of this program enter  ID password--------------")


print("\n\n-------------------------------------------------------------------------------------------")
r = sr.Recognizer()

with sr.Microphone() as source:
    
    pyttsx3.speak("speak your voice ID")
    print("\nSpeak your voice ID:")

    iD_audio = r.listen(source)
    pyttsx3.speak("we got your voice ID")
    print("\nwe got your voice ID")


print("\n\n--------------------------------------------------------------------------------------------")
ID = r.recognize_google(iD_audio)
pyttsx3.speak("you said {}".format(ID))
print("\n you said",ID)


pyttsx3.speak("Enter valid voice password")
print("\n\n----------------------- Enter  voice password--------------")

print("\n\n-------------------------------------------------------------------------------------------")
r = sr.Recognizer()

with sr.Microphone() as source:
    
    pyttsx3.speak("speak your voice password")
    print("\nSpeak your voice password:")

    pass_audio = r.listen(source)
    pyttsx3.speak("we got your voice password")
    print("\nwe got your voice password")


print("\n\n--------------------------------------------------------------------------------------------")
q = r.recognize_google(pass_audio)
pyttsx3.speak("you said {}".format(q))
print("\n you said",q)



pass1 = "admin"
if pass1 != q:
    pyttsx3.speak("Password is invalid you can't use this system")
    print("Password is invalid you can't use this system")
    exit()

else:    
    pyttsx3.speak("Welcome you in  voice email system")
    print("*Welcome you in  voice email system **")


def get_info():
      try:
          with sr.Microphone() as source:
              print("Listening..")
              voice = listener.listen(source)
              info = listener.recognize_google(voice)
              print(info)
              return info.lower()
            
      except:
          pass

def send_email(receiver, subject, message):
      server = smtplib.SMTP('smtp.gmail.com', 587)
      server.starttls()
      server.login('blackpoonam1010@gmail.com', 'Pooonam08@')
      email = EmailMessage()
      email['From'] = 'blackpoonam1010@gmail.com'
      email['To'] = receiver
      email['Subject'] = subject
      email.set_content(message)
      server.send_message(email)

email_list = {
      'poonam' : 'blackpoonam1010@gmail.com',
      'deepak' : 'janvibankar200797@gmail.com'
      }

def get_email_info():
      talk('To whom do you want to send email')
      name = get_info()
      receiver = email_list[name]
      print(receiver)
      talk('What is the subject of your email')
      subject = get_info()
      talk('Tell me the body of your email')
      message = get_info()
      send_email(receiver, subject, message)
    
def read_mail():
    server = imaplib.IMAP4_SSL('imap.gmail.com',993)
    server.login('blackpoonam1010@gmail.com', 'Pooonam08@')
    stat, total = server.select('Inbox')
    print ("Number of mails in your inbox :"+str(total))
    talk('Total mails are: '+str(total))
    
    unseen = server.search(None,'Unseen')
    print ("Number of UnSeen mails :"+str(unseen))
    talk('Unseen mails are: '+str(unseen))
    
    result, data = server.uid('search',None, "ALL")
    inbox_item_list = data[0].split()
    new = inbox_item_list[-1]
    old = inbox_item_list[0]
    result2, email_data = server.uid('fetch', new, '(RFC822)') #fetch
    raw_email = email_data[0][1].decode("utf-8") #decode
    email_message = email.message_from_string(raw_email)
    print ("From: "+email_message['From'])
    talk('Mail is from: '+email_message['From'])
    print ("Subject: "+str(email_message['Subject']))
    talk('Subject of the mail is : '+email_message['Subject'])
    
    stat, total1 = server.select('Inbox')
    stat, data1 = server.fetch(total1[0], "(UID BODY[TEXT])")
    msg = data1[0][1]
    soup = BeautifulSoup(msg, "html.parser")
    txt = soup.get_text()
    print ("Body :"+txt)
    talk('Body of the mail is: '+txt)

r = sr.Recognizer()

with sr.Microphone() as source:
    
    pyttsx3.speak("Choose your option")
    print("\nChoose your option:")
    pyttsx3.speak("Speak one to compose mail")
    print("\n:Speak one to compose mail")
    pyttsx3.speak("Speak two to read inbox")
    print("\n:Speak two to read inbox")
    choice = r.listen(source)
    pyttsx3.speak("we got your choice")
    print("\nwe got your choice")
    print("\n\n--------------------------------------------------------------------------------------------")
    choice = r.recognize_google(choice)
    pyttsx3.speak("you said {}".format(choice))
    print("\n you said",choice)

if(("one" in choice) or ("One" in choice) or ("1" in choice)):
        
  listener = sr.Recognizer()
  engine = pyttsx3.init()

  def talk(text):
      engine.say(text)
      engine.runAndWait()
  get_email_info()
      
elif(("two" in choice) or ("Two" in choice) or ("2" in choice) or ("tu" in choice) or ("to" in choice)):
   listener = sr.Recognizer()
   engine = pyttsx3.init()

   def talk(text):
      engine.say(text)
      engine.runAndWait()
      
   read_mail()
import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import random
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import smtplib
import imaplib
import email
from email.message import EmailMessage
from bs4 import BeautifulSoup


engine=pyttsx3.init()
engine.setProperty('rate',130)

app=Flask("dbproject")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb/data.sqlite'

db=SQLAlchemy(app)



class myclass(db.Model):
	nickname = db.Column(db.Text, unique = True)
	userid = db.Column(db.Text, primary_key = True)
	password = db.Column(db.Text)

	def __init__(self,nickname,userid,password):
		self.nickname=nickname
		self.userid = userid
		self.password = password
	
db.create_all()

global struid
global lpass


r = sr.Recognizer()

with sr.Microphone() as source:
	pyttsx3.speak("Are you new user of system ")
	print("\nAre you new user of system?")
	uchoice = r.listen(source)
	pyttsx3.speak("we got your voice")
	print("\nwe got your voice ")


print("\n\n--------------------------------------------------------------------------------------------")


Userchoice = r.recognize_google(uchoice)
pyttsx3.speak("you said {}".format(Userchoice))
print("\n you said",Userchoice)

if ( (Userchoice=="yes") or (Userchoice=="Yes") ):
	pyttsx3.speak("To register in voice based email system speak your Nickname username and password ")
	print("\n\n-----------------------To register in voice based email system speak your Nickname username and password--------------")

	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("speak your Nickname")
			print("\nSpeak your voice Nickname:")

			nickaudio_audio = r.listen(source)
			pyttsx3.speak("we got your Nickname")
			print("\nwe got your voice Nickname")


	print("\n\n--------------------------------------------------------------------------------------------")

	global Nickname

	Nickname = r.recognize_google(nickaudio_audio)
	pyttsx3.speak("you said {}".format(Nickname))
	print("\n you said",Nickname)
	
	




	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("speak your voice ID")
			print("\nSpeak your voice ID:")

			iD_audio = r.listen(source)
			pyttsx3.speak("we got your voice ID")
			print("\nwe got your voice ID")


	print("\n\n--------------------------------------------------------------------------------------------")

	global ID

	ID = r.recognize_google(iD_audio)
	pyttsx3.speak("you said {}".format(ID))
	print("\n you said",ID)
	id=ID.replace(" ", "")
	UID=id.lower()


	print("\n\n-------------------------------------------------------------------------------------------")
	r=sr.Recognizer()

	with sr.Microphone() as source:
    
		pyttsx3.speak("speak your voice password")
		print("\nSpeak your voice password:")
		pass_audio=r.listen(source)
		pyttsx3.speak("we got your voice password")
		print("\nwe got your voice password")


	print("\n\n--------------------------------------------------------------------------------------------")

	global Passaudio

	Passaudio=r.recognize_google(pass_audio)
	pyttsx3.speak("you said {}".format(Passaudio))
	print("\n you said",Passaudio)

	passaudio=Passaudio.replace(" ", "")
	
	nickname=Nickname
	userid=UID
	userpass=passaudio
	
	uname=myclass.query.filter_by(nickname=Nickname).first()
	if uname:
		print("User is already exist in system choose different username and password to register in system")
		pyttsx3.speak("User is already exist in system choose different username and password to register in system")
	else:
		userinfo=myclass(nickname,userid,userpass)
		db.session.add(userinfo)
		db.session.commit()
		pyttsx3.speak("user successfully added in database")
		print("user successfully added in database")

		
	pyttsx3.speak("Speak your Login credential to login into Voice based email system")
	print("\nSpeak your Login credential to login into Voice based email system:")
	

	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("Speak your Nickname")
			print("\nSpeak your login Nickname:")

			l_nickname= r.listen(source)
			pyttsx3.speak("we got your Nickname")
			print("\nwe got your voice Nickname")
			

	print("\n\n--------------------------------------------------------------------------------------------")

	Lognickname=r.recognize_google(l_nickname)
	pyttsx3.speak("you said {}".format(Lognickname))
	print("\n you said",Lognickname)


	
	lname=myclass.query.filter_by(nickname=Lognickname).first()
	u_id=lname.userid
	

	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("Speak your Password")
			print("\nSpeak your login Password:")

			l_password= r.listen(source)
			pyttsx3.speak("we got your Password")
			print("\nwe got your voice Password")
			

	print("\n\n--------------------------------------------------------------------------------------------")

	Log_password=r.recognize_google(l_password)
	Logpassword=Log_password.replace(" ","")
	pyttsx3.speak("you said {}".format(Logpassword))
	print("\n you said",Logpassword)
	
	l_pass=lname.password

	lpass=str(l_pass)
	uid=str(u_id)
	
		
	if l_pass==Logpassword:
		print("You have enter correct password")
		pyttsx3.speak("You have enter correct password")


		if (lname and lpass):

			pyttsx3.speak("you userid is {}".format(uid))
			print("\n you userid is",uid)

		
			pyttsx3.speak("You have successfully enter in system")
			print("\You have successfully enter in system")	


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
				server.login(uid,lpass)
				email = EmailMessage()
				email['From'] = uid
				email['To'] = receiver
				email['Subject'] = subject
				email.set_content(message)
				server.send_message(email)
				pyttsx3.speak("Congrats you have successfully sent an email")

			email_list = {
				'poonam' : 'blackpoonam1010@gmail.com',
				'deepak' : 'khetted@gmail.com'
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
				server.login(uid,lpass)
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


			elif(("two" in choice) or ("Two" in choice) or ("2" in choice) or ("tu" in choice) or ("to" in choice) or ("Tu" in choice) or ("To" in choice)):
				listener = sr.Recognizer()
				engine = pyttsx3.init()

				def talk(text):
					engine.say(text)
					engine.runAndWait()
      
				read_mail()

			while True:

				r = sr.Recognizer()

				with sr.Microphone() as source:
    
					pyttsx3.speak("Do You continue to read mail or compose mail")
					print("\nDo You continue to read mail or compose mail")
					pyttsx3.speak("Speak yes to continue with voice based email system")
					print("\n:Speak yes to continue with voice based email system")
					pyttsx3.speak("Speak no to exit from voice based email system")
					print("\n:Speak no to exit from voice based email system")
					secondchoice = r.listen(source)
					pyttsx3.speak("we got your choice")
					print("\nwe got your choice")
					print("\n\n--------------------------------------------------------------------------------------------")
					Secondchoice = r.recognize_google(secondchoice)
					pyttsx3.speak("you said {}".format(Secondchoice))
					print("\n you said",Secondchoice)
			
					if(("Yes" in Secondchoice) or ("yes" in Secondchoice)):
						pyttsx3.speak("Speak one to compose mail")
						print("\n:Speak one to compose mail")
						pyttsx3.speak("Speak two to read inbox")
						print("\n:Speak two to read inbox")
						con = r.listen(source)
						pyttsx3.speak("we got your choice")
						print("\nwe got your choice")
						print("\n\n--------------------------------------------------------------------------------------------")
						Con = r.recognize_google(con)
						pyttsx3.speak("you said {}".format(Con))
						print("\n you said",Con)        

						if(("one" in Con) or ("One" in Con) or ("1" in Con)):
        
							listener = sr.Recognizer()
							engine = pyttsx3.init()

							def talk(text):
								engine.say(text)
								engine.runAndWait()
							get_email_info()
					
						elif(("two" in Con) or ("Two" in Con) or ("Tu" in Con) or ("tu" in Con) or ("2" in Con)):
							listener = sr.Recognizer()
							engine = pyttsx3.init()

							def talk(text):
								engine.say(text)
								engine.runAndWait()
      
							read_mail()
        						
				
					elif(("No" in Secondchoice) or ("no" in Secondchoice)):
						break		






		else:
			print("You have enter wrong password")
			pyttsx3.speak("You have enter wrong password")


	
	else:
		pyttsx3.speak("You have enter wrong credentials")
		print("\You have enter wrong credentials")




elif ( (Userchoice=="no") or (Userchoice=="NO") ):

	engine=pyttsx3.init()
	engine.setProperty('rate',130)


	
	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("Speak your Nickname")
			print("\nSpeak your login Nickname:")

			l_nickname= r.listen(source)
			pyttsx3.speak("we got your Nickname")
			print("\nwe got your voice Nickname")
			

	print("\n\n--------------------------------------------------------------------------------------------")

	Lognickname=r.recognize_google(l_nickname)
	pyttsx3.speak("you said {}".format(Lognickname))
	print("\n you said",Lognickname)

	



	
	lname=myclass.query.filter_by(nickname=Lognickname).first()



	r = sr.Recognizer()

	with sr.Microphone() as source:
    
			pyttsx3.speak("Speak your Password")
			print("\nSpeak your login Password:")

			l_password= r.listen(source)
			pyttsx3.speak("we got your Password")
			print("\nwe got your voice Password")
			

	print("\n\n--------------------------------------------------------------------------------------------")

	Log_password=r.recognize_google(l_password)
	Logpassword=Log_password.replace(" ","")
	pyttsx3.speak("you said {}".format(Logpassword))
	
	
	
	
	l_pass=lname.password
	
	u_id=lname.userid
	
	if l_pass==Logpassword:
		print("You have enter correct password")
		pyttsx3.speak("You have enter correct password")

	
		lpass=str(l_pass)
		uid=str(u_id)
	
	
	
		if (lname and lpass):

			pyttsx3.speak("you userid is {}".format(uid))
			print("\n you userid is",uid)

		
			pyttsx3.speak("You have successfully enter in system")
			print("\You have successfully enter in system")	


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
				server.login(uid,lpass)
				email = EmailMessage()
				email['From'] = uid
				email['To'] = receiver
				email['Subject'] = subject
				email.set_content(message)
				server.send_message(email)

			email_list = {
				'poonam' : 'blackpoonam1010@gmail.com',
				'deepak' : 'khetted@gmail.com'
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
				server.login(uid,lpass)
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


			elif(("two" in choice) or ("Two" in choice) or ("2" in choice) or ("tu" in choice) or ("to" in choice) or ("Tu" in choice) or ("To" in choice)):
				listener = sr.Recognizer()
				engine = pyttsx3.init()

				def talk(text):
					engine.say(text)
					engine.runAndWait()
      
				read_mail()

			
			while True:

				r = sr.Recognizer()

				with sr.Microphone() as source:
    
					pyttsx3.speak("Do You continue to read mail or compose mail")
					print("\nDo You continue to read mail or compose mail")
					pyttsx3.speak("Speak yes to continue with voice based email system")
					print("\n:Speak yes to continue with voice based email system")
					pyttsx3.speak("Speak no to exit from voice based email system")
					print("\n:Speak no to exit from voice based email system")
					secondchoice = r.listen(source)
					pyttsx3.speak("we got your choice")
					print("\nwe got your choice")
					print("\n\n--------------------------------------------------------------------------------------------")
					Secondchoice = r.recognize_google(secondchoice)
					pyttsx3.speak("you said {}".format(Secondchoice))
					print("\n you said",Secondchoice)
			
					if(("Yes" in Secondchoice) or ("yes" in Secondchoice)):
						pyttsx3.speak("Speak one to compose mail")
						print("\n:Speak one to compose mail")
						pyttsx3.speak("Speak two to read inbox")
						print("\n:Speak two to read inbox")
						con = r.listen(source)
						pyttsx3.speak("we got your choice")
						print("\nwe got your choice")
						print("\n\n--------------------------------------------------------------------------------------------")
						Con = r.recognize_google(con)
						pyttsx3.speak("you said {}".format(Con))
						print("\n you said",Con)        

						if(("one" in Con) or ("One" in Con) or ("1" in Con)):
        
							listener = sr.Recognizer()
							engine = pyttsx3.init()

							def talk(text):
								engine.say(text)
								engine.runAndWait()
							get_email_info()
					
						elif(("two" in Con) or ("Two" in Con) or ("Tu" in Con) or ("tu" in Con) or ("2" in Con)):
							listener = sr.Recognizer()
							engine = pyttsx3.init()

							def talk(text):
								engine.say(text)
								engine.runAndWait()
      
							read_mail()
        						
				
					elif(("No" in Secondchoice) or ("no" in Secondchoice)):
						break					
			


					

		else:
			print("You have enter wrong password")
			pyttsx3.speak("You have enter wrong password")



	
	else:
		pyttsx3.speak("You have enter wrong credentials")
		print("\You have enter wrong credentials")



	
		
	

		
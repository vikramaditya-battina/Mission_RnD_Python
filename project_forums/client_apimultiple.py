__author__ = 'team 9'

import time
import socket               # Import socket module
import color_console as cons
from serialiser_and_deserialiser import *

s = socket.socket()         # Create a socket object
host ='10.3.10.202' # Get local machine name
port = 8090      # Reserve a port for your service.
s.connect((host, port))

class json():
    def __init__(self):
        self.choice='None'
        self.username='None'
        self.password='None'
        self.old='None'
        self.new='None'
        self.cnf='None'
        self.emailid='None'
        self.phone='None'
        self.current_time='None'
        self.cname='None'
        self.fname='None'
        self.author='None'
        self.ques='None'
        self.cmt='None'
        self.qid='None'
    def serialize(self):
        if self.choice=='login' or self.choice=='signup' or self.choice=='changepwd':
            return '{"choice":"'+self.choice+'","username":"'+self.username+'","password":"'+self.password+'","oldpwd":"'+self.old+'","newpwd":"'+self.new+'","cnfpwd":"'+self.cnf+'","email":"'+self.emailid+'","phone":"'+self.phone+'","current_time":"'+self.current_time+'"}'
        if self.choice=='createforum'  or self.choice=='postquestion' or self.choice=='postcomment':
            return '{"choice":"'+self.choice+'","current_time":"'+self.current_time+'","category":"'+self.cname+'","forumname":"'+self.fname+'","author":"'+self.author+'","question":"'+self.ques+'","comment":"'+self.cmt+'"}'
        if self.choice=='viewforums'or self.choice=='viewquestions' or self.choice=='viewcomments':
            return '{"choice":"'+self.choice+'","category":"'+self.cname+'","forumname":"'+self.fname+'"}'

def sending(mess,s):
    mess='START'+mess+'STOP'
    while mess!='':
        #print 'sending'
        s.send(mess[:1024])
        mess=mess[1024:]

def receive(s):
    message=''
    start=False
    while True:
        message_from_client=s.recv(1024)
        if message_from_client[:5] =='START' and message_from_client[-4:]=='STOP':
             message=message+message_from_client[5:-4]
             #print message_from_client
             #print 'client reciever'
             break
        elif message_from_client[:5]=='START' and start==False:
             start=True
             message=message+message_from_client[5:]
        elif message_from_client[-4:]=='STOP' and start==True:
            message=message+message_from_client[:-4]
            break
        else:
             message=message+message_from_client
    return message

def sign():
    cons.set_text_attr(cons.FOREGROUND_BLUE  |
                       cons.FOREGROUND_INTENSITY)
    print "1.sign in \n2.sign up \n3.anonymous 4.exit()"
    choice=raw_input("enter your choice:")
    #sending(choice,s)
    if choice=='1':
        uname=login()
        display_cat(uname)
    elif choice=='2':
        uname=signup()
        display_cat(uname)
    elif choice=='3':
        uname="anynoumous"
        display_cat(uname)
    elif choice=='4':
        exit()
    else:
        print "invalid option"
        sign()

def login():
    cons.set_text_attr(cons.FOREGROUND_GREEN |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="login"
    obj.username=raw_input("enter username:")
    obj.password=raw_input("enter password:")
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "login success"
        changepwd(obj.username)
        return obj.username
    else:
        print "invalid username or password.please try again"
        sign()

def changepwd(uname):
    cons.set_text_attr(cons.FOREGROUND_GREY|
                       cons.FOREGROUND_INTENSITY)
    choice=raw_input("change password?\n1.yes\n2.no\n")
    #sending(choice,s)
    if choice=='1':
        obj=json()
        obj.choice="changepwd"
        obj.username=uname
        obj.old=raw_input("enter old password:")
        obj.new=raw_input("enter new password:")
        obj.cnf=raw_input("confirm new password:")
        input=obj.serialize()
        sending(input,s)
        res=receive(s)
        if res=="True":
            print "password changed succesfully"
        else:
            print res
            changepwd(uname)
    elif choice=='2':
        return
    else:
        print "invalid option"
        changepwd(uname)


def signup():
    cons.set_text_attr(cons.FOREGROUND_GREY  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="signup"
    obj.username=raw_input("enter name:")
    obj.emailid=raw_input("enter mail id:")
    obj.phone=raw_input("enter mobile number:")
    obj.password=raw_input("create a password")
    obj.cnf=raw_input("confirm password")
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "registered successfully"
        return obj.username
    else:
        print res
        signup()


def display_cat(uname):
    obj=json()
    cons.set_text_attr(cons.FOREGROUND_CYAN|
                        cons.FOREGROUND_INTENSITY)
    print "available categories are\n 1.education\n2.sports\n3.politics\n4.current affairs\n5.technology\n6.others\n7.exit()"
    cat=raw_input("enter a category:")
    if cat == '1':
      obj.cname="education"
    elif cat == '2':
      obj.cname="sports"
    elif cat == '3':
      obj.cname="politics"
    elif cat == '4':
      obj.cname="current affairs"
    elif cat == '5':
       obj.cname="technology"
    elif cat == '6':
       obj.cname="others"
    else:
        exit()
    display_opt(uname,obj.cname)
def display_opt(uname,cat):
    if uname=="anynoumous":
      print "1.viewforums\n2.change categeory\n3.exit()"
      opt=raw_input("enter a vaid option")
      if opt=='1':
          viewforums(uname,cat)
          display_opt(uname,cat)
      elif opt=='2':
          display_cat(uname)
      elif opt=='3':
          exit()
      else:
          print "enter a valid option"
          display_opt(uname,cat)
    else:
      print "1.view forums\n2.create a forum\n3.enter a question\n4.change categeory\n5.exit()"
      opt=raw_input("enter a valid option")
      if opt=='1':
          viewforums(cat,uname)
          display_opt(uname,cat)
      elif opt=='2':
          createforum(uname,cat)
          display_opt(uname,cat)
      elif opt=='3':
          postquestion(cat,None,uname)
      elif opt=='4':
          display_cat(uname)
      elif opt=='5':
          exit()
      else:
          print "please enter a valid input"
          display_opt(uname,cat)

def viewforums(cat,uname):
    cons.set_text_attr(cons.FOREGROUND_YELLOW  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="viewforums"
    obj.cname=cat
    #if obj.cname!='education' and obj.cname!='sports' and obj.cname!='politics' and obj.cname!='current affairs'and obj.cname!='latest technology'and obj.cname!='others':
     #   print "enter a valid option"
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    if r=="1":
        print "empty forums list yet"
        return
    res=deserialiser(r)
    print "the forums of "+obj.cname+" are\n"
    for i in res["forumlist"]:
        print i
    print "1.select a forum to view questions\n2.post a question\n3.change cateogery\n 3.return"
    opt=raw_input("enter a valid option")
    if opt=='1':
        forum=raw_input("enter a forum name")
        '''i=0
        while i<len(res["forumlist"]):
            if i==forum:
                break
            i=i+1
        if i==len(res["forumlist"]):
               print "forum does not exist"
               return'''
        viewquestions(cat,forum,uname)
    elif opt=='2':
        forum=raw_input("enter a forum to post questions")
        postquestion(cat,forum,uname)
    elif opt=='3':
        display_cat(uname)
    elif opt=='4':
        return
def viewquestions(cat,forum,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="viewquestions"
    obj.cname=cat
    obj.fname=forum
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    if r == "1":
        print "empty forum yet"
        return
    res=deserialiser(r)
    print "the questions of the forum:"+obj.fname+"\n"
    for i in res["questionlist"]:
        print i
    print "1.post a comment\n2.change categeory3.view comments\n4.exit()"
    opt=raw_input("enter a valid option")
    if opt=='1':
        qid=raw_input("enter a valid q id")
        postcomment(cat,forum,qid,uname)
    elif opt=='2':
        display_cat(uname)
    elif opt=='3':
        qid=raw_input("enter a valid q id")
        viewcomments(cat,forum,qid)
    elif opt=='4':
        exit()
def isnumb(n):
    if str(n)>='0' or str(n)<='9':
        return True
    return False

def createforum(uname,cat):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.cname=cat
    obj.choice="createforum"
    obj.fname=raw_input("enter forum name:")
    obj.author=uname
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "forum created"
    else:
        print res
def postquestion(cat,forum,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice='postquestion'
    obj.cname=cat
    obj.fname=forum
    obj.ques=raw_input("enter question:")
    obj.author=uname
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "question posted"
    else:
        print res

def postcomment(cat,forum,qid,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="postcomment"
    obj.cname=cat
    obj.fname=forum
    obj.ques=qid
    obj.cmt=raw_input("enter a comment:")
    obj.author=uname
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "comment posted"
    else:
        print res
def  viewcomments(cat,forum,qid):
    obj=json()
    obj.choice="viewcomments"
    obj.cname=cat
    obj.forum=forum
    obj.qid=qid
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    print res
if __name__=="__main__":
    sign()

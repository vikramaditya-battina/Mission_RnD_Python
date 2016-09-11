__author__ = 'team 9'

import time
import socket               # Import socket module
import color_console as cons
import serialiser_and_deserialiser


s = socket.socket()         # Create a socket object
host = '10.3.10.202' # Get local machine name
port = 8090               # Reserve a port for your service.
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
    def serialize(self):
        if self.choice=='login' or self.choice=='signup' or self.choice=='changepwd':
            return '{"choice":"'+self.choice+'","username":"'+self.username+'","password":"'+self.password+'","oldpwd":"'+self.old+'","newpwd":"'+self.new+'","cnfpwd":"'+self.cnf+'","email":"'+self.emailid+'","phone":"'+self.phone+'","current_time":"'+self.current_time+'"}'
        if self.choice=='createforum' or self.choice=='postquestion' or self.choice=='postcomment':
            return '{"choice":"'+self.choice+'","current_time":"'+self.current_time+'","category":"'+self.cname+'","forumname":"'+self.fname+'","author":"'+self.author+'","question":"'+self.ques+'","comment":"'+self.cmt+'"}'
        if self.choice=='viewforums' or self.choice=='viewquestions' or self.choice=='viewcomments':
            return '{"choice":"'+self.choice+'","category":"'+self.cname+'","forumname":"'+self.fname+'","question":"'+self.ques+'"}'

def sending(mess,s):
    mess='START'+mess+'STOP'
    while mess!='':
        s.send(mess[:1024])
        mess=mess[1024:]

def receive(s):
    message=''
    start=False
    while True:
        message_from_client=s.recv(1024)
        if message_from_client[:5] =='START' and message_from_client[-4:]=='STOP':
             message=message+message_from_client[5:-4]
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
                       cons.FOREGROUND_INTENSITY )
    print "1.sign in \n2.sign up \n3.login as anonymous\n4.exit"
    choice=raw_input("enter your choice:")
    if choice=='1':
        login()
    elif choice=='2':
        signup()
    elif choice=='3':
        display_cat(uname="anonymous")
    elif choice=='4':
        input="exited"
        sending(input,s)
        print "\n",receive(s)
        exit(0)
    else:
        print "\ninvalid option"
        sign()

def login():
    cons.set_text_attr(cons.FOREGROUND_GREEN |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="login"
    obj.username=raw_input("\nenter username:")
    obj.password=raw_input("enter password:")
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "login success"
        changepwd(obj.username)
    else:
        print "\ninvalid username or password.please try again"
        login()

def changepwd(uname):
    cons.set_text_attr(cons.FOREGROUND_GREY|
                       cons.FOREGROUND_INTENSITY)
    choice=raw_input("\nchange password?\n1.yes\n2.no\n")
    if choice=='1':
        obj=json()
        obj.choice="changepwd"
        obj.username=uname
        obj.old=raw_input("\nenter old password:")
        obj.new=raw_input("enter new password:")
        obj.cnf=raw_input("confirm new password:")
        input=obj.serialize()
        sending(input,s)
        res=receive(s)
        if res=="True":
            print "\npassword changed successfully"
            display_cat(uname)
        else:
            print res
            changepwd(uname)
    elif choice=='2':
        display_cat(uname)
    else:
        print "\ninvalid option"
        changepwd(uname)


def signup():
    cons.set_text_attr(cons.FOREGROUND_GREY  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="signup"
    obj.username=raw_input("\nenter name:")
    obj.emailid=raw_input("enter mail id:")
    obj.phone=raw_input("enter mobile number:")
    obj.password=raw_input("create a password")
    obj.cnf=raw_input("confirm password")
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "\nregistered successfully"
        display_cat(obj.username)
    else:
        print res
        signup()

def display_cat(uname):
    obj=json()
    cons.set_text_attr(cons.FOREGROUND_CYAN|
                        cons.FOREGROUND_INTENSITY)
    print "\navailable categories are\n1.education\n2.sports\n3.politics\n4.current affairs\n5.technology\n6.others\n7.logout"
    cat=raw_input("select a category:")
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
    elif cat=='7':
        print "\nlogged out successfully\n"
        sign()
    else:
        print "\ninvalid option"
        display_cat(uname)
    display(obj.cname,uname)


def display(cname,uname):
    cons.set_text_attr(cons.FOREGROUND_CYAN|
                        cons.FOREGROUND_INTENSITY)
    if uname=="anonymous":
        print "\n1.view forums\n2.change category\n3.logout"
        choice=raw_input("enter your choice:")
        if choice=='1':
            viewforums(cname,uname)
        elif choice=='2':
            display_cat(uname="anonymous")
        elif choice=='3':
            print "\nlogged out successfully\n"
            sign()
        else:
            print "\ninvalid choice"
            display(cname,uname="anonymous")
    else:
        print "\n1.view forums\n2.create a forum\n3.change category\n4.exit"
        choice=raw_input("enter your choice:")
        if choice=='1':
            viewforums(cname,uname)
            display(cname,uname)
        elif choice=='2':
            createforum(cname,uname)
        elif choice=='3':
            display_cat(uname)
        elif choice=='4':
            print "\nlogged out successfully\n"
            sign()
        else:
            print "\ninvalid choice"
            display(cname,uname)

def viewforums(cname,uname):
    cons.set_text_attr(cons.FOREGROUND_YELLOW  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="viewforums"
    obj.cname=cname
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
#    if r=="1":
 #       print "\nempty forums list"
  #      print "choose another category"
   #     display_cat(uname)
    res=serialiser_and_deserialiser.deserialiser(r)
    print "............res........",res
    if res["forumlist"] == []:
        print "\nempty forums list"
        print "choose another category"
        display_cat(uname)
    else:
        print "\nthe forums of "+obj.cname+" are:"
        for i in res["forumlist"]:
            print i
        display1(cname,uname)


def display1(cname,uname):
    print "\n1.view a forum\n2.choose another category\n3.logout"
    choice=raw_input("enter your choice")
    if choice=='1':
        fname=raw_input("\nenter a forum name:")
        viewquestions(cname,fname,uname)
    elif choice=='2':
        display_cat(uname)
    elif choice=='3':
        print "\nlogged out successfully\n"
        sign()
    else:
        print "\ninvalid choice"
        viewforums(cname,uname)

def display_options(cname,fname,uname):
    print "\n1.post a question\n2.comment on a question\n3.view comments\n4.view another forum\n5.change category\n6.logout"
    choice=raw_input("select a option:")
    if choice=='1':
        postquestion(cname,fname,uname)
    elif choice=='2':

        postcomment(cname,fname,uname)
    elif choice=='3':

        viewcomments(cname,fname,uname)
    elif choice=='4':
        fname=raw_input("\nenter forum name:")
        viewquestions(cname,fname,uname)
    elif choice=='5':
        display_cat(uname)
    elif choice=='6':
        print "\nlogged out successfully\n"
        sign()
    else:
        print "\ninvalid choice"
        display_options(cname,fname,uname)


def viewquestions(cname,fname,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="viewquestions"
    obj.cname=cname
    obj.fname=fname
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    res=serialiser_and_deserialiser.deserialiser(r)
    if res["questionslist"] == []:
        print "\nempty forum yet"
        display_options(cname,fname,uname)
    else:
        print "\nquestions of the forum "+obj.fname+":"
        for i in res["questionslist"]:
            print i
        display_options(cname,fname,uname)


def createforum(cname,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.cname=cname
    obj.choice="createforum"
    obj.fname=raw_input("\nenter forum name:")
    obj.author=uname
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "\nforum created"
        display(cname,uname)
    else:
        print res
        display(cname,uname)


def postquestion(cname,fname,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="postquestion"
    obj.cname=cname
    obj.fname=fname
    obj.author=uname
    ques=raw_input("\nenter a question to be posted:")
    obj.ques=ques
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "\nquestion posted"
        display_options(cname,fname,uname)
    else:
        print "\n",res
        display_options(cname,fname,uname)


def postcomment(cname,fname,uname):
    cons.set_text_attr(cons.FOREGROUND_MAGENTA  |
                       cons.FOREGROUND_INTENSITY)
    obj=json()
    obj.choice="viewquestions"
    obj.cname=cname
    obj.fname=fname
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    res=serialiser_and_deserialiser.deserialiser(r)
    if res["questionslist"] == []:
        print "\nempty forum yet"
    else:
        print "\nquestions of the forum "+obj.fname+":"
        for i in res["questionslist"]:
            print i
    obj.choice="postcomment"
    obj.ques=raw_input("\nselect a question id:")
    obj.cmt=raw_input("enter a comment:")
    obj.author=uname
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    res=receive(s)
    if res=="True":
        print "\ncomment posted"
        display_options(cname,fname,uname)
    else:
        print "\n",res
        display_options(cname,fname,uname)

def viewcomments(cname,fname,uname):
    obj=json()
    obj.choice="viewquestions"
    obj.cname=cname
    obj.fname=fname
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    res=serialiser_and_deserialiser.deserialiser(r)
    if res["questionslist"] == []:
        print "\nempty forum yet"
    else:
        print "\nquestions of the forum "+obj.fname+":"
        for i in res["questionslist"]:
            print i
    obj=json()
    obj.choice="viewcomments"
    obj.cname=cname
    obj.fname=fname
    obj.ques=raw_input("select a question id:")
    obj.current_time=time.asctime( time.localtime(time.time()) )
    input=obj.serialize()
    sending(input,s)
    r=receive(s)
    print "...............",r
    res=serialiser_and_deserialiser.deserialiser(r)
    print"..............deserializer.......",res
    if res["commentlist"] == []:
        print "\nempty forum yet"
        display_options(cname,fname,uname)
    else:
        print "\nquestions of the forum "+obj.fname+":"
        for i in res["commentlist"]:
            print i
        display_options(cname,fname,uname)

if __name__=="__main__":
    sign()

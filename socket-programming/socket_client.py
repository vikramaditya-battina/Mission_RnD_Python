import socket
from serialiser import *
from serialiser_and_deserialiser import *
class forum(object):
    def __init__(self):
        self.keyword=None
        self.name=None
        self.message=None

def recieve(c):
    message=''
    while True:
        message_from_client=c.recv(1024)
        if message_from_client[:5] =='START' and message_from_client[-4:]=='STOP':
             message=message+message_from_client[5:-4]
             print message_from_client
             print 'client reciever'
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

def sending(mess,c):
    mess='START'+mess+'STOP'
    while mess!='':
        print 'sending'
        c.send(mess[:1024])
        mess=mess[1024:]


def client():
    s=socket.socket()
    host=socket.gethostname()
    port=12345
    s.connect((host,port))
    while True:
        print '1.ADD FORUM'
        print '2.VIEW FORUM'
        print '3.ADD MESSAGE'
        print '4.VIEW MESSAGE'
        print '5.EXIT'
        option=raw_input('enter your option')
        frm=None
        if option=='1':
            name=raw_input('enter the forum name')
            frm=forum()
            frm.keyword='create'
            frm.name=name
        elif option=='2':
            frm=forum()
            frm.keyword='viewforums'
        elif option=='3':
            name=raw_input('enter the forum name')
            message=raw_input('enter the message')
            frm=forum()
            frm.keyword='post'
            frm.name=name
            frm.message=message
        elif option=='4':
            name=raw_input('enter the forum which u want to view the message')
            frm=forum()
            frm.keyword="viewmessages"
            frm.name=name
        elif option=='5':
            frm=forum()
            frm.keyword='exit'

        else:
            print 'ENTER VALID OPTION '
            continue
        dict={}
        if frm.name!=None:
           dict['name']=frm.name
        if frm.keyword!=None:
           dict['keyword']=frm.keyword
        if frm.message!=None:
            dict['message']=frm.message
        data=serialiser(dict)

        sending(data,s)

        mess=recieve(s)

        mess=deserialiser(mess)

        for i in mess:
            print i
        if option=='5':
            break



















if __name__=='__main__':
    client()
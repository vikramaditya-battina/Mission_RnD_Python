import socket
from serialiser_and_deserialiser import *
from  serialiser  import *
forumobjects={}
fp=None
class forum(object):
    def __init__(self,name):
        self.forumname=name
        self.messages=[]


def write_to_file():
    fp=open('backup.txt','w')
    keys=forumobjects.keys()
    for i in keys:
        forumobjects[i]=forumobjects[i].messages
    print 'this is the forumobjects',forumobjects
    string=serialiser(forumobjects)
    print 'matter to be written in file',string
    fp.write(string)

def recieve(c):
    mess=''
    start=False
    while True:
        print 'reciver1'
        message_from_client=c.recv(1024)

        if message_from_client[:5] =='START' and message_from_client[-4:]=='STOP':
             print   'in the reciever'
             mess=mess+message_from_client[5:-4]
             break
        elif message_from_client[:5]=='START' and start==False:
             start=True
             mess=mess+message_from_client[5:]
        elif message_from_client[-4:]=='STOP' and start==True:
            mess=mess+message_from_client[:-4]
            break
        else:
             mess=mess+message_from_client

    return mess

def sending(mess,c):
    mess='START'+mess+'STOP'
    while mess!='':
        print 'sending in the server'
        c.send(mess[:1024])
        mess=mess[1024:]

def analyse(dict,c):
    if dict['keyword']=='create':
        name=dict['name']
        if name in forumobjects:
            mess='START'+'[ "sorry name not avialable"]'+'STOP'
            c.send(mess)
        else:
            forumobjects[name]=forum(name)
            mess='START'+'["SUCCESSFULLY ADDED"]'+'STOP'
            c.send(mess)
    if dict['keyword']=='viewforums':

        lis=forumobjects.keys()
        if lis==[]:
            c.send('START'+'["SORRY NO FORUMS TO DISPLAY"]'+'STOP')
        else:
            mess=serialiser(lis)

            sending(mess,c)
    if dict['keyword']=='viewmessages':

        lis=forumobjects[dict['name']].messages
        if lis==[]:
            c.send('START["sorry no messages to display"]STOP')
        else:
            mess=serialiser(lis)
            sending(mess,c)
    if dict['keyword']=='post':
        if dict['name'] in forumobjects:

            forumobjects[dict['name']].messages.append(dict['message'])
            c.send('START["posted sucessfully"]STOP')
        else:
            c.send('START["no such forum name"]STOP')
    if dict['keyword']=='exit':
        write_to_file()
        c.send('START["exited succesfully"]STOP')







s=socket.socket()
host=socket.gethostname()
port=12345
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
try:
    string=open('backup.txt')
    print 'readed string',string
    datastructure=deserialiser(string)
    for i in datastructure:
        x=forum(i)
        x.messages=datastructure[i]
        forumobjects[i]=x
except:
    pass
while True:
    message=recieve(c)
    dict=deserialiser(message)
    print dict
    analyse(dict,c)





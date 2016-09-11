from bottle import route, run, request, get, post, response,static_file

from serialiser_and_deserialiser import *

from serialiser import *

forumsDict = dict()
class forum:
    name=""
    subforums=[]
    message=[]

class message:
    content=""
    reply=[]


@route('/hello')
def gethello():
    return "Hello World!"

@route('/forums')
def getForums():
    string=''
    for i in forumsDict.keys():
        string=string+'\n'+i

    return string




@route('/addforum', method='POST')
def addForum():
    forumname = request.forms.forumname
    if forumname in forumsDict:
        return 'sorry name already exists choose another name'
    author = request.forms.author
    forumsDict[forumname]={}
    forumsDict[forumname]['forumname']=forumname
    forumsDict[forumname]['author']=author
    return '''FORUM CREATED SUCCESSFULLY '''

@route('/forums/<forumname>/<subforumname>')
def subforum(forumname,subforumname):
    dic=forumsDict[forumname]['subforumname']
    string=''
    for i in dic['messages']:
        string=string+'\n\n\n\n\n'
    return string
@route('/forums/<forumname>/<subforumname>/addmessage')
def messaging(forumname,subforumname):
    if forumname not in forumsDict:
        return 'no such forum exists'

@route('/forums/<forumname>')
def printing_about_forum(forumname):
    if 'subgroups' in forumsDict[forumname]:
        subforums=forumsDict[forumname]['subgroups']
        string='_________subforms are__________'
        for i in subforums:
            string=string+(i['name'])+'\n\n\n'
    if 'messages' in forumsDict[forumname]:
        messages=forumsDict[forumname]['messages']
        string=string+'________message________________'
        for i in messages:
           string=string+i+'\n\n'
    else:
        string='nothing else to display'

    return string
@route('/forums/<forumname>/addmessage', method='POST')
def messagepost(forumname):

    message=request.forms.messsage
    if 'message' not in forumsDict[forumname]:

        forumsDict[forumname]['messages']=[]
    else:
        forumsDict[forumname]['messages'].append(message)
    return 'message posted successfully'

@route('/forums/<forumname>/addforum',method='POST')
def creating_subforms(forumname):
    formname=request.forms.forumname
    author=request.POST['author']
    if 'subforums' not in forumsDict[forumname]:
        forumsDict[forumname]['subforums']=[]
    x={}
    x['forumname']=formname
    x['author']=author
    if formname in forumsDict[forumname]['subforums']:
        return 'sorry that name exists'
    forumsDict[forumname]['subforums'].append(x)
    return 'added subforum in '+forumname+formname+author



@route('/forums/<forumname>')
def getForum(forumname):
    mess=''
    messages=forumsDict[forumname]
    for i in messages[messages]:

        mess=mess+i+'\n\n\n\n'

    return mess

run(host='localhost', port=8080, debug=True, reloader=True)

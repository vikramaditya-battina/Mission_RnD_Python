def deserialiser(string):
    string=trimmingspaces(string)
    if string[0]=='{' and string[-1]=='}':  #checking whether given thing is dictionary or the list
        return dictionary(string)

    elif string[0]=='[' and string[-1]==']':
        return listconversion(string)
    else:
        raise Exception,'some syntax mistake is there'


def dictionary(string):
    i=1
    key=''
    value=''
    dict={}
    keybool=False
    valuebool=False
    pairparse=True
    while i<len(string)-1:
        if string[i]=='"' and keybool==False and valuebool==False:  #determinig the quotes whether for key or the value
            keybool=True
            i=i+1
            while i<len(string)-1:
                if string[i]=='"':
                    i=i+1
                    break
                key=key+string[i]
                i=i+1

            if string[i]!=':':
                raise Exception,'expecting the : for key and dictionary'
            i=i+1
            continue
        elif  keybool==True and valuebool==False:
            valuebool=True
            if string[i]!='"':
                x=i
                if string[i]=='{':
                    count=0
                    while i<len(string)-1:
                        if string[i]=='{':
                            count=count+1
                        elif string[i]=='}':
                            count=count-1
                        if count==0:
                            i=i+1
                            break
                        i=i+1
                    dict[key]=deserialiser(string[x:i])
                    pairparse=True
                    continue
                if string[i]=='[':
                    count=0
                    while i<len(string)-1:
                        if string[i]=='[':
                            count=count+1
                        elif string[i]==']':
                            count=count-1
                        if count==0:
                            i=i+1
                            break
                        i=i+1
                    dict[key]=deserialiser(string[x:i])
                    pairparse=True
                    continue
                else:#we can code it for numbers
                    value=''

                    while i<len(string)-1:
                        if string[i]==',' :

                            break
                        else:
                            value=value+string[i]
                        i=i+1

                    try:
                        value=float(value)
                        dict[key]=value
                    except ValueError:
                        raise Exception,'object value can be either number ,string ,dict'
                    pairparse=True
                    continue

            else:

                i=i+1
                while i<len(string)-1:
                    if string[i]=='"':
                        i=i+1
                        break
                    value=value+string[i]
                    i=i+1
                dict[key]=value
                pairparse=True
                continue
        elif pairparse==True:
            if string[i]!=',':

                raise Exception,'expecting the comma as the delimeter'
            if string[i]==',' and string[i+1]=='}':
                raise Exception,'not expecting the at the end of the value in the dictinary'
            pairparse=False
            value=''
            key=''
            keybool=False
            valuebool=False

        i=i+1

    return dict

def listconversion(string):
    i=1
    valuebool=False
    parsebool=False
    value=''
    list=[]

    while i<len(string)-1:
        if parsebool==False:
            if string[i]=='"':
                i=i+1
                while i<len(string)-1:
                    if string[i]=='"':
                        i=i+1
                        break
                    value=value+string[i]
                    i=i+1
                list.append(value)
                parsebool=True
                continue
            if string[i]=='{':
                    count=0
                    x=i
                    while i<len(string)-1:
                        if string[i]=='{':
                            count=count+1
                        elif string[i]=='}':
                            count=count-1
                        if count==0:
                            i=i+1
                            break
                        i=i+1
                    list.append(deserialiser(string[x:i]))
                    parsebool=True
                    continue
            if string[i]=='[':
                count=0
                x=i
                while i<len(string)-1:
                    if string[i]=='[':
                        count=count+1
                    elif string[i]==']':
                        count=count-1
                    if count==0:
                        i=i+1
                        break
                    i=i+1
                list.append(deserialiser(string[x:i]))
                parsebool=True
                continue
            if string[i].isdigit():
                floatbool=False
                while i<len(string)-1:
                    if string[i]==',':
                        break
                    if string[i].isdigit()==False:
                        if string[i]=='.' and floatbool==False:
                            value=value+'.'
                            floatbool=True
                        else:
                            raise Exception,'list should contain data in the in quotes'
                    value=value+string[i]
                    i=i+1
                list.append(float(value))
                parsebool=True
                continue
        if parsebool==True:
            if string[i]!=',':
                raise Exception,'excpecting commas as dellimiter'
            if string[i]==',' and string[i+1]==']':
                raise Exception,'expecting no comma'
            value=''
            parsebool=False
        i=i+1
    return list
def trimmingspaces(string):
    i=0
    quotes=False
    newstring=''

    while i< len(string):
        if (string[i]=='"') and quotes==False:
            newstring=newstring+'"'

            quotes=True
            i=i+1
            continue
        elif string[i]=='"' and quotes==True:
            newstring=newstring+'"'
            quotes=False
            i=i+1
            continue
        if quotes==False:
            if not (string[i]==' ' or string[i]=='\n'):
                newstring=newstring+string[i]
        else:
            newstring=newstring+string[i]
        i=i+1
    return   newstring

if __name__=='__main__':
    fp=open('test_write.txt')
    string=fp.read()
    jsonstring=trimmingspaces('["1","2","3"]')
    print deserialiser(jsonstring)


def serialiser(datastructure):
    newstring=''
    if type(datastructure).__name__ == 'list':
        newstring=list_serialisation(datastructure)
    if type(datastructure).__name__=='dict':
        newstring=dict_serialisation(datastructure)
    return newstring

def list_serialisation(datastructure):
    newstring='['
    i=0
    if len(datastructure)==0: newstring=newstring+']'
    while i<len(datastructure)-1:
        if type(datastructure[i]).__name__=='str':
            newstring=newstring+'"'+datastructure[i]+'"'+','
        if type(datastructure[i]).__name__=='dict':
            newstring=newstring+serialiser(datastructure[i])+','
        if type(datastructure[i]).__name__=='list':
            newstring=newstring+serialiser(datastructure[i])+','
        i=i+1
    if i==len(datastructure)-1:
        if type(datastructure[i]).__name__=='str':
            newstring=newstring+'"'+datastructure[i]+'"'+']'
        if type(datastructure[i]).__name__=='dict':
            newstring=newstring+serialiser(datastructure[i])+']'
        if type(datastructure[i]).__name__=='list':
            newstring=newstring+serialiser(datastructure[i])+']'
    return newstring

def dict_serialisation(datastructure):
    newstring='{'
    i=0
    lis=datastructure.keys()
    if len(lis)==0 :newstring=newstring+'}'
    while i<len(lis)-1:
        newstring=newstring+'"'+lis[i]+'"'+':'
        if type(datastructure[lis[i]]).__name__=='str':
            newstring=newstring+'"'+datastructure[lis[i]]+'"'+','
        if type(datastructure[lis[i]]).__name__=='dict':
            newstring=newstring+serialiser(datastructure[lis[i]])+','

        if type(datastructure[lis[i]]).__name__=='list':
            newstring=newstring+serialiser(datastructure[lis[i]])+','
        i=i+1

    if i==len(lis)-1:
        newstring=newstring+'"'+lis[i]+'"'+':'
        if type(datastructure[lis[i]]).__name__=='str':
            newstring=newstring+'"'+datastructure[lis[i]]+'"'
        if type(datastructure[lis[i]]).__name__=='dict':
            newstring=newstring+serialiser(datastructure[lis[i]])

        if type(datastructure[lis[i]]).__name__=='list':
            newstring=newstring+serialiser(datastructure[lis[i]])

    newstring=newstring+'}'
    return newstring

if __name__=='__main__':
    lis={'sumath':[],'vikram':['hi ra ela vunnavu ra mama']}
    print lis
    print serialiser(lis)



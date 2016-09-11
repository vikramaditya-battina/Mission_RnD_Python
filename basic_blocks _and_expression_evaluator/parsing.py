from treeutils import *
symboltable={}
def parsing(string):#creating tree
    if len(string)==1 or string.isdigit():
          if string.isdigit():
             return TreeNode(int(string))
          else:
              return TreeNode(string)
    if string:

        if string[-1].isdigit():
            i=len(string)-1
            placevalue=1
            value=0
            while i>=0:

                if string[i].isdigit():


                    value=value+placevalue*int(string[i])
                    placevalue=placevalue*10
                else:
                    break
                i=i-1

            root=TreeNode(string[i])
            root.right=TreeNode(value)
            root.left=parsing(string[:i])
            return root

        else:
            root=TreeNode(string[-2])  #operator
            root.right=TreeNode(string[-1])      #operand
            root.left=parsing(string[:-2]) #skipping that operator and operand
            return root


def preordertraversal(root):
    if root:
        preordertraversal(root.left)
        print root.value,
        preordertraversal(root.right)
def isvariable(value):
    if type(value).__name__ !='str':
        return False
    if ( ord(value)>=ord('a') and ord(value)<=ord('z') ) or (ord(value)>=ord('A') and ord(value)<=ord('Z')):
        return True
    else:
        return False


def evaluator(root):
    if root.left==None and root.right==None:
        if isvariable(root.value):
            return symboltable[root.value]
        else:
            return root.value
    else:
        x=evaluator(root.left)
        y=evaluator(root.right)
        if root.value=='*':
            return x*y
        elif root.value=='+':
            return x+y
        elif root.value=='-':
            return x-y
        elif root.value=='/':
            if y==0:
                print 'division by zero not allowed'
                exit(0)
            return x/y


def isoperator(string):
    if string=='*' or string=='+' or string=='-' or string=='/':
        return True
    else:
        return False


def isdefined(string):
    if string in symboltable:

        return True
    else:

        return False


def check_whether_place_of_operators(root):
    if root.left==None and root.right==None:
        if isoperator(root.value):

            return False
        elif type(root.value).__name__ =='int':

            return True
        elif not isdefined(root.value):

            return False
        else:
            return True
    if root.left!=None and root.right!=None:

        x= check_whether_place_of_operators(root.left) and check_whether_place_of_operators(root.right)
        y=isoperator(root.value)

        return x and y

def assingment_evaluator(root):
    result=evaluator(root.right)
    symboltable[root.left.value]=result

def error_checking(root):
    if root.value!='=':

        return False
    if isvariable(root.left.value)!=True:

        return False
    x=check_whether_place_of_operators(root.right)
    if True!= x:
        print x            #internal nodes should contain the oparators and leaf shold contain data
        return False
    return True


def parse(string):
    root=TreeNode(string[1])
    root.left=TreeNode(string[0])
    root.right=parsing(string[2:])
    return root

def trimming_of_spaces(string):
    newstring=''
    i=0
    while i<len(string):
        if string[i]!=' ':
            if string[i].isdigit():
                while i<len(string)  and (string[i]==' ' or string[i].isdigit()):
                    newstring=newstring+string[i]
                    i=i+1
                continue
            newstring=newstring+string[i]
        i=i+1
    return newstring
def trimallspaces(string):
    newstring=''
    for char in string:
        if char!=' ':
            newstring=newstring+char
    return newstring

def main():
    print 'if u want to stop the evaluator just enter "exit"'
    print 'evalautor starts....'
    while True:
        try:
            x=input('------>>')
        except Exception:
            print 'you should enter string in single or double quotes'
            continue
        if type(x).__name__ != 'str':
             print 'error message---enter a expression string'
             return None
        x=trimming_of_spaces(x)
        if not checking_number_error(x):
            print 'some error occured space between number not allowed'
            return
        x=trimallspaces(x)
        if x=='exit':
             print 'thanks...'
             return
        else:
             root=parse(x)
             if error_checking(root)==True:  #no error is there
                   assingment_evaluator(root)
                   print 'value of',root.left.value,'is',symboltable[root.left.value]
             else:
                   print 'error in expression'
def checking_number_error(x):
    i=len(x)-1
    number=False
    while i>=0:
        if x[i].isdigit():
            number=True
        elif x[i]==' ' and number==True:
            return False
        else:
            number=False
        i=i-1
    return True



if __name__=='__main__':
    main()

from parsing import *
def reading_blocks(program):
    fp=open(program)
    basicblocks=[]
    leaders=[]
    if_before=False
    codelines=fp.readlines()
    i=0
    while i<len(codelines):
        if codelines[i]=='\n':
            i=i+1
            continue
        if codelines[i][0:2]=='if':
            if leaders==[]:
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]

            else:
                basicblocks.append(leaders)
                leaders=[]
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]
            i=i+1
            if i<len(codelines):
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]
            i=i+1
            if i<len(codelines):
                if codelines[i][0:4]=='else':
                    i=i+1
                    if i<len(codelines):
                        leaders.append(codelines[i])
                        basicblocks.append(leaders)
                        leaders=[]
                i=i+1
                continue
        elif codelines[i][0:5]=='while':

            if leaders!=[]:
                basicblocks.append(leaders)
                leaders=[]
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]
            else:
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]
            i=i+1
            if i<len(codelines):
                leaders.append(codelines[i])


            i=i+1
            if i<len(codelines):
                leaders.append(codelines[i])
                basicblocks.append(leaders)
                leaders=[]
            i=i+1
            continue
        else:
            leaders.append(codelines[i])
        i=i+1

    return basicblocks

def evaluation_of_relation(relatn):
    i=0
    if isvariable(relatn[0]):
        if relatn[0] in symboltable:
            left=symboltable[relatn[0]]
            i=i+1
        else:

            print 'undefined expression error in conditional expression',relatn
            exit(0)
    else:
        i=0
        while i<len(relatn):
            if not relatn[i].isdigit():
               break
            i=i+1
        left=int(relatn[:i])
    if isvariable(relatn[-1]):
        j=len(relatn)-1
        if relatn[-1] in symboltable:
            right=symboltable[relatn[-1]]
            j=j-1

        else:

            print 'some undefined variable error in conditional expression',relatn
            exit(0)
    else:
        j=len(relatn)-1
        while j>=0:
            if not relatn[j].isdigit():
                break
            j=j-1
        right=int(relatn[j+1:])
    op=relatn[i:j+1]
    if op=='>':
        return left>right
    elif op=='>=':
        return left>=right
    elif op=='<':
        return left<right
    elif op=='<=':
        return left<=right
    elif op=='==':
        return left==right
    else:
        print 'sorry irrelavent relational operator'
        exit(0)



def evaluator_for_condition(stmt):
    i=0

    if 'and' in stmt and 'or' in stmt:
        index1=stmt.find('or')
        index2=stmt.find('and')
        if index1<index2:
            return evaluation_of_relation(stmt[:index1]) or evaluator_for_condition(stmt[index1+2:])
        else:
            return evaluation_of_relation(stmt[:index2]) and evaluator_for_condition(stmt[index2+3:])

    elif 'and' in stmt :
        index=stmt.find('and')
        return evaluation_of_relation(stmt[:index]) and evaluator_for_condition(stmt[index+3:])
    elif 'or' in stmt:
        index=stmt.find('or')
        return evaluation_of_relation(stmt[:index]) or evaluator_for_condition(stmt[index+2:])
    else:
        return evaluation_of_relation(stmt)


def determining_control_flow(basicblocks):
    controlflow=[]
    i=0
    whiletrue=False
    inwhile=False
    while i<len(basicblocks):
        j=0
        print i+1,'-->',
        block=basicblocks[i]
        while j<len(block):


            if block[j][0:2]=='if':
                stmt=trimming_of_spaces(block[j])
                if not checking_number_error(stmt):
                    print 'error in expression',block[j]
                    return
                stmt=trimallspaces(stmt)
                if stmt[-1]!=':':
                    print ':'+'missing in '+block[j]
                    return
                if not evaluator_for_condition(stmt[2:-1]):
                    i=i+1
                    break


            elif block[j][0:5]=='while':
                whiletrue=True
                inwhile=True
                stmt=trimming_of_spaces(block[j])
                if not checking_number_error(block[j]):
                    print 'error in expression',block[j]
                    return
                stmt=trimallspaces(stmt)
                if stmt[-1]!=':':
                    print ':'+'missing in'+block[j]
                    return
                if not evaluator_for_condition(stmt[5:-1]):
                    i=i+1
                    whiletrue=False
                    inwhile=False
                    break


            elif whiletrue:
                inwhile=False
                stmt=trimming_of_spaces(block[j])
                if not checking_number_error(stmt):
                    print 'error in statement',stmt
                    return
                root=parse(stmt)
                if not error_checking(root):
                    print 'error in expression',stmt
                    return
                assingment_evaluator(root)
            else:
                stmt=trimming_of_spaces(block[j])
                if  checking_number_error(stmt)==False:
                    print 'error in statement',stmt
                    return
                root=parse(stmt)
                if not error_checking(root):
                    print 'error in expression',stmt
                    return
                assingment_evaluator(root)


            j=j+1
        if whiletrue and not inwhile:
            i=i-1
        else:
            i=i+1



def removing_enter_end(basicblocks):
    i=0
    while i<len(basicblocks):
        j=0
        block=basicblocks[i]
        while j<len(block):
            block[j]=block[j][0:-1]
            j=j+1
        basicblocks[i]=block
        i=i+1
    return basicblocks



def main():
    program=raw_input('enter the file name contains the programm')
    basicblocks=reading_blocks(program)
    basicblocks=removing_enter_end(basicblocks)
    i=1
    for block in basicblocks:
        print i,':'
        for stmt in block:
            print stmt
        i=i+1
    determining_control_flow(basicblocks)

if __name__ == '__main__':
    main()

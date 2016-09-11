__author__ = 'hemavishnu'

notes = """
    This is to refresh your bit manipulation skills.
"""


#Convert integer to binary string and return the string.
#Integers also include negative numbers. So for negative numbers represent in two's complement.
#Integers are 32-bit integers.
def integer_to_binary(input):
    binary=''
    flag=0
    if input<0:
        flag=1
        input=input*(-1)

    while input:
        binary=str(input&1)+binary
        input=input>>1

    if flag==1:
        newbinary=''
        if binary[-1]=='1':
            for i in range(len(binary)-1):
                if i=='1':
                    newbinary=newbinary+'0'
                else:
                    newbinary=newbinary+'1'
        else:
            i=len(binary)-1
            while i>=0:

                if binary[i]=='1':
                    newbinary=newbinary+'1'
                    i=i-1
                    break
                newbinary=newbinary+'0'
                i=i-1
            while i>=0:

                if binary[i]=='1':
                    newbinary=newbinary+'0'
                else:
                    newbinary=newbinary+'1'
                i=i-1
        return newbinary
    return binary
    pass


#write tests to test your solution
#def test_integer_to_binary():

def main():
    print integer_to_binary(-10)

if  __name__=='__main__':
    main()
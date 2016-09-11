from struct import *

def zeroblock():
    fp=open('binary.bin.bin','rb+')
    fp.seek(0,0)
    x=pack('I',1073741824)  #size of the file system
    fp.write(x)

    x=pack('I',2048)         #address of the inode block
    fp.write(x)

    x=pack('I',3072)        #address of  the userdata base
    fp.write(x)

    x=pack('I',1048571)     #number of the free blocks
    fp.write(x)

    x=pack('H',255)         #index of the free disk block
    fp.write(x)

    x=pack('I',4096)        #address of the free disk block
    fp.write(x)


    x=pack('H',100)         #size of the inode list
    fp.write(x)


    x=pack('H',99)          #index of the  next free inode block
    fp.write(x)

    fp.seek(1012,0)
    fp.write(pack('I',3072))

    fp.seek(3072+1020,0)
    fp.write(pack('I',1))
    fp.close()




def intialise_freediskblocklist():
    fp=open('binary.bin','rb+')
    freeblock=4096
    free_block_offset=5120
    offset=4096
    i=0
    num=0
    while num<1048571:

        fp.seek(freeblock)
        i=0
        while i<256:
           if i==0:
               freeblock=free_block_offset

           x=pack('I',free_block_offset)
           fp.write(x)
           free_block_offset+=1024
           i=i+1
           num=num+1

        num=num+1
    fp.close()

def printtingfreeblocklist():
    offset=4096
    i=0
    fp=open('igb.bin','rb')
    while i<1048571:
        fp.seek(offset)
        x=fp.read(1024)
        fmt='I'*256
        result= unpack(fmt,x)
        offset=result[0]
        print result
        i=i+256
def printtingfreeblock():
    fp=open('igb.bin','rb')
    offset=4096
    fp.seek(offset)
    fmt='I'*256
    x=fp.read(1024)
    result=unpack(fmt,x)
    print result
    print '--------------------------------------'
    offset=result[0]
    fp.seek(offset)
    fmt='I'*256
    x=fp.read(1024)
    result=unpack(fmt,x)
    print result
def return_a_freeblock():
      #reading the index in the zeroth block
    fp=open('binary.bin','rb+')
    fp.seek(16,0)
    indexB=fp.read(2)
    index=unpack('H',indexB)
    index=index[0]


                  #reading addresss of the free disk block
    adrees_of_free_block=fp.read(4)
    adrees_of_free_block=unpack('I',adrees_of_free_block)
    adrees_of_free_block=adrees_of_free_block[0]

    fp.seek(adrees_of_free_block,0)             #going the address of the free disk blocks
    if index!=0:

        fp.seek(index*4,1)                       #going to the corresponding address
        freeblock=fp.read(4)                   #reading the free block
        freeblock=unpack('I',freeblock)



        freeblock=freeblock[0]
        index=index-1
        fp.seek(16,0)
        index=pack('H',index)
        fp.write(index)
        fp.close()
        return freeblock
    elif index==0:
        print 'aditya'
        fp.seek(18,0)
        freeblock=fp.read(4)
        freeblock=unpack('I',freeblock)
        freeblock=freeblock[0]
        fp.seek(adrees_of_free_block)
        link_address=fp.read(4)

        fp.seek(18,0)
        fp.write(link_address)
        fp.seek(16,0)
        index=255
        index=pack('H',index)
        fp.write(index)
        fp.close()
        return freeblock

def add_a_deleted_block(deletedblock):
    fp=open('binary.bin','rb+')
    fp.seek(16,0)
    index=fp.read(2)
    index=unpack('H',index)
    index=index[0]
    if index<255:
        index=index+1                                 #updating the index
        fp.seek(16,0)
        fp.write(pack('H',index))

        linkaddress=fp.read(4)                        #obtaining the linkaddress of free disk blocks zero th block
        linkaddress=unpack('I',linkaddress)
        linkaddress=linkaddress[0]

        fp.seek(linkaddress,0)                      #going to that link and updating the
        fp.seek(index*4,1)                          #updating the block deleted value
        fp.write(pack('I',deletedblock))

    elif index==255:
        fp.seek(18,0)                 #seek to the link address of diskblocks
        linkaddress=fp.read(4)       #reading the linkaddress
        linkaddress=unpack('I',linkaddress)   #storing the linkaddress
        linkaddress=linkaddress[0]

        fp.seek(18,0)                           #updating the linkaddress
        x=pack('I',deletedblock)
        fp.write(x)

        fp.seek(deletedblock)                 #going to the deletedblock and updating thelink
        fp.write(pack('I',linkaddress))
        fp.seek(16,0)                         #updating the index to 0
        fp.write(pack('H',0))
    fp.close()

def return_free_inode_number():
    fp=open('binary.bin','rb+')
    fp.seek(24,0)
    index_of_inode=fp.read(2)                  #reading the index of the inode list
    index_of_inode=unpack('H',index_of_inode)
    index_of_inode=index_of_inode[0]
    if index_of_inode!=0:                     #if index in inode is not zero
        fp.seek(26,0)
        fp.seek(index_of_inode*2,1)           #goto the corresponding index and retrieve the inode number
        free_inode_number=fp.read(2)
        free_inode_number=unpack('H',free_inode_number)   #unpacking the freeinode number and
        free_inode_number=free_inode_number[0]
        index_of_inode=index_of_inode-1         #updating the index as the free inode is assigned
        fp.seek(24,0)
        fp.write(pack('H',index_of_inode))
        fp.close()
        return free_inode_number
    elif index_of_inode==0:
        fp.seek(26,0)
        last_index=fp.read(2)
        last_index = unpack('H',last_index)
        last_index=last_index[0]
        search_for_free_inodeuntil_list_fills(last_index)
        fp.close()
        return last_index

def  search_for_free_inodeuntil_list_fills(lastindex):
    fp=open('binary.bin','rb+')
    offset=2048
    how_many_fit=10
    length=lastindex/how_many_fit
    i=0
    while i<length:
        fp.seek(offset+1024-4)

        offset=fp.read(4)
        offset=unpack('I',offset)
        offset=offset[0]
        i=i+1
    inodeoffset=lastindex%how_many_fit*100+offset
    inodeoffset=inodeoffset+100
    lastindex=lastindex+1
    fp.seek(inodeoffset,0)
    count=0
    lis=[]
    indentified_empty=False
    while count<100:

        if inodeoffset==offset+1000:

            fp.seek(offset+1020,0)
            data=fp.read(4)
            data=unpack('I',data)
            data=data[0]
            if data==1:

                offset1=return_a_freeblock()
                fp.seek(offset+1020,0)
                fp.write(pack('I',offset1))
                offset=offset1
                indentified_empty=True
                break
            else:

                    offset=data
                    inodeoffset=data


        else:

            data=fp.read(28)


            data=unpack('28s',data)

            if data=='None' :
                lis.append(lastindex)
                count=count+1

        lastindex=lastindex+1
        inodeoffset=inodeoffset+100
        fp.seek(inodeoffset,0)
    else:
        fp.seek(22,0)
        fp.write(pack('H',100))
        fp.write(pack('H',99))
        i=len(lis)-1
        while i>=0:
            print 'yaswitha'
            fp.write(pack('H',lis[i]))
            i=i-1


    if indentified_empty==True:
        i=0

        while i<10:

            lis.append(lastindex)
            lastindex=lastindex+1
            i=i+1
            count=count+1

        fp.seek(offset+1024-4)


        offset=return_a_freeblock()


        fp.write(pack('I',offset))
        i=0
        while i<10:

            lis.append(lastindex)
            lastindex=lastindex+1
            i=i+1
            count=count+1
        fp.seek(offset+1020,0)

        fp.write(pack('I',1))
        fp.seek(22,0)
        fp.write(pack('H',count))
        fp.write(pack('H',count-1))
        i=len(lis)-1
        while i>=0:
            fp.write(pack('H',lis[i]))
            i=i-1
    fp.close()
def intialise_inode_numbers():
    fp=open('binary.bin','rb+')
    offset=2048
    lis=[]
    count=0
    inodenumber=0
    while count<100:
        i=0
        fp.seek(offset+1024-4,0)
        if count!=0:
            offset=return_a_freeblock()
            fp.write(pack('I',offset))
        while i<10:
            lis.append(inodenumber)
            inodenumber=inodenumber+1
            count=count+1
            i=i+1
    fp.seek(offset+1020,0)
    fp.write(pack('I',1))
    fp.seek(22,0)
    fp.write(pack('H',count))
    fp.write(pack('H',count-1))
    i=len(lis)-1
    while i>=0:
        fp.write(pack('H',lis[i]))
        i=i-1

    fp.close()


def add_a_deleted_inode(deletedinodenumber):
    fp=open('binary.bin','rb+')
    fp.seek(24,0)
    index=fp.read(2)
    index=unpack('H',index)
    index=index[0]

    if index==99:
        fp.seek(26,0)
        rememredInode=fp.read(2)
        rememredInode=unpack('H',rememredInode)
        rememredInode=rememredInode[0]
        if rememredInode>deletedinodenumber:
            fp.seek(-2,1)
            fp.write(pack('H',deletedinodenumber))
    else:
        index=index+1
        fp.seek(-2,1)
        fp.seek(index*2)
        fp.write(pack('H',deletedinodenumber))
        fp.seek(24,0)
        fp.write(pack('H',index))
    fp.close()


def intialise():
    zeroblock()
    intialise_freediskblocklist()
    intialise_inode_numbers()

def printing(fp):
    fp.seek(26,0)
    count=0
    while count<100:
        data=fp.read(2)
        data=unpack('H',data)
        data=data[0]
        print data
        count=count+1


def testing():
    fp=open('binary.bin','rb+')
    count=0
    print '------------before-------------'
    fp.seek(22,0)
    print 'size is inode list',unpack('H',fp.read(2))[0]
    print 'index of the inode list',unpack('H',fp.read(2))[0]
    while count<100:
       print return_free_inode_number()
       count=count+1
    print '----------------------------------------'
    size=fp.seek(22,0)
    data=fp.read(2)
    data=unpack('H',data)
    data=data[0]
    print 'sizeof inode list',data
    count=0
    index=fp.read(2)
    index=unpack('H',index)
    index=index[0]
    print 'index   is',index
    fp.seek(26,0)
    while count<data:

        print unpack('H',fp.read(2))[0]
        count=count+1
    print return_free_inode_number()
    fp.seek(24,0)
    index=fp.read(2)
    index=unpack('H',index)
    index=index[0]
    print 'index  after returning  is',index
    print '----vikramaditya--------'
    count=0
    while count<20:
          print return_free_inode_number()
          count=count+1
    print '----------------------------------------'
    print '----------------------------------------'
    size=fp.seek(22,0)
    data=fp.read(2)
    data=unpack('H',data)
    data=data[0]
    print 'sizeof inode list',data
    count=0
    index=fp.read(2)
    index=unpack('H',index)
    index=index[0]
    print 'index   is',index
    fp.seek(26,0)
    while count<data:

        print unpack('H',fp.read(2))[0]
        count=count+1





if __name__=='__main__':
     intialise()
     print  'aditya'
     fp=open('binary.bin','rb+')
     print 'vikram'
     #1969514748
     #1073741824
     #1069813760
     i=0
     while i<1000:
        print return_free_inode_number()
        i=i+1
     length=100/10
     offset=2048
     i=0
     while i<length:
        fp.seek(offset+1024-4)

        offset=fp.read(4)
        offset=unpack('I',offset)
        offset=offset[0]
        i=i+1

     fp.seek(offset+1020,0)
     print unpack('I',fp.read(4))

    #printing( fp)


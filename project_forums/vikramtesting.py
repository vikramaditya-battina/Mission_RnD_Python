def vikram():
    freeblock=4096
    free_block_offset=5120
    offset=4096
    i=0
    num=0
    while num<1048571:


        i=0
        while i<256:
           if i==0:
               freeblock=free_block_offset
               print freeblock

           free_block_offset+=1024
           i=i+1
           num=num+1

        num=num+1
if __name__=='__main__':
    vikram()
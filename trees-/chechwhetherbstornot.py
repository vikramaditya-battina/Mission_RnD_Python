from treeutils import *
class bst(object):
    def __init__(self):
        self.value=None
        self.flag=None
    def determinebst(self,root):
        if root.value>=self.value:
            self.value=root.value
        else:
            self.flag=False

def inorder(root,visit):
    if root==None:
        return
    else:

        inorder(root.left,visit)
        visit(root)
        inorder(root.right,visit)

def postorder(root,visit):
    if root==None:
        return
    else:
        postorder(root.left,visit)
        postorder(root.right,visit)
        visit(root)


def preorder(root,visit):
    if root==None:
        return
    else:

        preorder(root.left,visit)
        preorder(root.right,visit)

class vikram(object):
    def __init__(self):
        self.lis=[]
    def append(self,root):
        self.lis.append(root.value)



if __name__=='__main__':

    root=create_tree((1,(5,(2,7,8),6),3))
    check=vikram()

    inorder(root,check.append)
    if check.lis!=sorted(check.lis):
        print 'not a search tree'
    else:
        print 'search tree'

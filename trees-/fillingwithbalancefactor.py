from treeutils import *
class Count():
    count=0
    def __init__(self):
        Count.count+=1

def inorder(root,visit):
    if root==None:
        return
    else:

        inorder(root.left,visit)
        print root.value
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
        visit(root)
        preorder(root.left,visit)
        preorder(root.right,visit)

def visit(root):
     x=0
     y=0
     if root.right==None and root.left==None:
         root.value=1
         return
     if root.right!=None:
         x=root.right.value
     if root.left!=None:
         y=root.left.value
     root.value=max(x,y)+1

def anothervisit(root):
    x=0
    y=0
    if root.left!=None:
       x=root.left.value
    if root.right!=None:
        y=root.right.value
    root.value=x-y
def depth(root):
    if root.value==-1:
        root.value=0
    if root.left!=None:
        root.left.value=root.value+1
    if root.right!=None:
        root.right.value=root.value+1
def intialise(root):
    root.value=-1


if __name__=='__main__':
    print 'vikram'
    root=create_tree((5,(3,1,None),(8,6,9)))
    postorder(root,visit)
    preorder(root,anothervisit)
    inorder(root,visit)
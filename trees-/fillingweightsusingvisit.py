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

        preorder(root.left,visit)
        preorder(root.right,visit)

def visit(root):
     x=0
     y=0
     if root.right!=None:
        x=(root.right).value
     if root.left!=None:
        y=(root.left).value
     root.value=x+y+1


if __name__=='__main__':
    print 'vikram'
    root=create_tree((1,(5,(2,7,8),6),3))
    postorder(root,visit)
    inorder(root,visit)